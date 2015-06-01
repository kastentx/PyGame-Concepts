# Nick Kasten
# pygameTemplate.py
# Basic Template for PyGame

import pygame, sys
from pygame.locals import *

pygame.init()

# basic colors
#          R    G    B
RED   = ( 255,   0,   0 )
GREEN = (   0, 255,   0 )
BLUE  = (   0,   0, 255 )
WHITE = ( 255, 255, 255 )
BLACK = (   0,   0,   0 )

# window dimensions
displayWidth  = 640
displayHeight = 480
gameDisplay   = pygame.display.set_mode( ( displayWidth, ( displayHeight ) ) )
screenRect    = gameDisplay.get_rect()
pygame.display.set_caption('My Game')

# frames per second setting
FPS      = 30  
fpsClock = pygame.time.Clock()
running  = True

# Content and Position of Title text
titleText = pygame.font.Font( 'freesansbold.ttf', 48 )
titleSurfaceObj = titleText.render( 'Hungry Snake Challenge', True, GREEN, BLUE )
titleRectObj = titleSurfaceObj.get_rect( center = ( screenRect.centerx, screenRect.centery - 100 ) )

# Content and Position of Game Over text
gameOverText = pygame.font.Font( 'freesansbold.ttf', 48 )
gameOverSurfaceObj = gameOverText.render( 'GAME OVER', True, WHITE )
gameOverRectObj = gameOverSurfaceObj.get_rect( center = ( screenRect.centerx, screenRect.centery - 100 ) )

# Content and Position of Press a Key text
pressKeyText = pygame.font.Font( 'freesansbold.ttf', 18 )
pressKeySurfaceObj = pressKeyText.render( 'Press any key to play...', True, WHITE )
pressKeyRectObj = pressKeySurfaceObj.get_rect( center = ( screenRect.centerx, screenRect.centery + 100 ) )



###### FUNCTION DEFINITIONS ######
def keyPressed():
    """ Removes KEYDOWN events from the event queue
        and returns KEYUP events """
    
    checkForQuit()

    for event in pygame.event.get( [ KEYDOWN, KEYUP ] ):
        if event.type == KEYDOWN:
            continue
        return event.key
    return None
    

def checkForQuit():
    for event in pygame.event.get(QUIT): # get all the QUIT events
        terminate() # terminate if any QUIT events are present
    for event in pygame.event.get(KEYUP): # get all the KEYUP events
        if event.key == K_ESCAPE:
            terminate() # terminate if the KEYUP event was for the Esc key
        pygame.event.post(event) # put the other KEYUP event objects back

def terminate():
    pygame.quit()
    sys.exit()
###### END OF FUNCTION DEFINITIONS ######

# main game loop:
while running:
    gameDisplay.blit( titleSurfaceObj, titleRectObj ) # display title text
    gameDisplay.blit( pressKeySurfaceObj, pressKeyRectObj ) # display press any key text
    while keyPressed() == None:
        pygame.display.update()
        fpsClock.tick( FPS )

    gameDisplay.fill( BLACK )
    while keyPressed() == None:
        pygame.display.update()

    gameDisplay.blit( gameOverSurfaceObj, gameOverRectObj ) # display game over text
    gameDisplay.blit( pressKeySurfaceObj, pressKeyRectObj ) # display press any key text
    while keyPressed() == None:
        pygame.display.update()
    
        fpsClock.tick( FPS )

    
    pygame.display.update()
    fpsClock.tick( FPS )
pygame.quit()
