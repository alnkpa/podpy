import about_podpy_dialog
from PySide import QtGui

class ControlMainWindow(QtGui.QDialog):
  def __init__(self, parent=None):
    super(ControlMainWindow, self).__init__(parent)
    self.ui = about_podpy_dialog.Ui_Dialog()
    self.ui.setupUi(self)

