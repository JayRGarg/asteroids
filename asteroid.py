import pygame
from circleshape import CircleShape
from explosion import Explosion
from constants import *
import random

class Asteroid(CircleShape):
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        #pygame.draw.circle(screen, "white", self.position, self.radius, width=2)
        path = "./assets/asteroid-blackbg.jpeg"
        img = pygame.image.load(path)
        img = pygame.transform.scale_by(img, 0.01*self.radius)
        img.set_colorkey((0, 0, 0))
        img = pygame.transform.flip(img, False, True)
        img = pygame.transform.laplacian(img)
        #img = pygame.transform.rotate(img, -self.rotation)
        img_rect = img.get_rect(center=self.position)
        screen.blit(img, img_rect.topleft)
        return

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            Explosion(self.position.x, self.position.y, self.velocity, self.radius)
            return
        else:
            angle = random.uniform(20, 50)
            v1, v2 = self.velocity.rotate(angle), self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            ast1 = Asteroid(self.position.x, self.position.y, new_radius)
            ast2 = Asteroid(self.position.x, self.position.y, new_radius)
            ast1.velocity = v1 * 1.2
            ast2.velocity = v2 * 1.2
