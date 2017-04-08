import pygame
from pygame.locals import *
import random

pygame.init()

# Ein Fenster erzeugen:
width=640
height=480

screen = pygame.display.set_mode((width, height))


# Hintergrundfarbe definieren
color = (0, 0, 0)

running = True
while running:
    for event in pygame.event.get():
        print(event)   # see: http://www.pygame.org/docs/ref/event.html
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                print("Pfeil nach unten gedrückt")
            elif event.key == pygame.K_0:
                print("Taste 0 gedrückt!")

        if event.type == pygame.MOUSEMOTION:
            xMaus = event.pos[0]
            yMaus = event.pos[1]
            buttons = event.buttons

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            button = event.button



pygame.quit()
