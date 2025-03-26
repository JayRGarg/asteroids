import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH,SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    # creating groups for players
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable) #when pl is initialized, will be initialized with containers as groups argument
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    pl = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # update state of all updatable objects
        updatable.update(dt)

        # check for player collision
        for ast in asteroids:
            if ast.collides_with(pl):
                print("GAME OVER!")
                exit()
            for s in shots:
                if ast.collides_with(s):
                    ast.split()
                    s.kill()

        screen.fill("black")
        # draw all drawable objects
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()

        # limit frame rate to 60 FPS
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
