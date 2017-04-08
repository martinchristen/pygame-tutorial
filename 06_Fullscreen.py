import pygame
from pygame.locals import *
import platform

###############################################
# Fix bug with Fullscreen in Windows:
if platform.system() == "Windows":
    import ctypes
    ctypes.windll.user32.SetProcessDPIAware()
###############################################

pygame.init()
display = pygame.display.Info()

screen_width = display.current_w
screen_height = display.current_h

print(screen_width, screen_height)

screen=pygame.display.set_mode([screen_width,screen_height], pygame.FULLSCREEN, 32)

# Hintergrundfarbe definieren
red = 0
green = 0
blue = 0

clock = pygame.time.Clock()
running = True
velocity = [4,2]


sprite = pygame.sprite.Sprite()               # create sprite
sprite.image = pygame.image.load("ball.png")  # load ball image
sprite.rect = sprite.image.get_rect()         # use image extent values
sprite.rect.topleft = (100,100)               # set position of top left corner

while running:
    screen.fill((0, 0, 0))   # fill background

    screen.blit(sprite.image, sprite.rect)

    pygame.display.flip()

    clock.tick(60)  # limit to 60 FPS
    sprite.rect.topleft = (sprite.rect.topleft[0]+velocity[0],
                           sprite.rect.topleft[1]+velocity[1])


    if sprite.rect.topleft[0]+sprite.rect.width >= screen_width and velocity[0]>0:
        velocity[0] = -velocity[0]
    if sprite.rect.topleft[0] <= 0 and velocity[0]<0:
        velocity[0] = -velocity[0]

    if sprite.rect.topleft[1]+sprite.rect.height >= screen_height and velocity[1]>0:
        velocity[1] = -velocity[1]
    if sprite.rect.topleft[1] <= 0 and velocity[1]<0:
        velocity[1] = -velocity[1]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False