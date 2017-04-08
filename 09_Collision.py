#################################################################
# Dies ist unser erstes richtiges Game:
# Es werden Raketen  geschossen und man muss dem Ball ausweichen
# Bei Kollision ist das Spiel verloren!
#################################################################

import pygame
from pygame.locals import *
import random

# pygame initialisieren
pygame.init()

# Ein Fenster erzeugen:
screen_width=640
screen_height=480
screen=pygame.display.set_mode([screen_width,screen_height])

clock = pygame.time.Clock()
running = True
cnt = 0

rockets = []

while running:
    screen.fill((255, 255, 255))   # hintergrund mit weiss füllen

    # Raketen-Sprite(s) zeichnen
    for rocket in rockets:
        screen.blit(rocket.image, rocket.rect)
        rocket.rect.topleft = (rocket.rect.topleft[0], rocket.rect.topleft[1] + 1)

    pygame.display.flip()

    clock.tick(60)  # Auf 60 Bilder pro Sekunde einschränken
    cnt += 1        # counter erhöhen, dies geschieht bei jedem Frame (also 60 mal pro Sekunde)

    ###################################################################################################################
    if cnt>30: # Alle 1/2 Sekunde eine neue Rakete...
        cnt = 0
        rocketsprite = pygame.sprite.Sprite()               # create sprite
        rocketsprite.image = pygame.image.load("rocket.png")  # load ball image
        rocketsprite.rect = rocketsprite.image.get_rect()         # use image extent values
        rocketsprite.rect.topleft = (random.randint(10, screen_width-10),0)
        rockets.append(rocketsprite)

    ####################################################################################################################
    # Raketen ausserhalb Bildschirm zerstören
    newrockets = []
    for rocket in rockets:
        if rocket.rect.topleft[1]<=screen_height:
            newrockets.append(rocket)

    rockets = newrockets   # Liste mit neuer überschreiben
                           # Entfernte sind nicht mehr in der Liste!
    ####################################################################################################################

    # Quit / ESC Taste überprüfen...
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False



