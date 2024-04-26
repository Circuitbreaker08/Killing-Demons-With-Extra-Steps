import sys

RESOLUTION = getattr(sys.modules["__main__"], "RESOLUTION")
screen = getattr(sys.modules["__main__"], "screen")

class Image():
    def __init__(self, position: tuple[int, int], image):
        self.position = position
        self.image = image
