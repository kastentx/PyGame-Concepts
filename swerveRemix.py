# Nick Kasten
# swerveRemix.py
# 1/19/2015
# testing swerve motion of an object

import pygame

# colors
GREEN = ( 0, 255, 0 )
WHITE = ( 255, 255, 255 )
BLACK = ( 0, 0, 0 )

# window dimensions
displayWidth = 640
displayHeight = 400
gameDisplay = pygame.display.set_mode( ( displayWidth, ( displayHeight ) ) )
gameDisplay.fill( WHITE )
clock = pygame.time.Clock()
running = True

def car(x, y):
    pygame.draw.rect( gameDisplay, GREEN, ( x, y, 50, 50 ), 0 )

carStartX = displayWidth * .45
carStartY = displayHeight * .8
carCurrentX = carStartX
xChange = 0
goingHome = False

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                xChange = -10
            if event.key == pygame.K_RIGHT:
                xChange = 10
            elif event.key != pygame.K_LEFT and event.key != pygame.K_RIGHT:
                continue
            goingHome = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT: 
                xChange = 7
            if event.key == pygame.K_RIGHT:
                xChange = -7
            elif event.key != pygame.K_LEFT and event.key != pygame.K_RIGHT:
                continue
            goingHome = True

        if event.type != pygame.KEYDOWN and event.type != pygame.KEYUP:
            continue

    if goingHome:
        if xChange < 0:
            if carCurrentX < carStartX:
                xChange = 0
                carCurrentX = carStartX
        elif xChange > 0:
            if carCurrentX > carStartX:
                xChange = 0
                carCurrentX = carStartX

    if carCurrentX > 0 and carCurrentX < ( displayWidth - 50 ):         
        carCurrentX += xChange
    else:
        if carCurrentX <= 0:
            xChange = 5

        elif carCurrentX >= ( displayWidth - 50 ):
            xChange = -5
            
        carCurrentX += xChange
        goingHome = True

        
    gameDisplay.fill( WHITE )
    car( carCurrentX, carStartY )

    pygame.display.update()
    clock.tick( 60 )
    
pygame.quit()
