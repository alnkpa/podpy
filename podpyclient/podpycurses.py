# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
import curses
import feed
import locale
import time
import os
import argparse

import torrent
import httpdownloader


# credit to Fred Cirera
def sizeof_fmt(num):
	for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
		if num < 1024.0:
			return "%3.1f %s" % (num, x)
		num /= 1024.0


class PodPyCurses(object):
	"""a curses controller for podpy"""
	def __init__(self):
		super(PodPyCurses, self).__init__()
		self.parse_args()
		if self.args.version:
			print """podpy v0.1.1"""
			return
		self.torrent_downloader = torrent.TorrentDownloader()
		self.feeds = []
		self.downloaders = [self.torrent_downloader]
		self.active_feed = 0
		self.page = 0

		curses.wrapper(self.start_curses)

	def parse_args(self):
		parser = argparse.ArgumentParser()

		parser.add_argument("--version", help="output version information",
									action="store_true")

		self.args = parser.parse_args()

	def start_curses(self, stdscr):
		### start foo, no blinking cursor, string encoding
		curses.curs_set(0)
		curses.start_color()
		locale.setlocale(locale.LC_ALL, '')
		self.code = locale.getpreferredencoding()

		### we need that in so many functions, we might as well save it
		self.stdscr = stdscr

		### have a nice border and non blocking getch
		self.stdscr.border()
		self.stdscr.nodelay(1)

		### add the global control elements
		### TODO put it in a seperate function
		height, width = self.stdscr.getmaxyx()
		self.stdscr.addch(height - 2, 2, 'n', curses.A_BOLD | curses.A_UNDERLINE)
		self.stdscr.addstr(height - 2, 3, "ew feed")
		self.stdscr.refresh()

		### the window for the actual feed entries
		self.pod_list = self.stdscr.derwin(height - 8, width - 2, 4, 1)

		### TODO add timed pod_list update
		now = time.time()
		### control
		while 1:
			inp = stdscr.getch()
			char = chr(inp) if 0 <= inp <= 255 else ''

			if char == 'q':
				### exit
				break
			elif char == 'n':
				### new feed
				self.feeds.append(feed.Feed(self.new_feed()))
				self.paint_tabs()
			elif inp == curses.KEY_LEFT:
				### feed to the left
				self.active_feed = (self.active_feed - 1) % len(self.feeds)
				self.page = 0
				self.paint_tabs()
			elif inp == curses.KEY_RIGHT:
				### feed to the right
				self.active_feed = (self.active_feed + 1) % len(self.feeds)
				self.page = 0
				self.paint_tabs()
			elif inp == curses.KEY_UP:
				### go one page up
				if self.page != 0:
					self.page -= 1
				self.update_pod_list()
			elif inp == curses.KEY_DOWN:
				### go one page down
				self.page += 1
				self.update_pod_list()
			elif '0' <= char <= '9':
				### select an entry for download or TODO play it
				integer = int(char)
				index = self.page * self.pod_list.getmaxyx()[0]/3 + integer
				cur_feed = self.feeds[self.active_feed]
				if index < len(cur_feed.encs):
					self.select_enc(cur_feed, index)

			### update pod_list once per second
			if time.time() - now > 1:
				self.update_pod_list()
				now = time.time()

	def select_enc(self, feed, index):
		dir_name = feed.title.lower().replace(' ', '_')
		if not os.path.isdir(dir_name):
			os.mkdir(dir_name)
		entry = feed.encs[index]
		if entry.done:
			self.play_sound(entry)
		else:
			entry.dir = dir_name
			if entry.href.endswith(".torrent"):
				self.torrent_downloader.addTorrent(dir_name, entry.href, entry)
			else:
				entry_name = entry.href.split("/")[-1]
				entry.path = entry_name
				if os.path.exists(entry.path()):
					entry.done = True
					entry.downloaded = entry.size = os.path.getsize(entry.path())
					return
				self.downloaders.append(httpdownloader.HttpDownloader(entry.hook_for_urlretrieve, entry.path()))
				self.downloaders[-1].download(entry.href)

	def play_sound(self, entry):
		pass

	def new_feed(self):
		### ask for feed url
		height, width = self.stdscr.getmaxyx()
		beginning_h = max(height/2 - 3, 0)
		beginning_w = max(width/2 - 30, 0)
		win = self.stdscr.derwin(6, 60, beginning_h, beginning_w)
		win.addstr(1, 17, "Please input the feed url", curses.A_DIM)
		win.addstr(3, 3, " "*54, curses.A_UNDERLINE)
		win.box()
		win.refresh()

		### shortly, have a blinking cursor and echo what's been written
		curses.echo()
		curses.curs_set(1)
		string = win.getstr(3, 3)
		curses.noecho()
		curses.curs_set(0)
		win.clear()
		return string

	def paint_tabs(self):
		height, width = self.stdscr.getmaxyx()

		for i in range(0, min(len(self.feeds), width/40)):
			attr = 0
			if i == self.active_feed:
				self.stdscr.addch(1, 40*i + 3, curses.ACS_LARROW, curses.A_BOLD | curses.A_UNDERLINE)
				self.stdscr.addch(1, 40*i + 37, curses.ACS_RARROW, curses.A_BOLD | curses.A_UNDERLINE)
				attr = curses.A_BOLD
			else:
				self.stdscr.addch(1, 40*i + 3, ' ')
				self.stdscr.addch(1, 40*i + 37, ' ')
			self.stdscr.addnstr(1, 40*i + 5, self.feeds[i].title.encode(self.code), 30, attr)
			self.stdscr.addch(0, 40*i + 1, curses.ACS_TTEE)
			self.stdscr.addch(1, 40*i + 1, curses.ACS_VLINE)
			self.stdscr.addch(2, 40*i + 1, curses.ACS_LLCORNER)
			self.stdscr.hline(2, 40*i + 2, curses.ACS_HLINE, 37)
			self.stdscr.addch(2, 40*i + 39, curses.ACS_LRCORNER)
			self.stdscr.addch(0, 40*i + 39, curses.ACS_TTEE)
			self.stdscr.addch(1, 40*i + 39, curses.ACS_VLINE)
		self.stdscr.refresh()
		self.update_pod_list()

	def update_pod_list(self):
		### if there a no feeds, we don't need to update the pod_list
		if not self.feeds:
			return

		### paint pod_list completely new, it's easier
		self.pod_list.clear()

		self.torrent_downloader.update_info()

		feed = self.feeds[self.active_feed]
		encs = feed.encs
		height, width = self.pod_list.getmaxyx()

		for i in range(0, min(len(encs), height/3)):
			index = self.page * height / 3 + i
			if index >= len(encs):
				break

			### paint downloading items bold
			attr = curses.A_BOLD if encs[index].done else 0
			### numbers
			self.pod_list.addch(3*i, 1, str(i), curses.A_BOLD | curses.A_UNDERLINE)
			### name
			self.pod_list.addnstr(3*i, 3, encs[index].title.encode(self.code), width - 3, attr)
			### date
			self.pod_list.addnstr(3*i + 1, 5, time.asctime(encs[index].published), 20)

			### progress
			down_string = sizeof_fmt(encs[index].downloaded)
			down_string += " / " + sizeof_fmt(encs[index].size)
			self.pod_list.addnstr(3*i + 1, 27, down_string, width - 30)
		self.pod_list.refresh()
