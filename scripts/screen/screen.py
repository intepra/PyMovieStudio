# Copyright (C) 2016 Ross D Milligan
# GNU GENERAL PUBLIC LICENSE Version 3 (full notice can be found at https://github.com/rdmilligan/PyMovieStudio)

from OpenGL.GL import *
from time import sleep
import cv2
from PIL import Image
from pygame import mixer

class Screen:

    # initialise
    def __init__(self, config_provider, disk):
        self.config_provider = config_provider
        self.disk = disk

        # texture
        self.texture_background = None

        # audio
        self.audio_log = self.disk.load_log(self.config_provider.screen_load_from)
        mixer.init()

    # initialise OpenGL
    def init_opengl(self):
        
        # texture
        glEnable(GL_TEXTURE_2D)
        self.texture_background = glGenTextures(1)

    # screen frame
    def frame(self, frame_number):

        # apply frame delay
        sleep(self.config_provider.frame_delay)

        # load frame from disk
        frame = self.disk.load_frame(self.config_provider.screen_load_from, None, frame_number, self.config_provider.frame_format)

        # ensure frame loaded from disk
        if frame is None:
            return False

        # convert frame to OpenGL texture format
        bg_image = cv2.flip(frame, 0)
        bg_image = Image.fromarray(bg_image)     
        ix = bg_image.size[0]
        iy = bg_image.size[1]
        bg_image = bg_image.tobytes('raw', 'BGRX', 0, -1)
 
        # create background texture
        glBindTexture(GL_TEXTURE_2D, self.texture_background)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexImage2D(GL_TEXTURE_2D, 0, 3, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, bg_image)
        
        # draw background
        glBindTexture(GL_TEXTURE_2D, self.texture_background)
        glPushMatrix()
        glTranslatef(0.0,0.0,-10.0)
        glBegin(GL_QUADS)
        glTexCoord2f(0.0, 1.0); glVertex3f(-4.0, -3.0, 0.0)
        glTexCoord2f(1.0, 1.0); glVertex3f( 4.0, -3.0, 0.0)
        glTexCoord2f(1.0, 0.0); glVertex3f( 4.0,  3.0, 0.0)
        glTexCoord2f(0.0, 0.0); glVertex3f(-4.0,  3.0, 0.0)
        glEnd( )
        glPopMatrix()

        # handle audio
        self._handle_audio(frame_number)

        return True

    # handle audio
    def _handle_audio(self, frame_number):

        # loop audio log
        for item in self.audio_log:

            # extract frame number and sound file 
            item_parts = item.split(',')
            item_frame_number = int(item_parts[0])
            item_sound_file = item_parts[1].replace('\n', '')

            # play sound if frames match
            if item_frame_number == frame_number:
                mixer.Sound("{}{}".format(self.config_provider.screen_load_from, item_sound_file)).play()
                break
        




