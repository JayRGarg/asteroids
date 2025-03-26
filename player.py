import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0 # degrees
        self.time_last_shot = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation) * self.radius
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward
        b = self.position - forward - right
        c = self.position - forward + right
        return [a, b, c]

    def draw(self, screen):
        #pygame.draw.polygon(screen, "white", self.triangle(), width=2)
        path = "./assets/rocket-blackbg.jpeg"
        img = pygame.image.load(path)
        img = pygame.transform.scale_by(img, 0.005*PLAYER_RADIUS)
        img.set_colorkey((0, 0, 0))
        img = pygame.transform.flip(img, False, True)
        img = pygame.transform.laplacian(img)
        img = pygame.transform.rotate(img, -self.rotation)
        img_rect = img.get_rect(center=self.position)
        screen.blit(img, img_rect.topleft)
        if (not (0+self.radius/2 < self.position.x < SCREEN_WIDTH-self.radius/2)) or (not (0+self.radius/2 < self.position.y < SCREEN_HEIGHT-self.radius/2)):
            first_pos = img_rect.topleft
            wrap_pos = pygame.Vector2(first_pos[0] % SCREEN_WIDTH, first_pos[1] % SCREEN_HEIGHT) #wraparound position
            screen.blit(img, wrap_pos)
        return

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        return

    def move(self, dt):
        curr_direction = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += curr_direction * PLAYER_SPEED * dt
        return

    def shoot(self):
        if self.time_last_shot <= 0:
            s = Shot(self.position.x, self.position.y)
            s.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            self.time_last_shot = PLAYER_SHOOT_COOLDOWN
        return
        

    def update(self, dt):
        self.time_last_shot -= dt

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

        # WRAP AROUND
        self.position.x %= SCREEN_WIDTH
        self.position.y %= SCREEN_HEIGHT
