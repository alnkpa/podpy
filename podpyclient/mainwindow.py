# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'podpyclient/mainwindow.ui'
#
# Created: Fri Mar 28 16:11:52 2014
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(779, 504)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.now_playing_display = QtGui.QLabel(self.centralwidget)
        self.now_playing_display.setMinimumSize(QtCore.QSize(0, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.now_playing_display.setFont(font)
        self.now_playing_display.setText("")
        self.now_playing_display.setTextFormat(QtCore.Qt.PlainText)
        self.now_playing_display.setObjectName("now_playing_display")
        self.verticalLayout_2.addWidget(self.now_playing_display)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.play_pause_button = QtGui.QToolButton(self.centralwidget)
        self.play_pause_button.setMinimumSize(QtCore.QSize(32, 32))
        self.play_pause_button.setAutoRaise(False)
        self.play_pause_button.setObjectName("play_pause_button")
        self.horizontalLayout.addWidget(self.play_pause_button)
        self.seek_slider = QtGui.QSlider(self.centralwidget)
        self.seek_slider.setMinimumSize(QtCore.QSize(86, 32))
        self.seek_slider.setTracking(False)
        self.seek_slider.setOrientation(QtCore.Qt.Horizontal)
        self.seek_slider.setObjectName("seek_slider")
        self.horizontalLayout.addWidget(self.seek_slider)
        self.time_display = QtGui.QLabel(self.centralwidget)
        self.time_display.setMinimumSize(QtCore.QSize(142, 32))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.time_display.setFont(font)
        self.time_display.setText("")
        self.time_display.setTextFormat(QtCore.Qt.PlainText)
        self.time_display.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.time_display.setObjectName("time_display")
        self.horizontalLayout.addWidget(self.time_display)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(0, 17))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setMinimumSize(QtCore.QSize(0, 17))
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.entry_view = QtGui.QListView(self.centralwidget)
        self.entry_view.setMinimumSize(QtCore.QSize(0, 19))
        self.entry_view.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.entry_view.setAlternatingRowColors(True)
        self.entry_view.setUniformItemSizes(True)
        self.entry_view.setObjectName("entry_view")
        self.gridLayout.addWidget(self.entry_view, 1, 1, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.feed_edit = QtGui.QLineEdit(self.centralwidget)
        self.feed_edit.setObjectName("feed_edit")
        self.verticalLayout.addWidget(self.feed_edit)
        self.feed_view = QtGui.QListView(self.centralwidget)
        self.feed_view.setMinimumSize(QtCore.QSize(0, 19))
        self.feed_view.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.feed_view.setAlternatingRowColors(True)
        self.feed_view.setUniformItemSizes(True)
        self.feed_view.setObjectName("feed_view")
        self.verticalLayout.addWidget(self.feed_view)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 779, 25))
        self.menuBar.setObjectName("menuBar")
        self.menu_Help = QtGui.QMenu(self.menuBar)
        self.menu_Help.setObjectName("menu_Help")
        self.menu_Edit = QtGui.QMenu(self.menuBar)
        self.menu_Edit.setObjectName("menu_Edit")
        MainWindow.setMenuBar(self.menuBar)
        self.action_About_Podpy = QtGui.QAction(MainWindow)
        self.action_About_Podpy.setIconVisibleInMenu(False)
        self.action_About_Podpy.setObjectName("action_About_Podpy")
        self.actionAbout_Qt = QtGui.QAction(MainWindow)
        self.actionAbout_Qt.setObjectName("actionAbout_Qt")
        self.action_Set_save_path = QtGui.QAction(MainWindow)
        self.action_Set_save_path.setObjectName("action_Set_save_path")
        self.action_Preferences = QtGui.QAction(MainWindow)
        self.action_Preferences.setObjectName("action_Preferences")
        self.menu_Help.addAction(self.action_About_Podpy)
        self.menu_Help.addAction(self.actionAbout_Qt)
        self.menu_Edit.addAction(self.action_Preferences)
        self.menuBar.addAction(self.menu_Edit.menuAction())
        self.menuBar.addAction(self.menu_Help.menuAction())
        self.label.setBuddy(self.feed_edit)
        self.label_2.setBuddy(self.entry_view)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.feed_edit, self.feed_view)
        MainWindow.setTabOrder(self.feed_view, self.entry_view)
        MainWindow.setTabOrder(self.entry_view, self.play_pause_button)
        MainWindow.setTabOrder(self.play_pause_button, self.seek_slider)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Podpy", None, QtGui.QApplication.UnicodeUTF8))
        self.play_pause_button.setText(QtGui.QApplication.translate("MainWindow", "p", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "&Feeds:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "En&tries:", None, QtGui.QApplication.UnicodeUTF8))
        self.feed_edit.setPlaceholderText(QtGui.QApplication.translate("MainWindow", "new Feed", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Help.setTitle(QtGui.QApplication.translate("MainWindow", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Edit.setTitle(QtGui.QApplication.translate("MainWindow", "&Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.action_About_Podpy.setText(QtGui.QApplication.translate("MainWindow", "&About Podpy", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout_Qt.setText(QtGui.QApplication.translate("MainWindow", "About &Qt", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Set_save_path.setText(QtGui.QApplication.translate("MainWindow", "&Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Preferences.setText(QtGui.QApplication.translate("MainWindow", "&Preferences", None, QtGui.QApplication.UnicodeUTF8))

