import json

from pyproteas.utilities import PeopleCounting, FaceRecognition


class PyProteas(object):

    def __init__(self, json_path):
        with open(json_path, 'r') as f:
            self.input = json.load(f)
        self.name = self.input['name']
        self.args = self.input['arguments']
        self.task = self.input['task']

    def execute(self):
        """
        Returns the result from task
        """
        result = getattr(self, self.task)()
        return result

    def people_counting(self):
        """
        Calls the constructor with relevant arguments
        """
        return PeopleCounting(self.name, **self.args).run()

    def face_recognition(self):
        """
        Calls the constructor with relevant arguments
        """
        return FaceRecognition(self.name, self.args).run()

    def motion_recognition(self):
        return MotionRecognition(self.name, self.args).run()
