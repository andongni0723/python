import pygame
import random
import math

pygame.init()

#set game
running = True
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("plane")

#set game icon
icon = pygame.image.load("player.png")
pygame.display.set_icon(icon)

#set game background
bg= pygame.image.load("bg.png")

#set game player
player = pygame.image.load("player.png")
playerX = 400
playerY = 500
playerspeed = 0

#set game enemy
enemyNum = 6
class Enemy():
    def __init__(self):
        self.image = pygame.image.load("enemy.png")
        self.x = random.randint(200, 600)
        self.y = random.randint(50, 250)
        self.speed = random.randint(2, 4)

enemies = []
for i in range(enemyNum):
    enemies.append(Enemy())

def show_enemy():
    
    for e in enemies:
        screen.blit(e.image,(e.x, e.y))
        e.x += e.speed
        
        if (e.x > 750 or e.x < 0):
            e.speed *= -1
            e.y += 40

def distance(bx,by,ex,ey):
    a = bx - ex
    b = by - ey
    return math.sqrt(a*a + b*b)
    

class Bullet():
    def __init__(self):
        self.image = pygame.image.load("bullet.png")
        self.x = playerX + 16
        self.y = playerY + 10
        self.speed = 10
    
    # def hit():
    #     for e in enemies:
    #         if (distance(self.x, self.y, e.x, e.y) < 30):
    #             bullets.remove(self)
    #             e.x = 11
        
bullets = []

def show_bullet():
    for b in bullets:
        screen.blit(b.image,(b.x, b.y))
        b.y -=b.speed
        if (b.y < 0):
            bullets.remove(b)
            
def game_event():
    
    global running, playerspeed
    
    for event in pygame.event.get():
        
        if (event.type == pygame.QUIT):
            running = False
            
        #player move
        if (event.type == pygame.KEYDOWN):
            
            if (event.key == pygame.K_RIGHT or event.key == pygame.K_d):
                playerspeed = 2
            elif (event.key == pygame.K_LEFT or event.key == pygame.K_a):
                playerspeed = -2
            elif (event.key == pygame.K_SPACE):
                #shoot bullet
                bullets.append(Bullet())
                
        if (event.type == pygame.KEYUP):
                playerspeed = 0

def player_move(): 
      
    global playerX
    
    screen.blit(player,(playerX,playerY))
    playerX += playerspeed
    
    if (playerX > 736):
        playerX = 736
    if (playerX < 0):
        playerX = 0
        
    
#main loop
while running:
    screen.blit(bg,(0,0)) #draw background
    
    game_event()   
    player_move()   
    show_enemy()   
    show_bullet()
     
    pygame.display.update()