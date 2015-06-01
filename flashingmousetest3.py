# Nick Kasten
# flashingmousetest3.py
# 1/17/2015
# Flashing Crosshairs that follow mouse movement

import pygame

x = y = 0
running = 1
width = 640
height = 400
screen = pygame.display.set_mode((width,height))
blueVal = 0
blueDir = 1
bgColor = 0, 0, 0

while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = 0
    elif event.type == pygame.MOUSEMOTION:
        x, y = event.pos

    screen.fill(bgColor)
    pygame.draw.line(screen, (0, 0, blueVal), (x, 0), (x, 399))
    pygame.draw.line(screen, (0, 0, blueVal), (0, y), (639, y))
    blueVal += blueDir
    if blueVal == 255 or blueVal == 0: blueDir *= -1
    pygame.display.flip()
pygame.quit()

