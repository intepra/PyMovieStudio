# Copyright (C) 2016 Ross D Milligan
# GNU GENERAL PUBLIC LICENSE Version 3 (full notice can be found at https://github.com/rdmilligan/PyMovieStudio)

import ConfigParser

class ConfigProvider:

    def __init__(self):
        self.config = ConfigParser.ConfigParser()
        self.config.read('appsettings.ini')

    @property
    def record_enabled(self):
        return self.config.getboolean('Record', 'Enabled')

    @property
    def record_save_to(self):
        return self.config.get('Record', 'SaveTo')

    @property
    def record_show_frames(self):
        return self.config.getboolean('Record', 'ShowFrames')

    @property
    def edit_enabled(self):
        return self.config.getboolean('Edit', 'Enabled')

    @property
    def edit_load_from(self):
        return self.config.get('Edit', 'LoadFrom')

    @property
    def edit_save_to(self):
        return self.config.get('Edit', 'SaveTo')

    @property
    def edit_show_frame(self):
        return self.config.getboolean('Edit', 'ShowFrame')

    @property
    def edit_camera_names(self):
        return self.config.get('Edit', 'CameraNames')

    @property
    def effects_enabled(self):
        return self.config.getboolean('Effects', 'Enabled')

    @property
    def effects_load_from(self):
        return self.config.get('Effects', 'LoadFrom')

    @property
    def effects_save_to(self):
        return self.config.get('Effects', 'SaveTo')

    @property
    def effects_show_frame(self):
        return self.config.getboolean('Effects', 'ShowFrame')

    @property
    def audio_enabled(self):
        return self.config.getboolean('Audio', 'Enabled')

    @property
    def audio_load_from(self):
        return self.config.get('Audio', 'LoadFrom')

    @property
    def audio_save_to(self):
        return self.config.get('Audio', 'SaveTo')

    @property
    def audio_show_frame(self):
        return self.config.getboolean('Audio', 'ShowFrame')

    @property
    def audio_sound_file(self):
        return self.config.get('Audio', 'SoundFile')

    @property
    def audio_sound_delay(self):
        return self.config.getint('Audio', 'SoundDelay')

    @property
    def screen_enabled(self):
        return self.config.getboolean('Screen', 'Enabled')

    @property
    def screen_load_from(self):
        return self.config.get('Screen', 'LoadFrom')

    @property
    def number_of_cameras(self):
        return self.config.getint('Shared', 'NumberOfCameras')

    @property
    def frame_delay(self):
        return self.config.getfloat('Shared', 'FrameDelay')

    @property
    def frame_format(self):
        return self.config.get('Shared', 'FrameFormat')
