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

class FullScreenWidget(QtGui.QWidget):
    def __init__(self, videoPlayer, seek_slider, fullscreen_push_button):
        super(FullScreenWidget, self).__init__()
        self.videoPlayer = videoPlayer
        self.player_widget = self.videoPlayer.videoWidget()
        self.seek_slider = seek_slider
        self.fullscreen_push_button = fullscreen_push_button
        self.setMouseTracking(True)

    def go_full_screen(self):
        self.setup_widget()
        self.fullscreen_push_button.clicked.connect(self.exit_fullscreen)
        self.showFullScreen()

    def return_widgets(self):
        self.seek_slider.show()
        self.fullscreen_push_button.show()
        return [
            self.videoPlayer,
            self.player_widget, 
            self.seek_slider, 
            self.fullscreen_push_button
        ]

    def exit_fullscreen(self):
        self.hide()

    def mouseMoveEvent(self, QMouseEvent):
        if QMouseEvent.pos().y() < 700:
            self.seek_slider.hide()
            self.fullscreen_push_button.hide()

        else:
            self.seek_slider.show()
            self.fullscreen_push_button.show()

    def setup_widget(self):
        self.setStyleSheet(_fromUtf8("QWidget {\n"
            "background: Black;\n"
            "}"))
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.verticalLayout = QtGui.QVBoxLayout(self)
        self.verticalLayout.addWidget(self.player_widget)
        self.verticalLayout.setContentsMargins(1,0,0,0)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.addWidget(self.seek_slider)
        self.horizontalLayout.addWidget(self.fullscreen_push_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
