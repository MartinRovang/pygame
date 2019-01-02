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


pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
win_text = pygame.font.SysFont('Comic Sans MS', 30)






class Player():

    def __init__(self):
        self.x = 50
        self.y = 700
        self.width = 100
        self.height = 40
        pygame.draw.rect(screen, (100,100,100),(self.x,self.y,self.width,self.height))    


    def Update(self):
        if pygame.mouse.get_pressed() == (1,0,0) and self.x < (width_screen- self.width):
            self.x += 0.9

        if pygame.mouse.get_pressed() == (0,0,1) and self.x > 0:
            self.x -= 0.9

        pygame.draw.rect(screen, (100,100,100),(self.x,self.y,self.width,self.height))



class box():

    def __init__(self):
        self.x = np.random.randint(50,800,1)
        self.y = 50
        self.width = 100
        self.height = 100
        self.won = 'False'
        self.image = pygame.image.load("gold.jpg")
        self.image = pygame.transform.scale(self.image, (self.width,self.height))
        screen.blit(self.image,(self.x,self.y))

    def Update(self):
        if self.won != 'False':
            screen.blit(self.image,(self.x,self.y))




class Ball():
    def __init__(self):
        self.x = 100
        self.y = 100
        self.Ball = pygame.image.load("kim.jpg")
        self.Ball = pygame.transform.scale(self.Ball, (30,30))
        self.vely = 1
        self.velx = 0.1
        self.time = pygame.time.get_ticks()

    def Update(self):

        if self.y <= 0:
            self.time = pygame.time.get_ticks()
            self.y = 5
            self.vely *= -1

        if self.x <= 0:
            self.x = 5
            self.time = pygame.time.get_ticks()
            self.velx *= -1

        if self.x >= (width_screen-30):
            self.x = (width_screen-35)
            self.time = pygame.time.get_ticks()
            self.velx *= -1

        #print(((pygame.time.get_ticks()-self.time)/1000))
        self.y += self.vely*((pygame.time.get_ticks()-self.time)/1000)
        self.x += self.velx*((pygame.time.get_ticks()-self.time)/1000)
        screen.blit(self.Ball,(self.x, self.y))

    


class Game():
    def __init__(self,content):
        self.players = 0
        self.content = content
        self.health = 100
        self.gold = 0
        self.timer = pygame.time.get_ticks()
        self.lock = 0
        self.current_col = 0
    
    def Events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

    def Update(self):
        ball = content[0]
        player = content[1]
        #if ball.x <= (player.x+player.width) and ball.y <= (player.y+player.height):
            #ball.vel += 0.5



        if ball.y >= (height_screen-30):
            ball.x = 100
            ball.y = 100
            ball.vely = 1
            ball.time = pygame.time.get_ticks()
            self.health -= 10
            self.lock = 0

        if ball.y <= 0:
           self.gold += 10



        if ball.y >= (player.y-player.height) and ball.y <= player.y and ball.x >= player.x and ball.x <= (player.x+player.width):
            ball.vely *= -1
            rand_x_1 = np.random.random(5)*0.10
            rand_x_2 = np.random.random(5)*0.10*(-1)
            rand = np.append(rand_x_1,rand_x_2)
            random_x = random.choice(rand)
            ball.velx += random_x

        if self.lock != 2:
            print('Active')
            boxx.won = 'True'
            self.lock = 2


        if ball.x >= boxx.x and ball.x <= (boxx.x + boxx.width) and ball.y >= (boxx.y-boxx.height) and ball.y <= boxx.y and boxx.won == 'True':
            self.gold += 500
            boxx.won = 'False'


        # if self.gold >= 30 and pygame.time.get_ticks() > self.timer+1000:
        #     self.current_col = (np.random.randint(60,200,1),np.random.randint(60,200,1),np.random.randint(60,200,1))
        #     self.lock = 1
        #     self.timer = pygame.time.get_ticks()

    
        if self.lock == 1:
            screen.fill(self.current_col)
        else:
            screen.fill((0,0,0))
            

        textsurface = win_text.render('%d Health'%self.health, False, (100, 100, 100))
        screen.blit(textsurface,(0,0))
        textsurfacegold = win_text.render('%d Gold'%self.gold, False, (100, 100, 100))
        screen.blit(textsurfacegold,(0,30))
        boxx.Update()
        ball.Update()
        player.Update()
        pygame.display.flip()

               



player1 = Player()
ball = Ball()
content = [ball,player1]
game = Game(content)
boxx = box()

while True:
    game.Events()
    game.Update()
    sleep(0.0001)






