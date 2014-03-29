import podpyclient.mainwindow
from PySide.QtGui import QMainWindow, QIcon

class ControlMainWindow(QMainWindow):
  def __init__(self, parent=None):
    super(ControlMainWindow, self).__init__(parent)
    self.ui =  podpyclient.mainwindow.Ui_MainWindow()
    self.ui.setupUi(self)
    self.ui.play_pause_button.setIcon(QIcon("podpyclient/icons/play.svg"))
