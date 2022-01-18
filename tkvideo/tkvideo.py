"""Play moviepy video clips with tkiner"""
import threading
from time import perf_counter, sleep
from PIL import Image, ImageTk


class TkVideo:
    def __init__(self, clip, label, loop=0, size=(640, 360), hz=0):
        """The main class

        Args:
            clip (moviepy.editor.VideoFileClip): The clip to use
            label (Test): The file label
            loop (int, optional): Whether to loop the clip. Defaults to 0.
            size (tuple, optional): The dimensions of the clip. Defaults to (640, 360).
            hz (int, optional): The framerate of the clip. Defaults to 0.
        """
        self.clip = clip
        self.label = label
        self.loop = loop
        self.size = size
        self.hz = hz

    def load(self):
        """Loads the video's frames recursively onto the selected label widget's image parameter.
        Loop parameter controls whether the function will run in an infinite loop or once.
        """
        frames = self.clip.iter_frames()

        if self.hz:
            frame_duration = float(1 / self.hz)
        else:
            frame_duration = float(0)

        if self.loop:
            while True:
                before = perf_counter()
                for image in frames:
                    frame_image = ImageTk.PhotoImage(
                        Image.fromarray(image).resize(self.size)
                    )
                    self.label.config(image=frame_image)
                    self.label.image = frame_image

                    diff = frame_duration + before
                    after = perf_counter()
                    diff = diff - after
                    if diff > 0:
                        sleep(diff)
                    before = perf_counter()
        else:
            before = perf_counter()
            for image in frames:
                frame_image = ImageTk.PhotoImage(
                    Image.fromarray(image).resize(self.size)
                )
                self.label.config(image=frame_image)
                self.label.image = frame_image

                diff = frame_duration + before
                after = perf_counter()
                diff = diff - after
                if diff > 0:
                    sleep(diff)
                before = perf_counter()

    def play(self):
        """Creates and starts a thread as a daemon that plays the video by rapidly going through
        the video's frames.
        """
        thread = threading.Thread(target=self.load)
        thread.daemon = True
        thread.start()
