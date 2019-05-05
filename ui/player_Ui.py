# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'player.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(799, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("ui/icons/splay.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(_fromUtf8("QMainWindow {\n"
"background: Tomato;\n"
"}"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.videoPlayer = phonon.Phonon.VideoPlayer(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.videoPlayer.sizePolicy().hasHeightForWidth())
        self.videoPlayer.setSizePolicy(sizePolicy)
        self.videoPlayer.setObjectName(_fromUtf8("videoPlayer"))
        self.verticalLayout.addWidget(self.videoPlayer)
        self.seekSlider = phonon.Phonon.SeekSlider(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.seekSlider.sizePolicy().hasHeightForWidth())
        self.seekSlider.setSizePolicy(sizePolicy)
        self.seekSlider.setMaximumSize(QtCore.QSize(16777215, 100))
        self.seekSlider.setObjectName(_fromUtf8("seekSlider"))
        self.verticalLayout.addWidget(self.seekSlider)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.open_file_button = QtGui.QPushButton(self.centralwidget)
        self.open_file_button.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("ui/icons/open_file.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.open_file_button.setIcon(icon3)
        self.open_file_button.setIconSize(QtCore.QSize(20, 19))
        self.open_file_button.setObjectName(_fromUtf8("open_file_button"))
        self.horizontalLayout.addWidget(self.open_file_button)
        self.play_push_button = QtGui.QPushButton(self.centralwidget)
        self.play_push_button.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("ui/icons/play_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play_push_button.setIcon(icon1)
        # self.play_push_button.setIconSize(QtCore.QSize(20, 19))
        self.play_push_button.setObjectName(_fromUtf8("play_push_button"))
        self.horizontalLayout.addWidget(self.play_push_button)
        self.stop_push_button = QtGui.QPushButton(self.centralwidget)
        self.stop_push_button.setStyleSheet(_fromUtf8(""))
        self.stop_push_button.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("ui/icons/stop_icon .png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stop_push_button.setIcon(icon2)
        self.stop_push_button.setIconSize(QtCore.QSize(20, 19))
        self.stop_push_button.setObjectName(_fromUtf8("stop_push_button"))
        self.horizontalLayout.addWidget(self.stop_push_button)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.volumeSlider = phonon.Phonon.VolumeSlider(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.volumeSlider.sizePolicy().hasHeightForWidth())
        self.volumeSlider.setSizePolicy(sizePolicy)
        self.volumeSlider.setObjectName(_fromUtf8("volumeSlider"))
        self.horizontalLayout.addWidget(self.volumeSlider)
        self.fullscreen_push_button = QtGui.QPushButton(self.centralwidget)
        self.fullscreen_push_button.setStyleSheet(_fromUtf8("QPushButton {\n"
"background:Bisque ;\n"
"border-style: solid;\n"
"border-width:1px;\n"
"border-radius:10px;\n"
"max-width:30px;\n"
"max-height:30px;\n"
"min-width:25px;\n"
"min-height:25px;\n"
"}"))
        self.fullscreen_push_button.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("ui/icons/full_screen_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fullscreen_push_button.setIcon(icon3)
        self.fullscreen_push_button.setObjectName(_fromUtf8("fullscreen_push_button"))
        self.fullscreen_push_button.setIconSize(QtCore.QSize(20, 19))
        self.horizontalLayout.addWidget(self.fullscreen_push_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 799, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.menuFile.addAction(self.actionOpen)
        self.menuRecent = self.menuFile.addMenu("Recent")
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "SPlayer", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionOpen.setText(_translate("MainWindow", "Open", None))
        # self.actionRecent.setText(_translate("MainWindow", "Recent", None))

from PySide import phonon
