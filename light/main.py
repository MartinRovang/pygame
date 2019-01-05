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





class Game():
    def __init__(self):
        self.mouse = 0



    def Events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()



    def Update(self):
        x_pos = pygame.mouse.get_pos()[0]
        y_pos = pygame.mouse.get_pos()[1]
        r = 500
        screen.fill((0,0,0))
        print(pygame.mouse.get_pos())
        # pygame.draw.circle(screen, (255,64,64), (x_pos, y_pos),5)
        pygame.draw.rect(screen, (100, 100 ,100), (500,200,150,150), 1)

        for theta in np.linspace(0,2*np.pi, 500):
            if (x_pos + r*np.cos(theta)) >= 500 and (y_pos + r*np.sin(theta)) <= 200 or (y_pos + r*np.sin(theta)) <= 350 and (x_pos + r*np.cos(theta)) >= 500:
                continue
                # dx = 0
                # dy = 0
                # while (x_pos + dx*np.cos(theta)) <= 500 and (y_pos + dy*np.sin(theta)) >= 200 or (x_pos + dx*np.cos(theta)) >= 500 and (y_pos + dy*np.sin(theta)) <= 350:
                #     dx += 1
                #     dy += 1
                # pygame.draw.line(screen, (248,248,255), (x_pos,y_pos), (x_pos+dx*np.cos(theta) ,y_pos+dy*np.sin(theta)), 1)

            else:
                pygame.draw.line(screen, (248,248,255), (x_pos,y_pos), (x_pos+r*np.cos(theta) ,y_pos+r*np.sin(theta)), 1)
        pygame.display.flip()



game = Game()

while True:
    game.Events()
    game.Update()
    sleep(0.0001)
