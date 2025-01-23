import pygame
from circleshape import *
from constants import *
from main import *
from player import *

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0
        self.velocity = pygame.Vector2(0,1)

    def draw(self, surface):
        pygame.draw.circle(surface, (255, 255, 255), (self.position.x, self.position.y), self.radius, 2)
            
    def update(self, dt):
        #print(f"Shot position update! Velocity: {self.velocity}")
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SHOOT_SPEED * dt
        print(f"Shot rotation: {self.rotation}, Shot position: {self.position}")

    def rotate(self, player_rotation):
        #print(f"Projectile vector points at {player_rotation}")
        self.rotation = player_rotation