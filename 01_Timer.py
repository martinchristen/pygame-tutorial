import pygame
from pygame.locals import *
import random

pygame.init()

# Ein Fenster erzeugen:
screen_width=640
screen_height=480
screen=pygame.display.set_mode([screen_width,screen_height])

clock = pygame.time.Clock()

running = True
while running:
    screen.fill((random.randint(0,255), random.randint(0,255), random.randint(0,255)))
    pygame.display.flip()

    clock.tick(1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False