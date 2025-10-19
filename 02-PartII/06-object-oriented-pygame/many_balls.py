# pygame demo 6(b) - using the Ball class, bounce many balls

# 1 - Import packages
from Ball import *
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
BALL_WIDTH_HEIGHT = 100
N_PIXELS_TO_MOVE = 3
N_BALLS = 10
MAX_WIDTH = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT - BALL_WIDTH_HEIGHT
ball_x = random.randrange(MAX_WIDTH)
ball_y = random.randrange(MAX_HEIGHT)
x_speed = N_PIXELS_TO_MOVE
y_speed = N_PIXELS_TO_MOVE
BASE_PATH = Path(__file__).resolve().parent
path_to_ball = BASE_PATH / "images/ball.png"

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Load assets: image(s), sound(s), etc.
ball_image = pygame.image.load(path_to_ball)

# 5 - Initialize variables
ball_list = []
for ball in range(N_BALLS):
    ball = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)
    ball_list.append(ball)
    
# 6 - Loop forever
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if (ball_x < 0) or (ball_y >= MAX_WIDTH):
            x_speed = -x_speed
        if (ball_y < 0) or (ball_y >= MAX_HEIGHT):
            y_speed = -y_speed
            
        ball_x += x_speed
        ball_y += y_speed
        
    # 8 - Do any "per frame" actions
    for ball in ball_list:
        ball.update()
        
    window.fill(BLACK)
    
    for ball in ball_list:
        ball.draw()
        
    pygame.display.update()
    clock.tick(FRAMES_PER_SECOND)