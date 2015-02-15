# Button
import pygame
from pygame.locals import *
import ColorMod
pygame.init()
class slider():
	def __init__(self,sizep = 100, endsp = (0,255), debug = False):
		self.color = (255,255,255)
		self.loc = None
		self.debug_on = debug
		self.length = sizep
		self.ends = endsp
		self.conversionratio = (endsp[1]-endsp[0])/sizep #each pixel covers this amount of value
		self.value  = 0 #the true value it holds, no the position of the slider
		tmp = pygame.image.load("slide.png")
		self.slider_img = pygame.Surface((self.length,tmp.get_height()))
		self.select_img = pygame.image.load("select.png")
		self.SwapColor((200,10,10))
		
	
	def SwapColor(self, col = (255,0,0)):
		'''acceptable values are a 3d vector less than 255'''
		x = 0
		self.color = col
		tmp = pygame.image.load("slide.png")
		tmp = ColorMod.Colorize(tmp,col, 255)
		while x < self.slider_img.get_width():
			self.slider_img.blit(tmp, (x,0))
			x+= tmp.get_width()/2
		self.select_img = pygame.image.load("select.png")
		self.select_img = ColorMod.Colorize(self.select_img,col)
		tmp = pygame.image.load("selectmask.png")
		self.select_img.blit(tmp, (0,0))
			
	def ParseEvent(self, dist, etype = "click"):
		'''enable the slider to handle it's own events'''
 		if etype == "click":
			self.value = dist* self.conversionratio
		if self.debug_on:
			print "value: "+dist
			print "self.value:" + self.value

	def Draw(self, parsurf, loc):
		'''draw the element on parsurf at the given location'''
		parsurf.blit(self.slider_img, (loc[0], loc[1] + self.select_img.get_height()))
		x = self.value / self.conversionratio
		parsurf.blit(self.select_img, ( loc[0] + x- self.select_img.get_width()/2, loc[1]))
		if self.debug_on:
			print self.slider_img
			print self.select_img
		
	def GetSize(self):
		return (self.slider_img.get_width(), self.select_img.get_height() + self.slider_img.get_height())
	def GetValue(self):
		return self.value
	def GetColor(self):
		return self.color
