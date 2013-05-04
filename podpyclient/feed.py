# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
import feedparser
import entry


class Feed(object):
	"""one RSS/Atom-Feed"""
	def __init__(self, path):
		super(Feed, self).__init__()
		self.path = path
		self.feed = feedparser.parse(self.path)
		self.title = self.feed.feed.title
		self.encs = self.get_enclosures()

	def get_enclosures(self):
		l = []
		for e in self.feed.entries:
			l.append(entry.FeedEntry(e.title, e.published_parsed, e.enclosures[0].href, e.enclosures[0].length))
		return l
		#return {e.published_parsed: e.enclosures[0].href for e in self.feed.entries}
