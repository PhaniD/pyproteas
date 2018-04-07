import cv2
import numpy as np

class CV2Wrapper(object):
    """
    Wrappers around OpenCV
    """

    # Capture Video

    def capture_video(self, filename, **kwargs):
        """
        Args:
            filename (str): Name of the video file
        Kwargs:
            additional arguments to CV2 Video Capture

        Returns:
             Frames from video
        """
        return cv2.VideoCapture(filename)

    # Read Images

    def load_image(self, filename, **kwargs):
        """
        Args:
            filename (str): Name of the image file
        Kwargs:
            additional arguments to CV2 Image load utility

        Returns:
             Method to read images
        """
        return cv2.imread(filename, kwargs)


    # Operations on Frames
    def contours(self, frame, **kwargs):
        retr_mode = kwargs.get('retrieval_mode', 'RETR_EXTERNAL')
        contour_approx = kwargs.get('contour_approximation', 'CHAIN_APPROX_SIMPLE')
        _, _contours, _ = cv2.findContours(frame,
                                           getattr(cv2, retr_mode),
                                           getattr(cv2, contour_approx))
        return _contours

    def contour_area(self, contour):
        return cv2.contourArea(contour)

    def centroid(self, contour):
        M = cv2.moments(contour)
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])
        return cx, cy

    def square_kernel(self, dim=(3,3)):
        return np.ones(dim, np.uint8)

    def struct_element(self, op='MORPH_RECT', dim=(5,5)):
        morph_op = getattr(cv2, op)
        return cv2.getStructuringElement(morph_op,dim)

    def background_subtractor(self, **kwargs):
        shadows = kwargs.get('detectShadows', True)
        _method = "".join(['create', kwargs.get('background_subtractor', 'BackgroundSubtractorMOG2')])
        return getattr(cv2, _method)(detectShadows=shadows)

    def binary_threshold(self, src, threshold=200, maxValue=255, thresholdType='THRESH_BINARY'):
        thresh_value, bin_image = cv2.threshold(src, threshold, maxValue, getattr(cv2,thresholdType))
        return bin_image

    def morph(self, src, op='MORPH_OPEN', kernel=None):
        if kernel is None:
            kernel = self.square_kernel()
        return cv2.morphologyEx(src, getattr(cv2, op), kernel)

