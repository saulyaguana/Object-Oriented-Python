# Pygame demo 7 - Simple Button test

# 1- Import packages
from pathlib import Path
import pygame
from pygame.locals import *
import sys
import random
from Ball import *
from SimpleButton import *

# 2 - Define constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
PATHS = Path(__file__).resolve().parent
# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Load assets: image(s), sound(s), etc.
ball = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)

# 5 - Initialize variables
# Create an instance of a SimpleButton
button = SimpleButton(window, (150, 30), PATHS / "images/buttonUp.png", PATHS / "images/buttonDown.png")

# 6 - Loop forever
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if button.handle_event(event):
            print("User has clicked the button")
            
    window.fill(BLACK)
    button.draw()
    pygame.display.update()
    clock.tick(FRAMES_PER_SECOND)