import pygame
import random
import math




pygame.init()
#window size
screen = pygame.display.set_mode((1000,800,))
# title and icon
icon = pygame.image.load('neo.png')
pygame.display.set_icon(icon)

#player
playerimg= pygame.image.load('star-wars.png')
playerX=475
playerY=350
#enemy
enemyimg= pygame.image.load('space-station.png')
enemyX=random.randint(0,800)
enemyY=random.randint(0,600)


def player(x,y):
    screen.blit(playerimg,(x,y))
def enemy(x,y):
    screen.blit(enemyimg,(x,y))
running=True
while running:
    #background color
    screen.fill((0, 51, 102))
   ## playerX +=0.1 for movement
    for event in pygame.event.get():
        if event.type == pygame.QUIT :  # close for press x
            running= False


    #enemy follow center
    dx=playerX-enemyX
    dy=playerY-enemyY
    angle=math.atan2(dx,dy)
    mx=(math.sin(angle))*0.1
    my=math.cos((angle))*0.1

    enemyX += mx
    enemyY += my






    player(playerX,playerY)
    enemy(enemyX,enemyY)
    pygame.display.update()