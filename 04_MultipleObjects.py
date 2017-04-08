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

objects = []
num_objects = 100

for i in range(0,num_objects):
    position = [random.randint(0,screen_width),random.randint(0,screen_width)]
    velocity = [random.randint(1,8), random.randint(1,8)]
    radius = random.randint(2,10)
    color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    objects += [[position, velocity, radius, color]]


running = True
while running:
    screen.fill((0, 0, 0))   # Hintergrund löschen

    for i in range(0,num_objects):
        position = objects[i][0]
        velocity = objects[i][1]
        radius = objects[i][2]
        color = objects[i][3]
        pygame.draw.circle(screen, color, position, radius)

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


    pygame.display.flip()
    clock.tick(60)  # Limitiere auf 60 Bilder pro Sekunde

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False