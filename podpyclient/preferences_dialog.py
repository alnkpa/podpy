import preferences_window
from PySide import QtGui

class ControlMainWindow(QtGui.QDialog):
	def __init__(self, parent=None):
	    super(ControlMainWindow, self).__init__(parent)
	    self.ui = preferences_window.Ui_Dialog()
	    self.ui.setupUi(self)
	    self.ui.save_path_push_button.clicked.connect(self.ask_for_dir)

	def ask_for_dir(self):
		self.ui.save_path_line_edit.setText(QtGui.QFileDialog.getExistingDirectory(self))
