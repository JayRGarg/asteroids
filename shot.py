import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.time_since_shot = 0

    def draw(self, screen):
        scale = 0.005
        pygame.draw.line(screen, (102, 255, 0), self.position+(self.velocity*self.radius*scale), self.position-(self.velocity*self.radius*scale), width=1)
        if (not (0+self.radius/2 < self.position.x < SCREEN_WIDTH-self.radius/2)) or (not (0+self.radius/2 < self.position.y < SCREEN_HEIGHT-self.radius/2)):
            first_pos = self.position
            wrap_pos = pygame.Vector2(first_pos.x % SCREEN_WIDTH, first_pos.y % SCREEN_HEIGHT) #wraparound position
            pygame.draw.line(screen, (102, 255, 0), wrap_pos+(self.velocity*self.radius*scale), wrap_pos-(self.velocity*self.radius*scale), width=1)
        return

    def update(self, dt):
        self.time_since_shot += dt
        if self.time_since_shot > BULLET_TIME:
            self.kill()
        
        self.position += self.velocity * dt
        # WRAP AROUND
        self.position.x %= SCREEN_WIDTH
        self.position.y %= SCREEN_HEIGHT
        
