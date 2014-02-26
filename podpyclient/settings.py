class Settings(object):
	"""settings for podpy"""
	_shared_state = {}
	def __init__(self):
		super(Settings, self).__init__()
		self.__dict__ = self._shared_state
