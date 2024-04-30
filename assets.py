import pygame
import json
import os
import sys

root = os.getcwd()
os.chdir("assets/sprites")

sprites = {}
items = {}

for directory in os.listdir():
    sprites.update({directory: {}})
    os.chdir(os.path.join(root, "assets/sprites", directory))
    for file in os.listdir():
        sprites[directory].update({file: pygame.transform.scale(pygame.image.load(file).convert_alpha())})

os.chdir(os.path.join(root, "assets/items"))

for file in os.listdir():
    with open(file) as f:
        items.update({file: json.loads(f.read())})