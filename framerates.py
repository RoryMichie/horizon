import time


class framerate:
    def __init__(self, fps):
        self.last = time.time()
        self.fps = fps

    def align(self):
        e = time.time()
