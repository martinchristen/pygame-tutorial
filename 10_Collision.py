import pygame
from pygame.locals import *
import random

pygame.init()

# Ein Fenster erzeugen:
w = 640
h = 480
screen = pygame.display.set_mode([w,h])

clock = pygame.time.Clock()

running = True
left = 0
right = 1
xpos = w/2-32
ypos = 4*h/5-16

xball = 100
yball = 100
dxball = 2
dyball = 2

ballcolor = (255,0,0)
gameover = False

score = 0

font = pygame.font.Font("foo.ttf", 64)
fontsmall = pygame.font.Font("foo.ttf", 32)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left = 2
                right = 0
            elif event.key == pygame.K_RIGHT:
                left = 0
                right = 2

    screen.fill([0,0,0])  # Schwarzer Hintergrund

    xpos += right
    xpos -= left
    if xpos > w - 64:
        xpos = w-64
    if xpos < 0:
        xpos = 0

    xball += dxball
    yball += dyball

    if xball >= w - 16:
        dxball = -dxball
    if yball >= h - 16:
        dyball = 0 #GAME OVER!
        dxball = 0
        gameover = True
    if xball <= 0:
        dxball = -dxball
    if yball <= 0:
        dyball = -dyball
        score += 1
        pass

    if gameover:
        text = font.render("GAME OVER", 1, (127, 127, 255))
        textpos = text.get_rect()
        textpos.centerx = screen.get_rect().centerx
        textpos.centery = screen.get_rect().centery
        screen.blit(text, textpos)

    scoretext = fontsmall.render("Score: " + str(score), 1, (127,255,127))
    screen.blit(scoretext, (0,0))


    # ball hits paddle ?
    if xball+16 >= xpos and xball <=xpos+64 and yball+16>=ypos and yball<=ypos+32:
        dyball = -dyball
        ballcolor = (0,255,0)
    else:
        ballcolor = (255,0,0)

    # draw the paddle
    pygame.draw.rect(screen, (255,255,255), [xpos, ypos, 64, 32])

    #  draw the ball
    pygame.draw.ellipse(screen, ballcolor , [xball, yball, 16, 16])

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
