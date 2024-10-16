import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    delta_time = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))    

    # Create player
    x_coord = SCREEN_WIDTH / 2
    y_coord = SCREEN_HEIGHT / 2

    # Creating two containers updatable and drawable
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    player = Player(x_coord, y_coord)
    asteriod_field = AsteroidField() 

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
        
        # update movile objects
        for obj_update in updatable:
            obj_update.update(dt)

        screen.fill("black")
        # draw objects
        for obj_draw in drawable:
            obj_draw.draw(screen)        

        # check for colisions
        for ast in asteroids:
            if player.checkColision(ast):
                sys.exit("Game Over")
            
            for shot in shots:
                if ast.checkColision(shot):
                    ast.split()
                    shot.kill()


        # render screen should be always at last, if not none of the objects will display
        pygame.display.flip()
        
        dt = delta_time.tick(144)/1000


    pygame.quit()

if __name__ == '__main__':
    main()
