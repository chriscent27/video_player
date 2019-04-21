import os
import sys
from ui import player_Ui
from PySide import QtGui, QtCore
from PySide.phonon import Phonon

class PlayerData(object):
	def __init__(self):
		self.media_obj = None
		self.qactions = dict()
		self.recent_files = list()
		self.settings = QtCore.QSettings()
		self.play_pause_icons = {
			'play': None,
			'pause': None,	
		}
		self.create_play_pause_icons()
		#self.set_recent_files()

	def create_play_pause_icons(self):
		self.play_pause_icons['play'] = QtGui.QIcon()
		self.play_pause_icons['play'].addPixmap(QtGui.QPixmap("ui/icons/play_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.play_pause_icons['pause'] = QtGui.QIcon()
		self.play_pause_icons['pause'].addPixmap(QtGui.QPixmap("ui/icons/pause_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

	def set_recent_files(self): 
		selected_files = self.settings.value('selected_files')
		print('selected_files  ',selected_files)
		if selected_files.__class__ == list:
			self.recent_files = selected_files
		else:
			self.recent_files = list()
		
	def add_to_recent_files(self, file_path):
		self.set_recent_files()
		self.recent_files.append(file_path)
		self.recent_files = list(set(self.recent_files))
		if len(self.recent_files) > 10:
			self.recent_files.pop(0)

		self.settings.setValue('selected_files', self.recent_files)
		print('self.recent_files', self.recent_files)

	def get_last_selected_directory(self):
		return self.settings.value("last_selected")

	def set_last_selected_directory(self, file_path):
		directory_path = os.path.dirname(file_path)
		self.settings.setValue("last_selected", directory_path)

	def set_source(self, file_path):
		self.media_obj = Phonon.MediaSource(file_path)


class VideoPlayer(player_Ui.Ui_MainWindow, QtGui.QMainWindow):
	def __init__(self):
		super(VideoPlayer, self).__init__()
		self.setupUi(self)
		self.data = PlayerData()
		self.create_shortcuts()
		self.connect_signals_and_slots()
		self.populate_recent_files_menu()
		

	def populate_recent_files_menu(self):
		file_paths = self.data.recent_files
		if file_paths.__class__ == list:
			for file_path in file_paths:
				file_name = os.path.basename(file_path)
				print('file_path', file_path)
				self.data.qactions[file_path] = QtGui.QAction(self)
				self.data.qactions[file_path].setText(file_name)
				self.data.qactions[file_path].triggered.connect(lambda:self.load_and_play_video(file_path))
				self.actionRecent.addAction(self.data.qactions[file_path])
				

	def create_shortcuts(self):
		self.shortcutFull = QtGui.QShortcut(self)
		self.shortcutFull.setKey(QtGui.QKeySequence('F11'))
		self.shortcutFull.setContext(QtCore.Qt.ApplicationShortcut)
		self.shortcutFull.activated.connect(self.toggle_fullscreen)

	def connect_signals_and_slots(self):
		self.play_push_button.clicked.connect(self.play_pause_video)
		self.stop_push_button.clicked.connect(lambda: self.videoPlayer.stop())
		self.fullscreen_push_button.clicked.connect(self.toggle_fullscreen)
		self.fullscreen_push_button.setToolTip('Use "F11" Key to toggle fullscreen')
		self.actionOpen.triggered.connect(self.open_file_browser)

	def toggle_fullscreen(self):
		player_widget = self.videoPlayer.videoWidget()
		if player_widget.isFullScreen():
			player_widget.exitFullScreen()
		else:
			player_widget.enterFullScreen()


	def open_file_browser(self):
		directory_path = self.data.get_last_selected_directory()
		file_path = QtGui.QFileDialog.getOpenFileName(self, 'Select Video', directory_path)[0]
		if file_path:
			self.data.add_to_recent_files(file_path)
			self.data.set_last_selected_directory(file_path)
			self.load_and_play_video(file_path)

	def load_and_play_video(self, file_path):
		self.data.set_source(file_path)
		self.videoPlayer.load(self.data.media_obj)
		self.play_pause_video()		

	def play_pause_video(self):
		if self.videoPlayer.isPlaying():
			self.videoPlayer.pause()
			self.play_push_button.setIcon(self.data.play_pause_icons['play'])
		else:
			self.videoPlayer.play()
			self.seekSlider.setMediaObject(self.videoPlayer.mediaObject())
			self.volumeSlider.setAudioOutput(self.videoPlayer.audioOutput())
			self.play_push_button.setIcon(self.data.play_pause_icons['pause'])

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	player = VideoPlayer()
	player.show()
	app.exec_()
