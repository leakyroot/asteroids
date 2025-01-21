import pygame
from constants import *
from player import *

def main():
	pygame.init()
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2)
	clock = pygame.time.Clock()
	dt = 0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	while True:
		for event in pygame.event.get():
    		
			if event.type == pygame.QUIT:
        		
				return
		
		screen.fill(000000)
		player.update(dt)
		player.draw(screen)
		dt = clock.tick(60) / 1000
		pygame.display.flip()



	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

	
	

if __name__ == "__main__":
	main()