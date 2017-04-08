import pygame
from pygame.locals import *
import math

pygame.init()

# Ein Fenster erzeugen:
screen_width=640
screen_height=480
screen=pygame.display.set_mode([screen_width,screen_height])

font = pygame.font.Font("Foo.ttf", 36)

running = True
while running:
    screen.fill((0,0,0))


    text = font.render("Hello World", 1, (255, 255, 255))
    textpos = text.get_rect()
    #textpos.centerx = screen.get_rect().centerx
    screen.blit(text, textpos)

    pygame.display.flip()

    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        running = False
    elif event.type == KEYDOWN:
        if event.key == K_ESCAPE:
            running = False