import numpy as np

from pyproteas.cv2_wrapper import CV2Wrapper
from pyproteas.image import Image
from pyproteas.video import Video
from pyproteas.person import Person
from pyproteas.api import APIInterface


class PeopleCounting(object):

    def __init__(self, name, **kwargs):
        self.name = name
        self.kwargs = kwargs
        self.cv = CV2Wrapper()
        self.video = Video(**self.kwargs)
        self.Image = Image(**self.kwargs)

    def run(self):
        frames = self.__split_video(self.video.to_frames(), self.video.fps)
        count = np.array([])
        for arr in frames:
            _count = np.array([])
            for f in arr:
                f = self.Image.morph_close(self.Image.morph_open(self.Image.binarize(f)))
                _contours = self.cv.contours(f)
                _count = np.append(_count, self.count(_contours))
            count = np.append(count, np.round(np.average(_count), 0))
        return count

    def __split_video(self, frames, fps):
        fps = fps * self.kwargs['samplingInterval']
        trim_length = int(len(frames) % fps)
        if trim_length > 0:
            frames = frames[:-trim_length]
        return np.split(frames, len(frames)//fps)

    def count(self, contours, **kwargs):
        """
        Example: limits = [[x_0, x_1],[y_0, y_1]] where x_* are horizontal limits and y_* are vertical limits in the frame
        """
        centroids = list()
        limits = kwargs.get('limits', [])
        area_thresh = kwargs.get('frameAreaThreshold', 500)
        for c in contours:
            if self.cv.contour_area(c) > area_thresh:
                centroids.append(self.cv.centroid(c)[0])
                if len(limits) > 0 and self.cv.centroid(c)[1] not in range(limits[1]):
                    centroids.pop()
        return len(centroids)

    def track(self):
        pass


class FaceRecognition(object):

    def __init__(self, name, **kwargs):
          pass

class MotionRecognition(object):

    def __init__(self, name, **kwargs):
          pass
