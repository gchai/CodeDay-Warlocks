#Health bar script
import pygame, sys
from pygame.locals import *

class HealthBar():
    def __init__(self, max_bar_num = 5, order = ['g','y','r'], hp = 3):
        #__imglist holds an array of images
        self.__imglist = []
        self.__max = max_bar_num
        for i in range(len(order)):
            self.__imglist.append(pygame.image.load('Health/'+order[i]+'.png'))
            #basically set the images into imglist
        self.__currentHP = hp
        
    def SetHP(self,newHP):
        self.__currentHP = newHP
    def GetHP(self):
        return self.__currentHP
    def GetMax(self):
        return self.__max
    def Draw(self,surf, loc):
        #more health than is to be drawn or perfect health
        if self.__currentHP <= 0:
            return False;
        elif self.__currentHP >= self.__max:
            #draw everything with last image
            for i in range(self.__max):
                img = self.__imglist[0]
                surf.blit(img, (loc[0] +img.get_width()*i, loc[1])) 
        else:
            #draw everything with last image
            for i in range(self.__currentHP):
                img = self.__imglist[-self.__currentHP]
                surf.blit(img, (loc[0] +img.get_width()*i, loc[1]))
