import pygame
from pygame.locals import *
import random
#initialize variables

size=width,height=(800,800)
Space_w=int(width/5)
startind=False
speed=10

pygame.init()
run=True

#set windoe size
screen=pygame.display.set_mode(size)

pygame.display.set_caption("space game")
#load image
spacebg=pygame.image.load("location for the file")
spacebg_loc=spacebg.get_rect()

title=pygame.image.load("game_file/locatrion for the file")
title_loc=title.get_rect()
title_loc.center=width/2,height/2

gameestart=pygame.image.load("game_file/locatrion for the file")
gameestart_loc=gameestart.get_rect()
gameestart_loc.center=width/2,height/2

spaceship=pygame.image.load("game_file/locatrion for the file")
spaceship_loc=spaceship.get_rect()
spaceship_loc.center=Space_w,height*.8

meteor=pygame.image.load("game_file/locatrion for the file")
meteor_loc=meteor.get_rect()
meteor_loc.center=Space_w,height*.1

gameover=pygame.image.load("game_file/locatrion for the file")
gameover_loc=gameover.get_rect()
gameover_loc.center=width/2,height/2

#apply changes
screen.blit(spacebg,spacebg_loc)
screen.blit(gameestart,spacebg_loc)
screen.blit(spaceship,spacebg_loc)
screen.blit(meteor,meteor_loc)
screen.blit(title,title_loc)
pygame.display.update()

#start game sequence
while run:
    for event in pygame.event.get():
        if event.type == quit:
            run=False
        if event.type==KEYDOWN:
            if event.key==K_s:
                startind=True 
        while startind:
            for event in pygame.get():
                if event.type==KEYDOWN:
                    if event.key in {K_a,K_LEFT}:
                        spaceship_loc=spaceship_loc.move(Space_w,0)
                    if event.key in {K_d,K_RIGHT}:
                        spaceship_loc=spaceship_loc.move(Space_w,0)
                if event.type == quit:
                    run=False
                    startind=False
            meteor_loc[1] = meteor_loc[1]+speed
            if meteor_loc>height:
                meteor_loc.center=Space_w*random.randint(1,5)-100

            screen.blit(spacebg,spacebg_loc)
            screen.blit(gameestart,spacebg_loc)
            screen.blit(spaceship,spacebg_loc)
            screen.blit(meteor,meteor_loc)
            screen.blit(title,title_loc)
#game over logic
            if spaceship_loc[0]==meteor_loc[0] and spaceship_loc[1]<meteor_loc[1]+175 and spaceship_loc[1]>meteor_loc[1]+175 and spaceship_loc[1]>meteor_loc[1]:
                screen.blit(gameover,gameover_loc)
                pygame.display.update()
                startind=False
            pygame.display.update()
#quit game
pygame.quit()