# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'podpyclient/about_podpy.ui'
#
# Created: Fri Mar  7 18:48:09 2014
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 153)
        Dialog.setMinimumSize(QtCore.QSize(400, 153))
        Dialog.setMaximumSize(QtCore.QSize(400, 153))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(306, 117, 85, 27))
        self.pushButton.setMaximumSize(QtCore.QSize(85, 27))
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(9, 9, 382, 102))
        self.label.setMinimumSize(QtCore.QSize(382, 102))
        self.label.setWordWrap(True)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "About Podpy", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Dialog", "Ok", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "<html><head/><body><p>The code for Podpy is licensed under the <a href=\"https://www.mozilla.org/MPL/2.0/\"><span style=\" text-decoration: underline; color:#0000ff;\">Mozilla Public License Version 2.0</span></a>. For an easy run-down on what you may or may not do, please consult the <a href=\"https://www.mozilla.org/MPL/2.0/FAQ.html\"><span style=\" text-decoration: underline; color:#0000ff;\">FAQ</span></a> of the MPL. You may find the Source Code Form of this Executable as required by MPL at <a href=\"https://github.com/alnkpa/podpy\"><span style=\" text-decoration: underline; color:#0000ff;\">https://github.com/alnkpa/podpy</span></a>.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

