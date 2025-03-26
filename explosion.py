import pygame
from circleshape import CircleShape

class Explosion(CircleShape):

    def __init__(self, x, y, velocity, radius):
        super().__init__(x, y, radius)
        self.velocity = velocity
        self.time_since_explosion = 0

    def draw(self, screen):
        #pygame.draw.circle(screen, "white", self.position, self.radius, width=2)
        path = "./assets/red-explosion-blackbg.jpeg"
        img = pygame.image.load(path)
        img = pygame.transform.scale_by(img, 0.01*self.radius)
        img.set_colorkey((0, 0, 0))
        img.set_alpha(255*(2-self.time_since_explosion))
        #img = pygame.transform.flip(img, False, True)
        img = pygame.transform.laplacian(img)
        #img = pygame.transform.rotate(img, -self.rotation)
        img_rect = img.get_rect(center=self.position)
        screen.blit(img, img_rect.topleft)
        return

    def update(self, dt):
        self.position += self.velocity * dt
        self.time_since_explosion += dt
        if self.time_since_explosion > 2:
            self.kill()

