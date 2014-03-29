# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import os
import argparse
import yaml
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

class Settings(object):
	"""settings for podpy"""
	_shared_state =  {
	                   "command_line": False,
	                   "torrent_port_start": 6881,
	                   "torrent_port_range": 118,
	                   "torrent_download_rate": -1,
	                   "torrent_upload_rate": -1,
	                   "savePath": "./",
	                   "feeds": [],
	                   "qtOptions": []
					 }

	def __init__(self):
		super(Settings, self).__init__()
		self.__dict__ = self._shared_state

	def parse_args(self):
		print "before " + str(self.__dict__)
		parser = argparse.ArgumentParser(
					epilog="""All options can be truncated to the shortest
								uniquely identifiable version\n
								Please report any bugs and feature requests to
								https://github.com/alnkpa/podpy"""
										 )

		parser.add_argument("-v", "--version", help="output version information",
									action="version",
									version="%(prog)s v0.1.1"
							)
		parser.add_argument("--command-line",
		                   help="""if this parameter is present, the ncurses
		                   			client will be started, instead of the Qt
		                   			application""",
		                   	action="store_const",
		                   	const=True)
		parser.add_argument("--torrent-port-start",
							help="""start of the port range
									for torrent downloads\n(defaults to 6881)""",
							type=int
							)
		parser.add_argument("--torrent-port-range",
							help="""width of the port range
									for torrent downloads\n(defaults to 118)""",
							type=int
							)
		parser.add_argument("--torrent-download-rate",
							help="""maximum download rate for torrent downloads
									\n(defaults to -1 = unlimited)""",
							type=int
							)
		parser.add_argument("--torrent-upload-rate",
							help="""maximum upload rate for torrent downloads
									\n(defaults to -1 = unlimited)""",
							type=int
							)
		parser.add_argument("savePath", help="""path, where downloaded files
												should be saved to""",
										nargs='?'
							)
		parser.add_argument("qtOptions",
		                    help="""All other options will be passed to Qt, if
		                    		using the GUI interface. Otherwise, they
		                    		will be discarded. Beware: if you want to use
		                    		these qtOptions, savePath has to be explicitly
		                    		specified.""",
		                    nargs=argparse.REMAINDER)


		parser.parse_args(namespace=self)

		print "after " + str(self.__dict__)

	#@staticmethod
	def read_prefs(self):
		save_path = os.path.join(os.path.expanduser("~"), ".podpy", "settings.yaml")
		if os.path.isfile(save_path):
			with open(save_path, "r") as f:
				preferences = yaml.load(f, Loader=Loader)

				for pref in preferences:
					setattr(self, pref, preferences[pref])

	#@staticmethod
	def write_prefs(self):
		save_path = os.path.join(os.path.expanduser("~"), ".podpy")
		if not os.path.isdir(save_path):
			os.mkdir(save_path)
		with open(os.path.join(save_path, "settings.yaml"), "w") as f:
			yaml.dump(self.__dict__, f, Dumper=Dumper)
