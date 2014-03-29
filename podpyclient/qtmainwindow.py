# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


import podpyclient.mainwindow
from PySide.QtGui import QMainWindow, QIcon

class ControlMainWindow(QMainWindow):
  def __init__(self, parent=None):
    super(ControlMainWindow, self).__init__(parent)
    self.ui =  podpyclient.mainwindow.Ui_MainWindow()
    self.ui.setupUi(self)
    self.ui.play_pause_button.setIcon(QIcon("podpyclient/icons/play.svg"))
