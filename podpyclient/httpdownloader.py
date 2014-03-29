# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
import urllib
import thread
import functools

def download(entry, save_path, hook):
	try:
		thread.start_new_thread(urllib.urlretrieve,
		                        (entry.href,
		                         save_path,
		                         functools.partial(hook, entry)))
	except urllib.ContentTooShortError as e:
		raise e

class HttpDownloader(object):
	"""is the interface for http downloads"""
	def __init__(self, hook):
		super(HttpDownloader, self).__init__()


	def main_loop(self):
		pass

	def _hook_for_urlretrieve(self, block_count, block_size, file_size):
		pass
