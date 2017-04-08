####################################
# WARNING: THIS PROGRAM WILL HANG!!
####################################


import pygame
#from pygame.locals import *

pygame.init()
screen=pygame.display.set_mode([640,480])


# Hintergrundfarbe definieren
color = (255, 0, 0)


while True:
    screen.fill(color)
    pygame.display.update()

pygame.quit()
