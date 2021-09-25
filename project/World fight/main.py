#-----------------------#
# data   : 2021/09/25   #
# github : andongni0723 #
# video  : 36:50        #
#-----------------------#

import pygame
from pygame.constants import K_RIGHT
from pygame.key import get_pressed
from pygame.sprite import Group

FPS = 60
WIDTH = 500
HEIGHT = 600

# color
WHILE = (255, 255, 255)
GREEN = (0, 255, 0)

# init game
pygame.init()
pygame.display.set_caption("World Fight")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# sprite
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.speedx = 8

    def update(self):
        key_pressed = pygame.key.get_pressed()

        if key_pressed[pygame.K_d]:
            self.rect.x += self.speedx
        if key_pressed[pygame.K_a]:
            self.rect.x -= self.speedx

all_sprites = pygame.sprite.Group()    
player = Player()
all_sprites.add(player)

# game while
running = True
while running:
    clock.tick(FPS)
    # get input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # new the game
    all_sprites.update()

    # show on      
    screen.fill(WHILE)
    all_sprites.draw(screen)
    pygame.display.update()
pygame.quit()