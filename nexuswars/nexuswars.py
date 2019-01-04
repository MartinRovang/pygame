from sys import exit
from os import environ
import pygame
from time import sleep, localtime
import numpy as np
import random





width_screen = 800
height_screen = 800

SCREENSIZE = (width_screen, height_screen)

environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
screen = pygame.display.set_mode(SCREENSIZE)



#All monsters:
#pygame.image.load("lvl1.png")


class Monsters:
    def __init__(self):
        self.img = pygame.image.load("lvl1.png")
        self.x = 400
        self.y = np.random.randint(300,400,1)

    def Update(self):
        self.x += 4
        screen.blit(self.img,(self.x, self.y))


class Player:
    def __init__(self):
        self.background = pygame.image.load("nexus_main_100.png")
        self.health = 100
        self.army_total = []
        self.tick = pygame.time.get_ticks()

    def Health_update(self, dmg = 0):
        self.health -= dmg
        if self.health >= 100:
            self.background = pygame.image.load("nexus_main_100.png")
        if self.health <= 80 and self.health >= 60:
            self.background = pygame.image.load("nexus_main_80.png")
        if self.health <= 60 and self.health >= 40:
            self.background = pygame.image.load("nexus_main_60.png")
        if self.health <= 40 and self.health >= 20:
            self.background = pygame.image.load("nexus_main_40.png")
        if self.health <= 20 and self.health >= 0:
            self.background = pygame.image.load("nexus_main_20.png")
        if self.health <= 0:
            self.background = pygame.image.load("nexus_main_0.png")


    def Monster_update(self):
        if self.tick < pygame.time.get_ticks():
            monst = Monsters()
            self.army_total.append(monst)
            self.tick += 1000
        for army in self.army_total:
            if army.x >= 800:
                self.army_total.remove(army)
            army.Update()




class Game():
    def __init__(self, players):
        self.gold = 0
        self.menu = 0
        self.player = players
        self.tick = pygame.time.get_ticks()


    def Events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()


    def Update(self):
        self.player.Health_update()
        screen.blit(self.player.background,(0,0))
        self.player.Monster_update()
        pygame.display.flip()

        





player1 = Player()
game_current = Game(player1)





while True:
    game_current.Events()
    game_current.Update()
    sleep(0.0001)