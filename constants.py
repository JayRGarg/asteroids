import pygame 

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

ASTEROID_MIN_RADIUS = 20
ASTEROID_KINDS = 3
ASTEROID_SPAWN_RATE = 1#0.8  # seconds
ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS
ASTEROID_MIN_SPEED = 40
ASTEROID_MAX_SPEED = 100

PLAYER_RADIUS = 50#20
PLAYER_TURN_SPEED = 300
PLAYER_SPEED = 200

SHOT_RADIUS = 5
PLAYER_SHOOT_SPEED = 500
PLAYER_SHOOT_COOLDOWN = 0.1#0.3
BULLET_TIME = 1.5

EXPLOSION_TIME = 1

#pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.mixer.init()
BLASTER_SOUND = pygame.mixer.Sound('./assets/sounds/gun-blast.mp3')
raw = BLASTER_SOUND.get_raw()
print(len(raw))
raw = raw[70000:]
BLASTER_SOUND = pygame.mixer.Sound(buffer=raw)
BLASTER_SOUND.set_volume(0.2)

ROCK_BREAK_SOUND = pygame.mixer.Sound('./assets/sounds/rock-crack.mp3') 
ROCK_BREAK_SOUND.set_volume(0.4)

EXPLOSION_SOUND = pygame.mixer.Sound('./assets/sounds/explosion.mp3') 
EXPLOSION_SOUND.set_volume(0.5)
