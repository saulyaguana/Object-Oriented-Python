# pygame demo 4(b) - one image, bounce arounf the window using rects

# 1 - Import packages
import pygame
from pygame.locals import *
import sys
import random
from pathlib import Path

# 2 - Define constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
N_PIXELS_PER_FRAME = 3
BASE_PATH = Path(__file__).resolve().parent
path_to_ball = BASE_PATH / "images/ball.png"

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Load assests: image(s), sound(s), etc.
ball_image = pygame.image.load(path_to_ball)

# 5 - Initialize variables
ball_rect = ball_image.get_rect()
MAX_WIDTH = WINDOW_WIDTH - ball_rect.width
MAX_HEIGHT = WINDOW_HEIGHT - ball_rect.height
ball_rect.left = random.randrange(MAX_WIDTH)
ball_rect.top = random.randrange(MAX_HEIGHT)
x_speed = N_PIXELS_PER_FRAME
y_speed = N_PIXELS_PER_FRAME

# 6 - Loop forever
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    if (ball_rect.left < 0) or (ball_rect.right >= WINDOW_WIDTH):
        x_speed = -x_speed
        
    if (ball_rect.top < 0) or (ball_rect.bottom >= WINDOW_HEIGHT):
        y_speed = -y_speed
        
    # Update the ball's rectangle using the speed in two directions
    ball_rect.left += x_speed
    ball_rect.top += y_speed
    
    window.fill(BLACK)
    
    window.blit(ball_image, ball_rect)
    pygame.display.update()
    
    clock.tick(FRAMES_PER_SECOND)