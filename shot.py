import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        #pygame.draw.circle(screen, "white", self.position, self.radius, width=2)
        scale = 0.005
        pygame.draw.line(screen, (102, 255, 0), self.position+(self.velocity*self.radius*scale), self.position-(self.velocity*self.radius*scale), width=1)
        return

    def update(self, dt):
        self.position += self.velocity * dt
