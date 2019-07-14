""" This module define the full screen widget UI and functionality.
"""
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
    """ The class that define the player UI on going full screen.
            
        The full screen widget class defines the player functionality and 
        the widget UI when the player enters fullscreen.
    """
    def __init__(self, video_player, seek_slider, fullscreen_push_button):
        """ The Initialization method of the class.

            Args:
                video_player (obj): The phonon video player widget used in the video player.
                seek_slider (obj): The phonon seek slider widget.
                fullscreen_push_button (obj): The Qt Push Button widget.
        """
        super(FullScreenWidget, self).__init__()
        self.video_player = video_player
        self.player_widget = self.video_player.videoWidget()
        self.seek_slider = seek_slider
        self.fullscreen_push_button = fullscreen_push_button
        self.setMouseTracking(True)

    def go_full_screen(self):
        """ This method makes the widget go in full screen mode.
        """
        self.setup_widget()
        self.fullscreen_push_button.clicked.connect(self.exit_fullscreen)
        self.showFullScreen()

    def return_widgets(self):
        """ Returns the widgets back once the fullscreen in exited.
        """
        self.seek_slider.show()
        self.fullscreen_push_button.show()
        # returns the widgets back to the player widget UI class
        return [
            self.video_player,
            self.player_widget, 
            self.seek_slider, 
            self.fullscreen_push_button
        ]

    def exit_fullscreen(self):
        """ Hides the fullscreen widget.
        """
        self.hide()

    def mouseMoveEvent(self, QMouseEvent):
        """ The Qt mouse move event function being overriden.

            The mouse move is detected along with the position of the pointer, this is used
            to show and hide the seeker widget on full screen.
        """
        if QMouseEvent.pos().y() < 700:
            self.seek_slider.hide()
            self.fullscreen_push_button.hide()

        else:
            self.seek_slider.show()
            self.fullscreen_push_button.show()

    def setup_widget(self):
        """ Sets the fullscreen mode.
        """
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
