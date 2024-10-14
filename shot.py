import pygame
from circleshape import CircleShape
import constants

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, constants.SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(
            screen, 
            center=self.position, 
            color="white", 
            radius=self.radius, 
            width=1 )


    def update(self, dt):
        self.position += self.velocity * dt * constants.PLAYER_SHOOT_SPEED



