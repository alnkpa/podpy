# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from podpyclient.podpyqt import PodpyQt
from podpyclient.settings import Settings

def start():
	prefs = Settings()
	prefs.read_prefs()
	client = PodpyQt()

	with client:
		client.start()
