import pygame
from constants import *

def main():
    pygame.init()
    delta_time = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Loop principal del juego
    running = True
    while running:
        screen.fill((0, 0, 0))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
        dt = delta_time.tick(144)/1000
    pygame.quit()

if __name__ == '__main__':
    print("Starting asteroids!")
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')
    main()
