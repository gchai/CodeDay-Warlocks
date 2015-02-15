'''import sys, random
import pygame
from pygame.locals import *
pygame.init()
import GenerateBGI
sys.path.append( 'Health/' )
import health
sys.path.append( 'ColorMod/' )
import ColorMod
sys.path.append('PowerUps/')
sys.path.append('Animation/Foxreflector/')
import CTrail, CSegment, health, ColorMod, Pup, CAI, ClassReflector, CLightBike'''
import CGame
CGame.NUMHUM = (int(raw_input("How many human players?(0-3):"))%4)
CGame.NUMAI = (int(raw_input("How many Ai players?(0-9):"))%10)
CGame.main()
