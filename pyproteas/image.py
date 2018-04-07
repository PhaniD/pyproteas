import os

from pyproteas.cv2_wrapper import CV2Wrapper


class Image(object):

    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.cv = CV2Wrapper()
        self.mask = self.cv.background_subtractor(detectShadows=True)

    def apply_mask(self, frame):
        if self.kwargs.get('image'):
            frame = os.path.join(self.kwargs['dirpath'], self.kwargs['filename'])
        return self.mask.apply(frame)

    def binarize(self, frame, **kwargs):
        bin_frame = self.cv.binary_threshold(self.apply_mask(frame))
        return bin_frame

    def morph_open(self, frame, **kwargs):
        kernel = self.cv.square_kernel(dim=[5,5])
        morphed_frame = self.cv.morph(frame, op='MORPH_OPEN', kernel=kernel)
        return morphed_frame

    def morph_close(self, frame, **kwargs):
        kernel = self.cv.square_kernel(dim=[10,10])
        morphed_frame = self.cv.morph(frame, op='MORPH_CLOSE', kernel=kernel)
        return morphed_frame

    def erode(self):
        pass

    def dilate(self):
        pass
