# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
import urllib
import thread


class HttpDownloader(object):
	"""is the interface for htpp errors"""
	def __init__(self, hook, save_path="./"):
		super(HttpDownloader, self).__init__()
		self.save_path = save_path
		self.download_progress = -1
		self.file_size = -1
		self.hook = hook

	def download(self, path):
		try:
			thread.start_new_thread(urllib.urlretrieve, (path, self.save_path, self.hook))
		except urllib.ContentTooShortError as e:
			raise e

	def main_loop(self):
		pass

	def _hook_for_urlretrieve(self, block_count, block_size, file_size):
		pass
