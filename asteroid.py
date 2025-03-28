import pygame
from circleshape import CircleShape
from explosion import Explosion
from constants import *
import random

class Asteroid(CircleShape):
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        path = "./assets/images/round-asteroid.png"
        img = pygame.image.load(path).convert_alpha()
        img = pygame.transform.scale_by(img, 0.008*self.radius)
        img.set_colorkey((0, 0, 0))
        img = pygame.transform.flip(img, False, True)
        #img = pygame.transform.laplacian(img)
        #img = pygame.transform.rotate(img, -self.rotation)
        img_rect = img.get_rect(center=self.position)
        screen.blit(img, img_rect.topleft)
        if (not (0+self.radius/2 < self.position.x < SCREEN_WIDTH-self.radius/2)) or (not (0+self.radius/2 < self.position.y < SCREEN_HEIGHT-self.radius/2)):
            first_pos = img_rect.topleft
            wrap_pos = pygame.Vector2(first_pos[0] % SCREEN_WIDTH, first_pos[1] % SCREEN_HEIGHT) #wraparound position
            screen.blit(img, wrap_pos)
        return

    def update(self, dt):
        self.position += self.velocity * dt
        
        # WRAP AROUND
        self.position.x %= SCREEN_WIDTH 
        self.position.y %= SCREEN_HEIGHT

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return Explosion(self.position.x, self.position.y, self.velocity, self.radius)
        else:
            angle = random.uniform(20, 50)
            v1, v2 = self.velocity.rotate(angle), self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            ast1 = Asteroid(self.position.x, self.position.y, new_radius)
            ast2 = Asteroid(self.position.x, self.position.y, new_radius)
            ast1.velocity = v1 * 1.2
            ast2.velocity = v2 * 1.2
            ROCK_BREAK_SOUND.play(maxtime=400)
            return
