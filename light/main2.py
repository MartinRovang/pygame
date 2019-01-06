from sys import exit
from os import environ
import pygame
from time import sleep, localtime
import numpy as np
import random

width_screen = 800
height_screen = 800

SCREENSIZE = (width_screen, height_screen)

# environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
screen = pygame.display.set_mode(SCREENSIZE)




colors = [(240,248,255),(69,139,116),(227,207,87),(0,0,205),(255,97,3)]

class spawned_object():
    def __init__(self):
        self.x_pos = pygame.mouse.get_pos()[0]
        self.y_pos = pygame.mouse.get_pos()[1]
        self.color = random.choice(colors)
        pygame.draw.rect(screen, self.color, (self.x_pos,self.y_pos,100,100), 1)
        self.lock = 0
        self.timer = pygame.time.get_ticks()
        self.g = 1
        self.vel = 1

    def Update(self,position = [0,0]):
        if self.y_pos >= (800-100) or (position[0]+100 >= self.x_pos and position[0]-100 <= self.x_pos and position[1]-102 <= self.y_pos and position[1]+102 >= self.y_pos):
            pygame.draw.rect(screen, self.color, (self.x_pos, self.y_pos,100,100), 1)
            self.lock = 1
        if self.lock == 1:
            pass
        else:
            if self.timer < pygame.time.get_ticks():
                self.timer += 1
                self.y_pos += 1
                pygame.draw.rect(screen, self.color, (self.x_pos, self.y_pos,100,100), 1)
            else:
                pygame.draw.rect(screen, self.color, (self.x_pos, self.y_pos,100,100), 1)









class Game():
    def __init__(self):
        self.mouse = 0
        self.objected = []



    def Events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.objected.append(spawned_object())




    def Update(self):
        screen.fill((0,0,0))
        for i in self.objected:
            for j in self.objected:
                if i != j:
                    i.Update([j.x_pos,j.y_pos])
        if len(self.objected) == 1:
            i.Update()
        pygame.display.flip()



game = Game()

while True:
    game.Events()
    game.Update()
    sleep(0.0001)
