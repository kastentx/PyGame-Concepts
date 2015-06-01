# Nick Kasten
# pixeltrackwclass.py
# move a single pixel aroudn the screen without crashing into the edges
# this is a rewrite of pixeltrack.py using a class to store pixel info
# 1/7/2015

import pygame

# directions of movement
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

class MovingPixel:
    """ a moving pixel class """

    def __init__(self, x, y):
        """ creates a pixel """
        self.x = x
        self.y = y
        self.hdir = 0
        self.vdir = 0

    def direction(self, pixelDir):
        """ changes the pixels direction """
        self.hdir, self.vdir = pixelDir

    def move(self):
        """ moves the pixel """
        self.x += self.hdir
        self.y += self.vdir

    def draw(self, surface):
        surface.set_at((self.x, self.y), (255, 255, 255))

# window dimensions
width = 640
height = 400

# set the screen and clock and prepare a 'run' variable
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True

# create pixel in center of screen
pix = MovingPixel(int(round(width / 2)), int(round(height / 2)))



while running:
    pix.move()

    if pix.x <= 0 or pix.x >= width or pix.y <= 0 or pix.y >= height:
        print("You Crashed!")
        running = False

    screen.fill((0, 0, 0))
    pix.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                pix.direction(UP)
            elif event.key == pygame.K_DOWN:
                pix.direction(DOWN)
            elif event.key == pygame.K_LEFT:
                pix.direction(LEFT)
            elif event.key == pygame.K_RIGHT:
                pix.direction(RIGHT)

    pygame.display.flip()
    clock.tick(120)
pygame.quit()
