# PyGame template - skeleton for a new pygame project
import pygame
import random
from os import path


# Folders for assets
img_dir = path.join(path.dirname(__file__), 'img')

# Global Constants for window settings
WIDTH   = 480
HEIGHT  = 600
FPS     = 60

# Global Constants for colors
BLACK   = (0, 0, 0)
WHITE   = (255, 255, 255)
RED     = (255, 0, 0)
GREEN   = (0, 255, 0)
BLUE    = (0, 0, 255)

# Initialize PyGame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")
clock = pygame.time.Clock()


class Player(pygame.sprite.Sprite):
    """docstring for Player."""

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 16
        # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if (keystate[pygame.K_LEFT]):
            self.speedx = -10
        if (keystate[pygame.K_RIGHT]):
            self.speedx = 10
        self.rect.x += self.speedx
        if (self.rect.right > (WIDTH - 10)):
            self.rect.right = WIDTH - 10
        if (self.rect.left < 10):
            self.rect.left = 10


class Mob(pygame.sprite.Sprite):
    """docstring for Mob."""

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = bug_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 18
        # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if ((self.rect.top > HEIGHT + 10) or (self.rect.left < -25) or (self.rect.right > WIDTH + 20)):
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)
            self.speedx = random.randrange(-3, 3)


class Bullet(pygame.sprite.Sprite):
    """docstring for Bullet."""

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        # kill it if it moves off top screen
        if (self.rect.bottom < 0):
            self.kill()

# Load all game graphics
background = pygame.image.load(path.join(img_dir, 'bg.png')).convert()
background_rect = background.get_rect()
player_img = pygame.image.load(path.join(img_dir, 'ship.png')).convert()
bug_img = pygame.image.load(path.join(img_dir, 'bug1.png')).convert()
bullet_img = pygame.image.load(path.join(img_dir, 'laser.png')).convert()

# Sprites
all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
for i in range(8):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)

#------- Game Loop -------#
running = True
while running:
    # Keep loop running at the right speed
    clock.tick(FPS)

#------- Process Events -------#
    for event in pygame.event.get():
        # Check for closing window event
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

#------- Update -------#
    all_sprites.update()

    # Check to see if a bullet hit a mob
    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    for hit in hits:
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)

    # Check to see if a mob hit the player
    hits = pygame.sprite.spritecollide(player, mobs, False, pygame.sprite.collide_circle)
    if hits:
        running = False


#------- Draw/Render -------#
    screen.fill(BLACK)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
