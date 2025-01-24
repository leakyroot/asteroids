import pygame
import random
from circleshape import *
from constants import *
from main import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, surface):
        
        #print(f"Drawing asteroid at ({int(self.position.x)}, {int(self.position.y)}) on {surface}")
        pygame.draw.circle(surface, (255, 255, 255), (self.position.x, self.position.y), self.radius, 2)
        #if not (0 <= self.position.x <= SCREEN_WIDTH and 0 <= self.position.y <= SCREEN_HEIGHT):
        #    print(f"Asteroid off-screen at ({int(self.position.x)}, {int(self.position.y)})")
        #print(f"Drawing asteroid at ({int(self.position.x)}, {int(self.position.y)}) with radius {self.radius}")

        
    def update(self, dt):
        self.position += self.velocity * dt
        #print(f"Position: {self.position}, Velocity: {self.velocity}, dt: {dt}")

    def split(self):
        old_radius = self.radius
        old_position = self.position
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20,50)
            rotation1 = self.velocity.rotate(-angle)
            rotation2 = self.velocity.rotate(angle)
            new_radius = old_radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(old_position.x, old_position.y, new_radius)
            asteroid2 = Asteroid(old_position.x, old_position.y, new_radius)
            
            asteroid1.velocity = rotation1 * 1.2
            asteroid2.velocity = rotation2 * 1.2


