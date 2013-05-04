# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
import os.path


class FeedEntry(object):
	"""one FeedEntry"""
	def __init__(self, title, published, href, size):
		super(FeedEntry, self).__init__()
		self.title = title
		self.published = published
		self.href = href
		self.size = int(size)
		self.done = False
		self.downloaded = 0
		self.dir = ""
		self.file_name = ""
		self.seek = 0

	def hook_for_urlretrieve(self, block_count, block_size, file_size, done=-1):
		self.size = file_size
		self.downloaded = block_count*block_size
		if self.downloaded == self.size or done is True:
			self.done = True

	def path(self):
		return os.path.join(self.dir, self.file_name)
