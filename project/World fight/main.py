#-----------------------#
# data   : 2021/09/25   #
# github : andongni0723 #
# video  : 36:50        #
#-----------------------#
import pygame
import random
import os
from pygame.sprite import collide_circle

from pygame.transform import scale

FPS = 60
WIDTH = 500
HEIGHT = 600

# color
WHILE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

# init game
pygame.init()
pygame.display.set_caption("World Fight")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# load the image
background_img = pygame.image.load(os.path.join("img", "background.png")).convert()
player_img = pygame.image.load(os.path.join("img", "player.png")).convert()
rock_img = pygame.image.load(os.path.join("img", "rock.png")).convert()
bullet_img = pygame.image.load(os.path.join("img", "bullet.png")).convert()

# class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img, (50, 38))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 8
        self.radius = 20

    def update(self):
        key_pressed = pygame.key.get_pressed()

        if key_pressed[pygame.K_d]:
            self.rect.x += self.speedx
        if key_pressed[pygame.K_a]:
            self.rect.x -= self.speedx
        
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
    
    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        bullets.add(bullet)
        all_sprites.add(bullet)

class Rock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = rock_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = random.randint(-100, -40)
        self.speedy = random.randint(2, 10)
        self.speedx = random.randint(-3, 3)
        self.radius = self.rect.width * 0.85 / 2

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx

        if self.rect.top > HEIGHT or self.rect.left > WIDTH or self.rect.right < 0:
            self.rect.x = random.randint(0, WIDTH - self.rect.width)
            self.rect.y = random.randint(-100, -40)
            self.speedy = random.randint(2, 10)
            self.speedx = random.randint(-3, 3) 

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        
        if self.rect.bottom < 0:
            self.kill()

all_sprites = pygame.sprite.Group()   
rocks = pygame.sprite.Group()
bullets = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

for i in range(8):
    rock = Rock()
    rocks.add(rock)
    all_sprites.add(rock)

# game while
running = True
while running:
    clock.tick(FPS)
    # get input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

    # new the game
    all_sprites.update()

    hits = pygame.sprite.groupcollide(rocks, bullets, True, True) # hit to destoy
    for hit in hits:
        r = Rock()
        all_sprites.add(r)
        rocks.add(r)

    hits = pygame.sprite.spritecollide(player, rocks, False, pygame.sprite.collide_circle)
    for hit in hits:
        running = False

    # show on      
    screen.fill(BLACK)
    screen.blit(background_img, (0, 0))
    all_sprites.draw(screen)
    pygame.display.update()

pygame.quit()