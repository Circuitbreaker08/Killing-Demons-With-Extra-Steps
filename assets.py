import pygame
import json
import os
import sys

RESOLUTION = getattr(sys.modules["__main__"], "RESOLUTION")
scale = (RESOLUTION[0]/1920, RESOLUTION[1]/1080)

pygame.init()
root = os.getcwd()
os.chdir("assets/sprites")

sprites = {}
items = {}

for directory in os.listdir():
    sprites.update({directory: {}})
    os.chdir(os.path.join(root, "assets/sprites", directory))
    for file in os.listdir():
        image = pygame.image.load(file).convert_alpha()
        sprites[directory].update({file: pygame.transform.scale(image, (image.get_width() * scale[0], image.get_height() * scale[1]))})

os.chdir(os.path.join(root, "assets/items"))

for file in os.listdir():
    with open(file) as f:
        items.update({file: json.loads(f.read())})