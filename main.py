import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from explosion import Explosion

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
    explosions = pygame.sprite.Group()

    Player.containers = (updatable, drawable) #when pl is initialized, will be initialized with containers as groups argument
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)
    Explosion.containers = (updatable, drawable, explosions)

    MANUAL_DELETION = True

    if MANUAL_DELETION:
        set_asteroids = set()
        set_explosions = set()
        remove_asteroids = []
        remove_explosions = []

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
            if MANUAL_DELETION: set_asteroids.add(ast)
            if ast.collides_with(pl):
                print("GAME OVER!")
                exit()
            for s in shots:
                if ast.collides_with(s):
                    s.kill()
                    exp = ast.split()
                    if exp is not None:
                        if MANUAL_DELETION: set_explosions.add(exp)

        #IMMEDIATE DELETION for IMMEDIATE GARBAGE COLLECTION
        if MANUAL_DELETION:
            for a in set_asteroids:
                if not a.alive():
                    remove_asteroids.append(a)
            for e in set_explosions:
                if not e.alive():
                    remove_explosions.append(e)
            for a in remove_asteroids:
                set_asteroids.remove(a)
                del a
            remove_asteroids.clear()
            for e in remove_explosions:
                set_explosions.remove(e)
                del e
            remove_explosions.clear()

        screen.fill("black")
        # draw all drawable objects
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()

        # limit frame rate to 60 FPS
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
