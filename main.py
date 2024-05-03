import pygame

pygame.init()
info = pygame.display.Info()
RESOLUTION = (info.current_w, info.current_h)
screen = pygame.display.set_mode(RESOLUTION)
pygame.display.set_caption("Killing Demons With Extra Steps")
clock = pygame.time.Clock()

from assets import sprites
import ui

ui.title_screen()

running = True
while running:
    mouse_down = False
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_down = True
    screen.fill((0, 0, 0))
    ui.tick()
    pygame.display.flip()
    clock.tick(60)