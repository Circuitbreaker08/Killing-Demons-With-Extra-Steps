import pygame

pygame.init()
info = pygame.display.Info()
RESOLUTION = (info.current_w, info.current_h)
screen = pygame.display.set_mode(RESOLUTION)
pygame.display.set_caption("Killing Demons With Extra Steps")
clock = pygame.time.Clock()

from assets import sprites
import ui

while True:
    pygame.display.flip()
    clock.tick(60)