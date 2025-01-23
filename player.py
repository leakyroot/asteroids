import pygame
from circleshape import *
from constants import *
from main import *
from shot import *

class Player(CircleShape):
    
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.position = pygame.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
        
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            #print(f"Shot spawn at {self.position.x} / {self.position.y}")
            #Shot(self.position.x, self.position.y, SHOT_RADIUS)
            self.shoot(self.position.x, self.position.y, SHOT_RADIUS)

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def shoot(self, x, y, radius):
        shot = Shot(x, y, radius)
        shot.rotate(self.rotation)
        #print(f"Shot's rotation vector points at {shot.rotation}")
    


    