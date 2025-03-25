import pygame
from circleshape import CircleShape
from constants import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0 # degrees

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation) * self.radius
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward
        b = self.position - forward - right
        c = self.position - forward + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), width=2)
        return

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        return

    def move(self, dt):
        curr_direction = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += curr_direction * PLAYER_SPEED * dt
        return
        

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_w]:
            self.move(dt)
