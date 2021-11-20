""" tkVideo: Python module for playing videos (without sound) inside tkinter Label widget using Pillow and imageio

Copyright © 2020 Xenofon Konitsas <konitsasx@gmail.com>
Released under the terms of the MIT license (https://opensource.org/licenses/MIT) as described in LICENSE.md

"""

try:
    import Tkinter as tk  # for Python2 (although it has already reached EOL)
except ImportError:
    import tkinter as tk  # for Python3
import threading
from time import perf_counter, sleep
import imageio
from PIL import Image, ImageTk

class tkvideo():
    """ 
        Main class of tkVideo. Handles loading and playing 
        the video inside the selected label.
        
        :keyword path: 
            Path of video file
        :keyword label: 
            Name of label that will house the player
        :param loop:
            If equal to 0, the video only plays once, 
            if not it plays in an infinite loop (default 0)
        :param size:
            Changes the video's dimensions (2-tuple, 
            default is 640x360) 
        :param hz:
            Sets the video's frame rate (float, 
            default 0 is unchecked) 
    
    """
    def __init__(self, path, label, loop = 0, size = (640,360), hz = 0):
        self.path = path
        self.label = label
        self.loop = loop
        self.size = size
        self.hz = hz
    
    def load(self, path, label, loop, hz):
        """
            Loads the video's frames recursively onto the selected label widget's image parameter.
            Loop parameter controls whether the function will run in an infinite loop
            or once.
        """
        frame_data = imageio.get_reader(path)

        if hz > 0:
            frame_duration = float(1 / hz)
        else:
            frame_duration = float(0)

        if loop == 1:
            while True:
                before = perf_counter()
                for image in frame_data.iter_data():
                    frame_image = ImageTk.PhotoImage(Image.fromarray(image).resize(self.size))
                    label.config(image=frame_image)
                    label.image = frame_image

                    diff = frame_duration + before
                    after = perf_counter()
                    diff = diff - after 
                    if diff > 0:
                        sleep(diff)
                    before = perf_counter()
        else:
            before = perf_counter()
            for image in frame_data.iter_data():
                    frame_image = ImageTk.PhotoImage(Image.fromarray(image).resize(self.size))
                    label.config(image=frame_image)
                    label.image = frame_image

                    diff = frame_duration + before
                    after = perf_counter()
                    diff = diff - after 
                    if diff > 0:
                        sleep(diff)
                    before = perf_counter()

    def play(self):
        """
            Creates and starts a thread as a daemon that plays the video by rapidly going through
            the video's frames.
        """
        thread = threading.Thread(target=self.load, args=(self.path, self.label, self.loop, self.hz))
        thread.daemon = 1
        thread.start()
