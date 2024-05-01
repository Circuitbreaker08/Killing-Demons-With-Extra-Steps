import pygame
import sys

from assets import sprites

RESOLUTION = getattr(sys.modules["__main__"], "RESOLUTION")
screen: pygame.Surface = getattr(sys.modules["__main__"], "screen")
mouse = (0, 0)
mouse_down = True

class Image():
    def __init__(self, position: tuple[int, int], image):
        self.position = position
        self.image = image

    def tick(self):
        screen.blit(self.image, self.position)

class Button():
    def __init__(self, position: tuple[int, int], size: tuple[int, int], image, event: function):
        self.position = position
        self.size = size
        self.image = image
        self.event = event

    def tick(self):
        screen.blit(self.image, self.position)
        if mouse[0] > self.position[0] and mouse[0] < self.size[1] and mouse[1] > self.position[0] and mouse[1] < self.position[1] and mouse_down:
            self.event()

elements: list[Image, Button] = []

def tick():
    mouse = pygame.mouse.get_pos()
    mouse_down = getattr(sys.modules["__main__"], "mouse_down")
    for element in elements:
        element.tick()

def title_screen():
    def debug():
        print("Click!")
    global elements
    elements = [
        Image((39 * RESOLUTION[0]/320, RESOLUTION[1]/10), sprites["ui"]["logo.png"]),
        Button((0, 0), (100, 100), sprites["ui"]["start_game.png"], debug)
    ]