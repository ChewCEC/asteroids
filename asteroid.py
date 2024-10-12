import pygame
from circleshape import CircleShape
from constants import ASTEROID_SPAWN_RATE, ASTEROID_KINDS, ASTEROID_MAX_RADIUS, ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, center=self.position, color="white", radius=self.radius, width=2)


    def update(self, dt):
        forward = pygame.Vector2(0, 1)
        self.position += self.velocity * dt * forward

    



