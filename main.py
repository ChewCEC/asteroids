import pygame
from constants import *

print("Starting asteroids!")
print(f'Screen width: {SCREEN_WIDTH}')
print(f'Screen height: {SCREEN_HEIGHT}')


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill((0, 0, 0))
    pygame.display.flip()

    #main()
