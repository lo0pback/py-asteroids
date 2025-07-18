from circleshape import CircleShape
import pygame
from constants import *

class Shot(CircleShape):  
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        return pygame.draw.circle(screen, "white", self.position, SHOT_RADIUS, 2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)