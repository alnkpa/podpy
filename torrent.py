#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import sys
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
		self.handles = []
		settings = lt.session_settings()
		self.ses = lt.session()
		self.ses.set_download_rate_limit(int(self.max_download_rate))
		self.ses.set_upload_rate_limit(int(self.max_upload_rate))
		self.ses.listen_on(self.ports, self.ports + self.port_range)
		self.ses.set_settings(settings)
		self.ses.set_alert_mask(0xfffffff)

	def addTorrent(self, path):
		atp = {}
		atp["save_path"] = self.save_path
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

		self.handles.append(h)

	def main_loop(self):
		for h in self.handles:
			out = ''
			if h.has_metadata():
				name = h.get_torrent_info().name()[:40]
			else:
				name = '-'
			out += 'name: %-40s' % name
			s = h.status()
			out += '%5.4f%% ' % (s.progress*100)
			print out

	def stop(self):
		self.ses.pause()
		for h in self.handles:
			if not h.is_valid() or not h.has_metadata() or (4 < h.status().state < 7):
				continue
			data = lt.bencode(h.write_resume_data())
			open(os.path.join(self.save_path, h.get_torrent_info().name() + '.fastresume'), 'wb').write(data)

	def set_save_path(self, path):
		self.save_path = path

if __name__ == '__main__':
	client = TorrentDownloader()
	try:
		client.addTorrent(sys.argv[1])
		while 1:
			client.main_loop()
			time.sleep(1)
	except (KeyboardInterrupt, SystemExit):
		client.stop()
