# In pygame gibt es die folgenden Zeichenfunktionen um Geometrien (shapes) zu zeichen:

# pygame.draw.rect	    draw a rectangle shape:  rect(screen, color, Rect, width=0)
# pygame.draw.polygon	draw a shape with any number of sides: polygon(screen, color, pointlist, width=0)
# pygame.draw.circle	draw a circle around a point: circle(screen, color, pos, radius, width=0)
# pygame.draw.ellipse	draw a round shape inside a rectangle: ellipse(screen, color, Rect, width=0)ellipse(Surface, color, Rect, width=0)
# pygame.draw.arc	    draw a partial section of an ellipse: arc(screen, color, Rect, start_angle, stop_angle, width=1)
# pygame.draw.line	    draw a straight line segment: line(screen, color, start_pos, end_pos, width=1)
# pygame.draw.lines	    draw multiple contiguous line segments: lines(screen, color, closed, pointlist, width=1)
# pygame.draw.aaline	draw fine antialiased lines: aaline(screen, color, startpos, endpos, blend=1)
# pygame.draw.aalines	draw a connected sequence of antialiased lines: aalines(screen, color, closed, pointlist, blend=1)


import pygame
from pygame.locals import *
import math

pygame.init()

# Ein Fenster erzeugen:
screen_width=640
screen_height=480
screen=pygame.display.set_mode([screen_width,screen_height])

# Ein paar Farben definieren
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

running = True
while running:
    screen.fill(WHITE)

    pygame.draw.line(screen, GREEN, [0, 0], [50,30], 5)
    pygame.draw.lines(screen, BLACK, False, [[0, 80], [50, 90], [200, 80], [220, 30]], 5)
    pygame.draw.aaline(screen, GREEN, [0, 50],[50, 80], True)
    pygame.draw.rect(screen, BLACK, [75, 10, 50, 20], 2)
    pygame.draw.rect(screen, BLACK, [150, 10, 50, 20])
    pygame.draw.ellipse(screen, RED, [225, 10, 50, 20], 2)
    pygame.draw.ellipse(screen, RED, [300, 10, 50, 20])
    pygame.draw.polygon(screen, BLACK, [[100, 100], [0, 200], [200, 200]], 5)
    pygame.draw.arc(screen, BLACK,[210, 75, 150, 125], 0, math.pi/2, 2)
    pygame.draw.arc(screen, GREEN,[210, 75, 150, 125], math.pi/2, math.pi, 2)
    pygame.draw.arc(screen, BLUE, [210, 75, 150, 125], math.pi, 3*math.pi/2, 2)
    pygame.draw.arc(screen, RED,  [210, 75, 150, 125], 3*math.pi/2, 2*math.pi, 2)

    pygame.display.flip()

    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        running = False
    elif event.type == KEYDOWN:
        if event.key == K_ESCAPE:
            running = False
