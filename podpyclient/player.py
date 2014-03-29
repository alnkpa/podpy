#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

# credit goes to the tutorial of pygst at
# http://pygstdocs.berlios.de/pygst-tutorial/index.html

import pygst
import threading
import glib
import gst
import gobject
import os.path
import time


class Player(object):
	"""plays sounds"""

	NULL = -1
	PAUSED = 0
	PLAYING = 1

	def __init__(self):
		super(Player, self).__init__()
		self.playing_entry = None
		self.state = Player.NULL
		gobject.threads_init()
		self.glib_main_loop = glib.MainLoop()
		self.glib_main_loop_thread = threading.Thread(target=self.glib_main_loop.run)
		self.glib_main_loop_thread.start()
		self.player = gst.element_factory_make("playbin2", "podpyplayer")
		fakesink = gst.element_factory_make("fakesink", "fakesink")
		self.player.set_property("video-sink", fakesink)
		bus = self.player.get_bus()
		bus.add_signal_watch()
		bus.connect("message", self.on_message)

	def terminate(self):
		self.state = Player.NULL
		self.player.set_state(gst.STATE_NULL)
		self.glib_main_loop.quit()

	def toggle_play_pause(self):
		if self.state == Player.NULL:
			return
		elif self.state == Player.PAUSED:
			self.play()
		elif self.state == Player.PLAYING:
			self.pause()

	def play(self, entry=None):
		self.state = Player.PLAYING
		if entry is None:
			self.player.set_state(gst.STATE_PLAYING)
			return
		self.player.set_state(gst.STATE_NULL)
		self.playing_entry = entry
		self.player.set_property("uri", "file://" + os.path.abspath(entry.path()))
		self.player.set_state(gst.STATE_PAUSED)
		# self.player.seek_simple(gst.FORMAT_TIME, gst.SEEK_FLAG_FLUSH, entry.seek)
		self.player.set_state(gst.STATE_PLAYING)
		# neither worked
		while True:
			try:
				duration = self.player.query_duration(gst.FORMAT_TIME, None)[0]
				break
			except gst.QueryError:
				pass
		self.playing_entry.duration = duration

	def pause(self):
		self.state = Player.PAUSED
		self.player.set_state(gst.STATE_PAUSED)
		self.update()

	def stop(self):
		self.state = Player.NULL
		self.player.set_state(gst.STATE_NULL)

	def seek(self, time):
		self.player.seek_simple(gst.FORMAT_TIME,
		                        gst.SEEK_FLAG_FLUSH | gst.SEEK_FLAG_KEY_UNIT,
		                        time)

	def update(self):
		if not self.playing_entry is None:
			try:
				pos_int = self.player.query_position(gst.FORMAT_TIME, None)[0]
				self.playing_entry.seek = pos_int
			except gst.QueryError:
				pass

	def on_message(self, bus, message):
		t = message.type
		if t == gst.MESSAGE_EOS or t == gst.MESSAGE_ERROR:
			self.playing_entry = None
			self.player.set_state(gst.STATE_NULL)
			self.state = Player.NULL

if __name__ == '__main__':
	import time
	import sys

	class DummyEntry(object):
		"""docstring for DummyEntry"""
		def __init__(self):
			super(DummyEntry, self).__init__()
			self.seek = 0

			print self.seek

		def path(self):
			return sys.argv[1]

	player = Player()
	entry = DummyEntry()
	player.play(entry)
	time.sleep(10)
	player.terminate()
