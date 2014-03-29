#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from PySide.QtGui import QApplication, QStringListModel, QIcon
from PySide.QtCore import QTimer

import sys
argv, sys.argv = sys.argv, []
import player
sys.argv = argv

import settings
import entrymodel
import qtmainwindow
import feed
import torrent
import httpdownloader
import os
from datetime import timedelta
import time
import about_podpy
import preferences_dialog

class PodpyQt(object):
	"""graphical interface for Podpy"""

	def __init__(self):
		super(PodpyQt, self).__init__()


	def __enter__(self):
		prefs = settings.Settings()
		self.playing_entry = None

		self.app = QApplication(prefs.qtOptions)
		self.player = player.Player()
		self.torrent = torrent.TorrentDownloader()

		self.main_window = qtmainwindow.ControlMainWindow()
		self.main_window.show()
		self.update_feeds()
		self.main_window.ui.feed_view.activated.connect(self.update_entries)
		self.main_window.ui.entry_view.activated.connect(self.select_entry)
		self.main_window.ui.feed_edit.returnPressed.connect(self.add_feed)
		self.main_window.ui.play_pause_button.clicked.connect(self.toggle_play_pause)
		self.main_window.ui.actionAbout_Qt.triggered.connect(self.app.aboutQt)

		self.about_podpy = about_podpy.ControlMainWindow()
		self.preferences_dialog = preferences_dialog.ControlMainWindow()

		self.main_window.ui.action_About_Podpy.triggered.connect(self.about_podpy.show)
		self.main_window.ui.action_About_Podpy.triggered.connect(self.disable_main_window)
		self.main_window.ui.action_Preferences.triggered.connect(self.enable_pref_window)
		self.main_window.ui.action_Preferences.triggered.connect(self.disable_main_window)
		self.preferences_dialog.finished.connect(self.prefs_finished)
		self.about_podpy.finished.connect(self.enable_main_window)

	def __exit__(self, exc_type, exc_value, traceback):
		self.app.quit()
		return True

	def start(self):
		exit_code = self.app.exec_()

		self.terminate()

		return exit_code


	def terminate(self):
		if not self.playing_entry is None:
			self.playing_entry.timer.stop()
			del self.playing_entry.timer

		prefs = settings.Settings()
		self.player.terminate()
		self.torrent.stop()

		prefs.write_prefs()

	def select_entry(self, index):
		prefs = settings.Settings()
		feed_number = self.main_window.ui.feed_view.currentIndex().row()

		entry = prefs.feeds[feed_number].sorted_encs()[index.row()]

		dir_name = os.path.abspath(
		                           os.path.join(prefs.savePath,
		                                        prefs.feeds[feed_number].title.lower().replace(' ', '_')
		                                        )
		                           )
		if not os.path.isdir(dir_name):
			os.mkdir(dir_name)
		if entry.done:
			self.play_sound(entry)
		else:
			entry.dir = dir_name
			if entry.href.endswith(".torrent"):
				self.torrent_downloader.addTorrent(dir_name, entry.href, entry)
			else:
				entry_name = entry.href.split("/")[-1]
				entry.file_name = entry_name
				if os.path.exists(entry.path()):
					entry.done = True
					entry.downloaded = entry.size = os.path.getsize(entry.path())
					return

				httpdownloader.download(entry,
				                        entry.path(),
				                        self.main_window.ui.entry_view.model().hook_for_urlretrieve)

	def add_feed(self):
		prefs = settings.Settings()
		prefs.feeds.append(feed.Feed(self.main_window.ui.feed_edit.text()))
		self.update_feeds()

	def update_feeds(self):
		prefs = settings.Settings()

		for feed in prefs.feeds:
			feed.update_encs()

		self.main_window.ui.feed_view.setModel(QStringListModel([x.title for x in prefs.feeds]))

	def update_entries(self, index):
		prefs = settings.Settings()
		feed = prefs.feeds[index.row()]

		model = entrymodel.EntryModel(feed.sorted_encs())
		self.main_window.ui.entry_view.setModel(model)

	def play_sound(self, entry):
		if not self.playing_entry is None:
			self.playing_entry.timer.stop()
			del self.playing_entry.timer

		self.playing_entry = entry
		self.main_window.ui.now_playing_display.setText(entry.title)
		self.player.play(entry)

		time.sleep(0.001)

		self.player.seek(entry.seek)

		self.main_window.ui.seek_slider.setRange(0, int(entry.duration/(10**9)))
		self.main_window.ui.seek_slider.setSingleStep(int(int(entry.duration/(10**9))/1000))
		self.main_window.ui.seek_slider.setPageStep(int(int(entry.duration/(10**9))/100))

		self.playing_entry.timer = QTimer()
		self.playing_entry.timer.timeout.connect(self.update_time_display)
		self.playing_entry.timer.start()

		self.update_play_pause_icon()

	def update_time_display(self):
		self.player.update()
		seek = timedelta(microseconds=(self.playing_entry.seek/1000))
		duration = timedelta(microseconds=(self.playing_entry.duration/1000))
		self.main_window.ui.time_display.setText(str(seek)[0:-5] + " / " + str(duration)[0:-5])
		self.main_window.ui.seek_slider.setValue(seek.total_seconds())

	def toggle_play_pause(self):
		self.player.toggle_play_pause()

		self.update_play_pause_icon()

	def update_play_pause_icon(self):
		if self.player.state is player.Player.PLAYING:
			self.main_window.ui.play_pause_button.setIcon(QIcon("podpyclient/icons/pause.svg"))
		elif self.player.state is player.Player.PAUSED:
			self.main_window.ui.play_pause_button.setIcon(QIcon("podpyclient/icons/play.svg"))

	def disable_main_window(self):
		self.main_window.setDisabled(True)

	def enable_main_window(self):
		self.main_window.setEnabled(True)

	def enable_pref_window(self):
		prefs = settings.Settings()
		ui = self.preferences_dialog.ui
		ui.port_start_spin_box.setValue(prefs.torrent_port_start)
		ui.port_range_spin_box.setValue(prefs.torrent_port_range)
		ui.download_rate_spin_box.setValue(prefs.torrent_download_rate)
		ui.upload_rate_spin_box.setValue(prefs.torrent_upload_rate)
		ui.save_path_line_edit.setText(prefs.savePath)

		self.preferences_dialog.show()

	def prefs_finished(self, result):

		if result is 1:
			prefs = settings.Settings()
			ui = self.preferences_dialog.ui

			prefs.torrent_port_start = ui.port_start_spin_box.value()
			prefs.torrent_port_range = ui.port_range_spin_box.value()
			prefs.torrent_download_rate = ui.download_rate_spin_box.value()
			prefs.torrent_upload_rate = ui.upload_rate_spin_box.value()
			prefs.savePath = ui.save_path_line_edit.text()

		self.enable_main_window()
