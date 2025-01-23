import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable)
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2)
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    
    

    while True:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                
                return
        
        screen.fill(000000)

        dt = clock.tick(60) / 1000
        asteroid_field.update(dt)
        for item in updatable:
                item.update(dt)
        for item in asteroids:
                if item.collision(player):
                      print("GAME OVER!")
                      sys.exit()
        
        #for item in drawable:
        #    if isinstance(item, Asteroid):  # Check specifically for asteroids
        #        print(f"Asteroid at ({int(item.position.x)}, {int(item.position.y)}) with radius {item.radius}")
        for item in drawable:
                item.draw(screen)
        
        
        pygame.display.flip()


    
    

if __name__ == "__main__":
    main()