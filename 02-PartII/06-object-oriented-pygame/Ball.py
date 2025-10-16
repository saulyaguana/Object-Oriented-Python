import pygame
from pygame.locals import *
import random
from pathlib import Path

# Ball class
class Ball():
    def __init__(self, window, window_width, window_height):
        self.window = window
        self.window_width = window_width
        self.window_height = window_height
        self.image = pygame.image.load(Path(__file__).resolve().parent / "images/ball.png")
        
        ball_rect = self.image.get_rect()
        self.width = ball_rect.width
        self.height = ball_rect.height
        self.max_width = window_width - self.width
        self.max_height = window_height - self.height
        
        self.x = random.randrange(0, self.max_width)
        self.y = random.randrange(0, self.max_height)
        
        speeds_list = [-4, -3, -2, -1, 1, 2, 3, 4]
        self.x_speed = random.choice(speeds_list)
        self.y_speed = random.choice(speeds_list)
        
    def update(self):
        if (self.x < 0) or (self.x >= self.max_width):
            self.x_speed = -self.x_speed
            
        if (self.y < 0) or (self.y >= self.max_height):
            self.y_speed = -self.y_speed
            
        self.x += self.x_speed
        self.y += self.y_speed
        
    def draw(self):
        self.window.blit(self.image, (self.x, self.y))