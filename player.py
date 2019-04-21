import os
import sys
from ui import player_Ui
from PySide import QtGui, QtCore
from PySide.phonon import Phonon

class PlayerData(object):
	def __init__(self):
		self.media_obj = None
	
	def set_source(self, file_path):
		self.media_obj = Phonon.MediaSource(file_path)


class VideoPlayer(player_Ui.Ui_MainWindow, QtGui.QMainWindow):
	def __init__(self):
		super(VideoPlayer, self).__init__()
		self.setupUi(self)
		self.play_instance = PlayerData()

		self.shortcutFull = QtGui.QShortcut(self)
		self.shortcutFull.setKey(QtGui.QKeySequence('F11'))
		self.shortcutFull.setContext(QtCore.Qt.ApplicationShortcut)
		self.shortcutFull.activated.connect(self.toggle_fullscreen)

		self.play_push_button.clicked.connect(self.play_pause_video)
		self.stop_push_button.clicked.connect(lambda: self.videoPlayer.stop())
		self.fullscreen_push_button.clicked.connect(self.toggle_fullscreen)
		self.actionOpen.triggered.connect(self.open_file_browser)

	def toggle_fullscreen(self):
		player_widget = self.videoPlayer.videoWidget()
		if player_widget.isFullScreen():
			player_widget.exitFullScreen()
		else:
			player_widget.enterFullScreen()
	
	def save_selection(self, file_path):
		directory_path = os.path.dirname(file_path)
		settings = QtCore.QSettings()
		settings.setValue("last_selected", directory_path)

	def set_play_pause_icons(self, flag):
		icon1 = QtGui.QIcon()
		if flag == 'pause':
        		icon1.addPixmap(QtGui.QPixmap("ui/icons/pause_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		else:
			icon1.addPixmap(QtGui.QPixmap("ui/icons/play_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        	
		self.play_push_button.setIcon(icon1)

	def open_file_browser(self):
		settings = QtCore.QSettings()
		directory_path = settings.value("last_selected")
		file_path = QtGui.QFileDialog.getOpenFileName(self, 'Select Video', directory_path)[0]
		if file_path:
			self.save_selection(file_path)
			self.play_instance.set_source(file_path)
			self.videoPlayer.load(self.play_instance.media_obj)
			self.play_pause_video()		

	def play_pause_video(self):
		if self.videoPlayer.isPlaying():
			self.videoPlayer.pause()
			self.set_play_pause_icons('play')
		else:
			self.videoPlayer.play()
			self.seekSlider.setMediaObject(self.videoPlayer.mediaObject())
			self.volumeSlider.setAudioOutput(self.videoPlayer.audioOutput())
			self.set_play_pause_icons('pause')


if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	player = VideoPlayer()
	player.show()
	app.exec_()
