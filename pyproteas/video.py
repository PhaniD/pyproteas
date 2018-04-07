import os
import numpy as np

from pyproteas.cv2_wrapper import CV2Wrapper

class Video(object):

    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.cv = CV2Wrapper()
        self.filename = os.path.join(self.kwargs['dirpath'], self.kwargs['filename'])
        self.__capture()

    def __capture(self):
        self.cap = self.cv.capture_video(self.filename)
        for i in range(10):
            print (self.cap.get(i))
        self.fps = self.cap.get(5)

    def to_frames(self):
        frames = list()
        while True:
            ret, f = self.cap.read()
            if not ret:
                break
            frames.append(f)
        self.cap.release()
        return np.array(frames)
