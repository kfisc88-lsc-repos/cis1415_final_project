# PyGame template - skeleton for a new pygame project
import pygame
import random

# Global Constants for window settings
WIDTH   = 360
HEIGHT  = 480
FPS     = 30

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
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    """docstring for Player."""

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, "ship.png")).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)


    def update(self):


# Sprites
all_sprites = pygame.sprite.Group()


# Game Loop
running = True
while running:
    # Keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # Check for closing window event
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()

    # Draw/Render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
