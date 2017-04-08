import pygame
from pygame.locals import *
import random

pygame.init()

# Ein Fenster erzeugen:
screen_width=640
screen_height=480
screen=pygame.display.set_mode([screen_width,screen_height])

# Hintergrundfarbe definieren
red = 0
green = 0
blue = 0

clock = pygame.time.Clock()
running = True
position = [100,100]
velocity = [4,2]
radius = 30

while running:
    screen.fill((0, 0, 0))   # Hintergrund löschen

    pygame.draw.circle(screen, (0,255,0), position, radius)

    pygame.display.flip()

    clock.tick(60)  # Limitiere auf 60 Bilder pro Sekunde
    position[0] += velocity[0]
    position[1] += velocity[1]

    if position[0]+radius >= screen_width and velocity[0]>0:
        velocity[0] = -velocity[0]
    if position[0]-radius <= 0 and velocity[0]<0:
        velocity[0] = -velocity[0]

    if position[1]+radius >= screen_height and velocity[1]>0:
        velocity[1] = -velocity[1]
    if position[1]-radius <= 0 and velocity[1]<0:
        velocity[1] = -velocity[1]



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False