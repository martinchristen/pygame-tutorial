import pygame
from pygame.locals import *


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
velocity = [4,2]


#sprite = pygame.Sprite()               # create sprite
image = pygame.image.load("ball.png").convert()  # load ball image
rect = image.get_rect()         # use image extent values
rect.topleft = (100,100)               # set position of top left corner




while running:
    screen.fill((0, 0, 0))   # fill background

    screen.blit(image, (100,100))

    pygame.display.flip()

    clock.tick(60)  # limit to 60 FPS
    rect.topleft = (rect.topleft[0]+velocity[0],
                           rect.topleft[1]+velocity[1])


    if rect.topleft[0]+rect.width >= screen_width and velocity[0]>0:
        velocity[0] = -velocity[0]
    if rect.topleft[0] <= 0 and velocity[0]<0:
        velocity[0] = -velocity[0]

    if rect.topleft[1]+rect.height >= screen_height and velocity[1]>0:
        velocity[1] = -velocity[1]
    if rect.topleft[1] <= 0 and velocity[1]<0:
        velocity[1] = -velocity[1]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False