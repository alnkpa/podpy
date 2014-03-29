from podpyclient.podpyqt import PodpyQt
from podpyclient.settings import Settings

def start():
	prefs = Settings()
	prefs.read_prefs()
	client = PodpyQt()

	with client:
		client.start()
