# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


from PySide.QtCore import QAbstractListModel, QModelIndex, Qt
import time
from utilities import sizeof_fmt

class EntryModel(QAbstractListModel):
	"""a model that fits a list of entries to qt"""
	def __init__(self, entry_list, parent=None):
		super(EntryModel, self).__init__(parent)
		self.entry_list = entry_list

	def flags(self, i):
		return Qt.ItemIsEnabled | Qt.ItemIsSelectable

	def data(self, index, role=Qt.DisplayRole):
		i = index.row()
		if role == Qt.DisplayRole:
			entry = self.entry_list[i]
			string = ""
			string += entry.title + "\n"
			string += time.asctime(entry.published) + "\n"
			string += sizeof_fmt(entry.downloaded) + " / " + sizeof_fmt(entry.size)
			return string

	def headerData(self, section, orientation, role=Qt.DisplayRole):
		return ""

	def rowCount(self, parent=QModelIndex()):
		return len(self.entry_list)

	def hook_for_urlretrieve(self, entry, block_count, block_size, file_size):
		entry.hook_for_urlretrieve(block_count, block_size, file_size)
		index = self.entry_list.index(entry)
		self.dataChanged.emit(self.createIndex(index, 0),
		                      self.createIndex(index, 0))
