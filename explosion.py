import pygame
from circleshape import CircleShape
from constants import *
import copy

class Explosion(CircleShape):

    def __init__(self, x, y, velocity, radius):
        super().__init__(x, y, radius)
        self.velocity = velocity
        self.time_since_explosion = 0
        EXPLOSION_SOUND.play(maxtime=200)

    def draw(self, screen):
        path = "./assets/images/explosion-cloud.png"
        img = pygame.image.load(path).convert_alpha()
        img = pygame.transform.scale_by(img, 0.05*ASTEROID_MIN_RADIUS)
        #img = pygame.transform.laplacian(img)
        img.set_colorkey((0, 0, 0))
        img.set_alpha(255*(EXPLOSION_TIME-self.time_since_explosion))
        #img = pygame.transform.flip(img, False, True)
        #img = pygame.transform.rotate(img, -self.rotation)
        img_rect = img.get_rect(center=self.position)
        screen.blit(img, img_rect.topleft)
        if (not (0+self.radius/2 < self.position.x < SCREEN_WIDTH-self.radius/2)) or (not (0+self.radius/2 < self.position.y < SCREEN_HEIGHT-self.radius/2)):
            first_pos = img_rect.topleft
            wrap_pos = pygame.Vector2(first_pos[0] % SCREEN_WIDTH, first_pos[1] % SCREEN_HEIGHT) #wraparound position
            screen.blit(img, wrap_pos)
        return

    def update(self, dt):
        self.time_since_explosion += dt
        if self.time_since_explosion > EXPLOSION_TIME:
            self.kill()

        self.position += self.velocity * dt
        # WRAP AROUND
        self.position.x %= SCREEN_WIDTH
        self.position.y %= SCREEN_HEIGHT
