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



class cookie():
    def __init__(self):
        self.x = np.random.randint(10,700,1)
        self.y = 10
        self.image = pygame.image.load("cookie.jpg")
        self.image = pygame.transform.scale(self.image, (100, 100))

    def Update(self):
        self.y += 1
        screen.blit(self.image,(self.x, self.y))



class Game():
    def __init__(self):
        self.gold = 0
        self.cookies_on_screen = []
        self.shop_button = pygame.transform.scale(pygame.image.load("shop.png"), (150, 50))
        self.cookiechef_image = pygame.transform.scale(pygame.image.load("chef.png"), (50, 50))
        self.cookiechef_amount = 0
        self.shop_background = pygame.image.load("shop_template.png")
        self.menu = 0
        self.earning = 0
        self.shop_text = ''
        self.timer = 0
        self.timer2 = 0

    def Events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            x_pos = pygame.mouse.get_pos()[0]
            y_pos = pygame.mouse.get_pos()[1]
            
            if event.type == pygame.MOUSEBUTTONDOWN and self.menu == 0:
                if x_pos <= 150 and y_pos <= 140 and y_pos >= 90:
                    self.menu = 1
                cook = cookie()
                self.cookies_on_screen.append(cook)
                self.gold += 10

            if event.type == pygame.MOUSEBUTTONDOWN and self.menu == 1 and x_pos <= 404 and x_pos >= 267 and y_pos <= 218 and y_pos >= 127 and self.gold >= 500:
                self.gold -= 500
                self.timer = (pygame.time.get_ticks()+1000)
                self.shop_text = 'Bought "The cookie chef"'
                self.cookiechef_amount += 1
                self.earning += 50

            if event.type == pygame.MOUSEBUTTONDOWN and self.menu == 1:
                if x_pos <= 770 and x_pos >= 707 and y_pos <= 60 and y_pos >= 20:
                    self.menu = 0




    def Shop(self):
        if pygame.time.get_ticks() >= self.timer:
            self.shop_text = ''
        if pygame.time.get_ticks() >= self.timer2:
            self.timer2 += 1000
            self.gold += self.earning
        screen.fill((0,0,0))
        screen.blit(self.shop_background,(0, 0))
        textsurfacegold = win_text.render('%d Cookies'%self.gold, False, (100, 100, 100))
        screen.blit(textsurfacegold,(0,0))
        shop_response = win_text.render('%s'%self.shop_text, False, (100, 100, 100))
        screen.blit(shop_response,(280,250))
        pygame.display.flip()
        print(pygame.mouse.get_pos())



    def Update(self):
        if self.menu == 0:
            if pygame.time.get_ticks() > self.timer2 and self.earning > 0:
                self.timer2 += 1000
                self.gold += self.earning
                cook = cookie()
                self.cookies_on_screen.append(cook)

            screen.fill((0,0,0))
            for i in self.cookies_on_screen:
                if i.y >= 800:
                    self.cookies_on_screen.remove(i)
                i.Update()
            textsurfacegold = win_text.render('%d Cookies'%self.gold, False, (100, 100, 100))
            screen.blit(textsurfacegold,(0,30))
            screen.blit(self.shop_button,(0, 90))
            cookiechef_amount = win_text.render('%d'%self.cookiechef_amount, False, (100, 100, 100))
            screen.blit(cookiechef_amount,(50,150))
            screen.blit(self.cookiechef_image,(0, 150))
            pygame.display.flip()
        else:
            self.Shop()

        



        


game = Game()

while True:
    game.Events()
    game.Update()
    sleep(0.0001)






