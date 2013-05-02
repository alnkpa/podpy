# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


class FeedEntry(object):
	"""one FeedEntry"""
	def __init__(self, title, published, href, size):
		super(FeedEntry, self).__init__()
		self.title = title
		self.published = published
		self.href = href
		self.size = int(size)
		self.downloading = False
		self.downloaded = 0