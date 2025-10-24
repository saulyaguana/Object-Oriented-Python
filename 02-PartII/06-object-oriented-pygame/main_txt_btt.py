# pygame demo 8 - SimpleText, SimpleButton, and Ball

# 1 - Import packages
import pygame
from pygame.locals import *
import sys
import random
from pathlib import Path
from Ball import *
from SimpleText import *
from SimpleButton import *

# 2 - Define constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
PATHS = Path(__file__).resolve().parent

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

ball = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)
frame_count_label = SimpleText(window, (60, 20), "Program has run through this many loops:", WHITE)
frame_count_display = SimpleText(window, (500, 20), "", WHITE)
restart_button = SimpleButton(window, (280, 60), PATHS / "images/restartUp.png", PATHS / "images/restartDown.png")
frame_counter = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if restart_button.handle_event(event):
            frame_counter = 0
            
    ball.update()
    frame_counter += 1
    frame_count_display.set_value(str(frame_counter))
    
    window.fill(BLACK)
    ball.draw()
    frame_count_label.draw()
    frame_count_display.draw()
    restart_button.draw()
    
    pygame.display.update()
    clock.tick(FRAMES_PER_SECOND)