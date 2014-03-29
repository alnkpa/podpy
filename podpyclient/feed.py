# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
import feedparser
import entry
import time


class Feed(object):
	"""one RSS/Atom-Feed"""
	def __init__(self, path):
		super(Feed, self).__init__()
		self.path = path
		feed = feedparser.parse(self.path)
		self.title = feed.feed.title
		self.etag = None
		self.modified = None
		if not hasattr(self, 'encs'):
			self.encs = {}
		self.update_encs(feed)

	def get_enclosures(self, feed):
		for e in feed.entries:
			if not e.published_parsed in self.encs:
				self.encs[e.published_parsed] = entry.FeedEntry(e.title,
				                                                e.published_parsed,
				                                                e.enclosures[0].href,
				                                                e.enclosures[0].length)

	def update_encs(self, feed=None):
		if feed is None:
			feed = feedparser.parse(self.path, etag=self.etag, modified=self.modified)
		if "etag" in feed:
			self.etag = feed.etag
		if "modified" in feed:
			self.modified = feed.modified
		self.get_enclosures(feed)

	def sorted_encs(self):
		return [self.encs[key] for key in sorted(self.encs.iterkeys(), reverse=True)]
