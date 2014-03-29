# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


import about_podpy_dialog
from PySide import QtGui

class ControlMainWindow(QtGui.QDialog):
  def __init__(self, parent=None):
    super(ControlMainWindow, self).__init__(parent)
    self.ui = about_podpy_dialog.Ui_Dialog()
    self.ui.setupUi(self)

