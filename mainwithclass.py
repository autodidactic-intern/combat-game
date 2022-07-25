import pygame
import random
import math
import time
import numpy as np
pygame.init()                                      #init (start)game

title=pygame.display.set_caption("Red pills") #title
icon = pygame.image.load('neo.png')  # icon
pygame.display.set_icon(icon)
screen=pygame.display.set_mode((1000,800,))    #window size
clock = pygame.time.Clock()

class Game():
    def __init__(self):
        self.player = Player()
        self.enemy = Enemy()
        self.screen = pygame.display.set_mode((1000, 800,))

    def step(self):
        self.screen.fill((0, 51, 102))
        self.screen.blit(self.player.img, (self.player.x, self.player.y))
        self.screen.blit(self.enemy.img, (self.enemy.x, self.enemy.y))

        pygame.display.update()

class Bullet():
    def __init__(self, x, y):
        self.pos = (x, y)
        mx, my = pygame.mouse.get_pos()
        self.dir = (mx - x, my - y)
        length = math.hypot(*self.dir)
        if length == 0.0:
            self.dir = (0, -1)
        else:
            self.dir = (self.dir[0] / length, self.dir[1] / length)
        angle = math.degrees(math.atan2(-self.dir[1], self.dir[0]))
        self.bullet = pygame.Surface((7, 2)).convert_alpha()
        self.bullet.fill((255, 255, 255))
        self.bullet = pygame.transform.rotate(self.bullet, angle)
        self.speed = 2

    def update(self):
        self.pos = (self.pos[0] + self.dir[0] * self.speed,
                    self.pos[1] + self.dir[1] * self.speed)

    def draw(self, surf):
        bullet_rect = self.bullet.get_rect(center=self.pos)
        surf.blit(self.bullet, bullet_rect)

def collision():
    distance=math.sqrt((showenemy.x-bullet.pos[0])**2+(showenemy.y-bullet.pos[0])**2)
    if distance <27:
        return True
    else:
        return False

class Player():
    def __init__(self):
        self.img = pygame.image.load('star-wars.png')
        self.x = 475
        self.y = 350
class Enemy():
    def __init__(self):

        self.img = pygame.image.load('space-station.png')
        self.x = random.randint(0,900)
        self.y = random.randint(0,700)
    def approach(self):

        dx = showplayer.x - showenemy.x
        dy = showplayer.y - showenemy.y
        angle = math.atan2(dx, dy)
        mx = (math.sin(angle))*0.5
        my = math.cos((angle))*0.5
        self.x += mx
        self.y += my

showplayer=Player()
showenemy=Enemy()
bullets = []
pos = (510, 375)


#player = Player()

game = Game()

running=True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT :  # close for press x
            running= False
        if event.type == pygame.MOUSEBUTTONDOWN:
            bullets.append(Bullet(*pos))

    for bullet in bullets[:]:
        bullet.update()
        if not screen.get_rect().collidepoint(bullet.pos):
            bullets.remove(bullet)



    for bullet in bullets:
        bullet.draw(screen)
    pygame.display.flip()



    showenemy.approach()
    game.enemy = showenemy
    game.player = showplayer
    game.step()
