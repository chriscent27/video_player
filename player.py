""" This module creates the video player data and the respective UI to represent it.
"""
""" This module contains the player data and player UI.
"""
import os
import sys
from ui import player_Ui
from PySide import QtGui, QtCore
from PySide.phonon import Phonon
from full_screen_widget import FullScreenWidget

class PlayerData(object):
    """ This class stores and manipulates all the player related data.
    """
    def __init__(self):
        """ The initialization method of the class.
        """
        self.media_source_obj = None
        self.phonon_media_obj = None
        self.qactions = {}
        self.recent_files = {}
        self.settings = QtCore.QSettings()
        self.play_pause_icons = {
            'play': None,
            'pause': None,  
        }
        self.file_path = None
        self.last_played = None
        self.seekOn = False

        self.create_play_pause_icons()
        self.load_recent_files()
        self.fetch_last_played_file_path()

    def set_phonon_media_obj(self, player):
        """ Sets the media object attribute from the player.

            Args:
                player (obj): The phonon media player object.
        """
        self.phonon_media_obj = player.mediaObject()

    def create_play_pause_icons(self):
        """ Creates the icon objects for play - pause button.
        
            The play-pause button needs to swap between the play and pause icons.
            This can be done fast using the generated icon objects in the class.

        """
        self.play_pause_icons['play'] = QtGui.QIcon()
        self.play_pause_icons['play'].addPixmap(QtGui.QPixmap("ui/icons/play_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play_pause_icons['pause'] = QtGui.QIcon()
        self.play_pause_icons['pause'].addPixmap(QtGui.QPixmap("ui/icons/pause_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

    def load_recent_files(self):
        """ Gets the recent files list from Qsettings and sets the variable.
        """
        selected_files = self.settings.value('selected_files')
        if selected_files.__class__ == dict:
            self.recent_files = selected_files
        else:
            self.recent_files = dict()
        
    def add_to_recent_files(self, file_path):
        """ Once the file is opened, the file path is added to the dictionary of recent files.

            The recent files dictionary is then saved in the QSettings.

            Args:
                file_path (str): The file path of the video that is being played.
        """
        self.recent_files[file_path] = None
        if len(self.recent_files) > 10:
            self.recent_files.popitem()

    def save_recent_files(self):
        """ Saves the recent files dictionary in the QSettings.
        """
        self.settings.setValue('selected_files', self.recent_files)

    def set_last_played_file_path(self, file_path):
        """ Returns the last selected directory path.
        """
        self.last_played = file_path

    def fetch_last_played_file_path(self):
        """ Returns the last selected directory path.
        """
        self.last_played = self.settings.value("last played")

    def save_last_played_file_path(self, file_path):
        """ Saves the directory path of the file opened in QSettings.
        """
        self.settings.setValue("last played", file_path)

    def get_last_selected_directory(self):
        """ Gets the directory path of the last selected video.
        """
        if self.last_played:
            return os.path.dirname(self.last_played)

    def set_source(self, file_path):
        """ Creates a media source object from the filepath provided.

            Args:
                file_path (str): The file path of the media object.
        """
        self.media_source_obj = Phonon.MediaSource(file_path)

    def get_last_played_time(self, file_path):
        """ Gets the time value of the video that was played last time.

            Args:
                file_path (str): The file path of the video that was played last time.
        """
        return self.recent_files.get(file_path)

    def update_current_playtime(self):
        """ Before closing the player, the player data is saved.

            This is done so that when the player is opened next time, the 
            last player state can be achieved again.

        """
        if self.phonon_media_obj:
            current_play_time = self.phonon_media_obj.currentTime()
            file_path = self.phonon_media_obj.currentSource().fileName()
            self.recent_files[file_path] = current_play_time
            self.save_last_played_file_path(file_path)


class VideoPlayer(player_Ui.Ui_MainWindow, QtGui.QMainWindow):
    """ This class handles the player functionality and user interface.
    """
    def __init__(self):
        """ The class initialization method.
        """
        super(VideoPlayer, self).__init__()
        self.setupUi(self)
        self.full_screen_widget = None
        self.data = PlayerData()
        self.data.set_phonon_media_obj(self.videoPlayer)
        self.create_shortcuts()
        self.connect_signals_and_slots()
        self.populate_recent_files_menu()
        self.seekSlider.setMediaObject(self.videoPlayer.mediaObject())
        self.volumeSlider.setAudioOutput(self.videoPlayer.audioOutput())
        self.load_last_played()


    def load_last_played(self):
        """ Loads the last played video when the player starts.
        """
        if self.data.last_played:
            self.load_and_play_video(self.data.last_played)

    def populate_recent_files_menu(self):
        """ Dynamically creates the recent files menu actions.
        """
        file_paths = self.data.recent_files
        if file_paths.__class__ == dict:
            for file_path in file_paths.keys():
                if file_path:
                    file_name = os.path.basename(file_path)
                    action = self.menuRecent.addAction(file_name)
                    action.triggered[()].connect(
                        lambda x = file_path: self.load_and_play_video(x))

    def create_shortcuts(self):
        """ All the player shortcuts are defined here.
        """
        self.shortcutFullscreen = QtGui.QShortcut(self)
        self.shortcutFullscreen.setKey(QtGui.QKeySequence('F11'))
        self.shortcutFullscreen.setContext(QtCore.Qt.ApplicationShortcut)
        self.shortcutFullscreen.activated.connect(self.toggle_fullscreen)

        self.shortcutPlayPause = QtGui.QShortcut(self)
        self.shortcutPlayPause.setKey(QtGui.QKeySequence('SPACE'))
        self.shortcutPlayPause.setContext(QtCore.Qt.ApplicationShortcut)
        self.shortcutPlayPause.activated.connect(self.play_pause_video)

    def connect_signals_and_slots(self):
        """ The signals and slots connections, and tooltips are defined here.
        """
        self.open_file_button.clicked.connect(self.open_file_browser)
        self.actionOpen.triggered.connect(self.open_file_browser)
        
        self.play_push_button.clicked.connect(self.play_pause_video)
        self.play_push_button.setToolTip('Use "Space" Key to toggle Play-Pause')
        self.stop_push_button.clicked.connect(lambda: self.videoPlayer.stop())
        
        self.fullscreen_push_button.clicked.connect(self.toggle_fullscreen)
        self.fullscreen_push_button.setToolTip('Use "F11" Key to toggle fullscreen')
        
        # connects when the phonon media obj becomes seekable.
        self.data.phonon_media_obj.seekableChanged.connect(self.seek_and_play)

    def toggle_fullscreen(self):
        """ This method handles the toggling of fullscreen funtionality.
        """
        if self.full_screen_widget:
            # This denotes the exit from fullsceen.
            widgets = self.full_screen_widget.return_widgets()

            # The widgets that are returned from the fullscreen widget is set.
            self.videoPlayer = widgets[0]
            self.player_widget = widgets[1]
            self.seekSlider = widgets[2]
            self.fullscreen_push_button = widgets[3]
            self.verticalLayout.insertWidget(0, self.player_widget)
            self.verticalLayout.insertWidget(1, self.seekSlider)
            self.horizontalLayout.addWidget(self.fullscreen_push_button)
            self.full_screen_widget.exit_fullscreen()
            self.full_screen_widget = None

        else:
            # Denotes the fullscreen mode. The widgets are passed to fullscreen UI.
            self.full_screen_widget = FullScreenWidget(
                self.videoPlayer,
                self.seekSlider,
                self.fullscreen_push_button,
            )
            self.full_screen_widget.go_full_screen()

    def open_file_browser(self):
        """ The file browser is opened and the video is played accordingly.

            The file browser is opened, the user selection is fetched and the
            video is loaded and played in the player.
        """
        directory_path = self.data.get_last_selected_directory()
        file_path = QtGui.QFileDialog.getOpenFileName(self, 'Select Video', directory_path)[0]
        if file_path:
            # The selection is saved for later use.
            self.data.add_to_recent_files(file_path)
            self.data.set_last_played_file_path(file_path)

            # The file is loaded and played.
            self.load_and_play_video(file_path)

    def load_and_play_video(self, file_path):
        """ Creates media souce object from filepath and loads in player.
        """
        if self.data.file_path:
            self.data.update_current_playtime()
        self.data.seekOn = True
        self.data.set_source(file_path)
        self.data.file_path = file_path
        self.videoPlayer.load(self.data.media_source_obj)
        self.play_pause_video()

    def seek_and_play(self):
        """ Once the media object is seekable, the seek value is changed.

            This function is called when a new file is loaded, once the file is
            loaded there is a delay for the file to become seekable. 

            Once the file is made seekable this method is called to seek the video
            to the last played time value.
        """
        if self.data.seekOn and self.data.phonon_media_obj.isSeekable():
            last_played = self.data.get_last_played_time(self.data.file_path)
            if last_played:
                self.videoPlayer.seek(last_played)

            self.data.seekOn = False
    
    def play_pause_video(self):
        """ This method toggles the play pause functionality using one button.
        """
        if self.videoPlayer.isPlaying():
            self.videoPlayer.pause()
            self.play_push_button.setIcon(self.data.play_pause_icons['play'])
        else:
            self.videoPlayer.play()
            self.play_push_button.setIcon(self.data.play_pause_icons['pause'])

    def closeEvent(self, event):
        """ This event is called when the player is closed.

            Before the player is closed, the player current state is 
            saved so that it can be retained when you open it the next time.
        """
        self.data.update_current_playtime()
        self.data.save_recent_files()



if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    player = VideoPlayer()
    player.show()
    app.exec_()
