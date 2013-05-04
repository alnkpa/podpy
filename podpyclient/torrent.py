#!/usr/bin/env python

# Copyright Daniel Wallin 2006. Use, modification and distribution is
# subject to the Boost Software License, Version 1.0. (See accompanying
# file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)

import os
import time
import libtorrent as lt


class TorrentDownloader(object):
	"""is the interface to libtorrent"""
	def __init__(self, ports=6881, port_range=118, max_download_rate=-1, max_upload_rate=-1):
		super(TorrentDownloader, self).__init__()
		self.ports = ports
		self.port_range = port_range
		self.max_download_rate = max_download_rate
		self.max_upload_rate = max_upload_rate
		self.save_path = './'
		self.handles = {}
		settings = lt.session_settings()
		self.ses = lt.session()
		self.ses.set_download_rate_limit(int(self.max_download_rate))
		self.ses.set_upload_rate_limit(int(self.max_upload_rate))
		self.ses.listen_on(self.ports, self.ports + self.port_range)
		self.ses.set_settings(settings)
		self.ses.set_alert_mask(0xfffffff)

	def addTorrent(self, save_path, path, entry):
		atp = {}
		atp["save_path"] = save_path
		atp["storage_mode"] = lt.storage_mode_t.storage_mode_sparse
		atp["paused"] = False
		atp["auto_managed"] = True
		atp["duplicate_is_error"] = True
		if path.startswith('magnet:') or path.startswith('http://') or path.startswith('https://'):
			atp["url"] = path
		else:
			e = lt.bdecode(open(path, 'rb').read())
			info = lt.torrent_info(e)
			print('Adding \'%s\'...' % info.name())

			try:
				atp["resume_data"] = open(os.path.join(self.save_path, info.name() + '.fastresume'), 'rb').read()
			except:
				pass

			atp["ti"] = info

		h = self.ses.add_torrent(atp)

		self.handles[entry] = h

	def update_info(self):
		for entry, handle in self.handles.iteritems():
			i = handle.get_torrent_info()
			if i.num_files() > 0:
				entry.file_name = i.file_at(0).path
			s = handle.status()
			downloaded = s.total_wanted_done
			size = s.total_wanted
			entry.hook_for_urlretrieve(downloaded, 1, size, s.is_finished)

	def get_handles(self):
		return self.handles.itervalues()

	def main_loop(self):
		pass
		# for h in self.handles:
		# 	out = ''
		# 	if h.has_metadata():
		# 		name = h.get_torrent_info().name()[:40]
		# 	else:
		# 		name = '-'
		# 	out += 'name: %-40s' % name
		# 	s = h.status()
		# 	out += '%5.4f%% ' % (s.progress*100)
		# 	print out

	def stop(self):
		self.ses.pause()
		for h in self.handles.itervalues():
			if not h.is_valid() or not h.has_metadata():
				continue
			data = lt.bencode(h.write_resume_data())
			open(os.path.join(self.save_path, h.get_torrent_info().name() + '.fastresume'), 'wb').write(data)

	def set_save_path(self, path):
		self.save_path = path

if __name__ == '__main__':
	import sys
	client = TorrentDownloader()
	try:
		client.addTorrent(sys.argv[1])
		while 1:
			client.main_loop()
			time.sleep(1)
	except (KeyboardInterrupt, SystemExit):
		client.stop()
