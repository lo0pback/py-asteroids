from circleshape import CircleShape
from constants import * 
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        return pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        else:
           random_angle = random.uniform(20, 50)
           new_radius = self.radius - ASTEROID_MIN_RADIUS

           vector_1 = self.velocity.rotate(random_angle)
           vector_2 = self.velocity.rotate(-random_angle)
           
           asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
           asteroid_1.velocity = vector_1 * 1.2

           asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
           asteroid_2.velocity = vector_2 * 1.2

    