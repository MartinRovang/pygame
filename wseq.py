from sys import exit
from os import environ
import pygame
from time import sleep, localtime

SCREENSIZE = (640, 480)

environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
screen = pygame.display.set_mode(SCREENSIZE)


pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
win_text = pygame.font.SysFont('Comic Sans MS', 30)






class Player():

    def __init__(self):
        self.x = 50
        self.y = 250
        self.width = 100
        self.height = 40
        screen.fill((0,0,0))
        pygame.draw.rect(screen, (100,100,100),(self.x,self.y,self.width,self.height))
        pygame.display.flip()        


    def Update(self):
        if pygame.mouse.get_pressed() == (1,0,0) and self.x < (640 - self.width):
            self.x += 1

        if pygame.mouse.get_pressed() == (0,0,1) and self.x > 0:
            self.x -= 1

        pygame.draw.rect(screen, (100,100,100),(self.x,self.y,self.width,self.height))




class Ball():
    def __init__(self):
        self.x = 100
        self.y = 100
        self.Ball = pygame.image.load("ball.jpg")
        self.Ball = pygame.transform.scale(self.Ball, (30,30))
        self.vel = -0.1
        self.g = 0.2
        self.time = pygame.time.get_ticks()
        self.loss = 0

    def Update(self):

        if self.y >= (480-30):
            self.x = 100
            self.y = 100
            self.vel = -0.1
            self.time = pygame.time.get_ticks()
            self.loss += 1

        if self.y <= 0:
            self.vel += 0.1
        print(pygame.time.get_ticks()-self.time)
        #print(((pygame.time.get_ticks()-self.time)/1000))
        self.y += (1/2)*self.g*((pygame.time.get_ticks()-self.time)/1000)**2 + self.vel*((pygame.time.get_ticks()-self.time)/1000)
        screen.blit(self.Ball,(self.x, self.y))

    


class Game():
    def __init__(self,content):
        self.players = 0
        self.content = content
    
    def Events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

    def Update(self):
        screen.fill((0,0,0))
        ball = content[0]
        player = content[1]
        #if ball.x <= (player.x+player.width) and ball.y <= (player.y+player.height):
            #ball.vel += 0.5


        if ball.y >= (player.y-player.height) and ball.x >= player.x and ball.x <= (player.x+player.width):
            ball.vel += -0.1

        
        textsurface = win_text.render('%d loss points'%ball.loss, False, (100, 100, 100))
        screen.blit(textsurface,(0,0))
        ball.Update()
        player.Update()
        pygame.display.flip()

               



player1 = Player()
ball = Ball()
content = [ball,player1]
game = Game(content)

while True:
    game.Events()
    game.Update()
    sleep(0.0001)






