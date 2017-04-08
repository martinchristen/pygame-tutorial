import pygame
from pygame.locals import *

# pygame initialisieren
pygame.init()

# Ein Fenster erzeugen:
screen_width=640
screen_height=480
screen=pygame.display.set_mode([screen_width,screen_height])


# Ein Sprite erzeugen:
sprite = pygame.sprite.Sprite()               # create sprite
sprite.image = pygame.image.load("ball.png")  # load ball image
sprite.rect = sprite.image.get_rect()         # use image extent values
sprite.rect.topleft = (100,100)               # set position of top left corner


clock = pygame.time.Clock()
running = True

while running:
    screen.fill((255, 255, 255))   # hintergrund mit weiss füllen

    screen.blit(sprite.image, sprite.rect)  # Sprite zeichnen

    pygame.display.flip()

    clock.tick(60)  # Auf 60 bilder pro Sekunde einschränken

    # Quit / ESC Taste überprüfen...
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == pygame.MOUSEMOTION:
            # event.pos ist ein Tupel mit der Maus-Position
            #  sprite.rect.topleft = event.pos


            # Wenn wir die Mitte wollen:
            w = sprite.rect.size[0]
            h = sprite.rect.size[1]
            sprite.rect.topleft = (event.pos[0] - w/2, event.pos[1] - h/2)



