#Zero Spark animation
import pygame, sys, os
class Firework():
	def __init__(self, par, mod = '2', directory = "./All/Tron2/Animation/firework/"):	
		i = 0
		self.directory = directory
		self.parsurf = par
		self.img = []
		self.stopped = True
		self.pos = [-1,-1]
		self.vel = [0,0]
		self.imgnum = 0
		while i < 10:
			self.img.append(pygame.image.load( self.directory + mod + str(i)+ ".png"))
			i += 1
		self.size = [48,48]
		self.surf = self.img[0]


#begin starts the animation. you need to call update for it to continue 
	def begin(self,start = -1):
		self.surf = self.img[1]
		self.imgnum = 1
		self.stopped = False
	def changeMod(self, new):
		new = str(new)
		i = 0
		self.img = []
		while i < 10:
			self.img.append(pygame.image.load( self.directory + new + str(i)+ ".png"))
			i += 1
	def velocity(self, x, y):
		self.vel = [x , y]
#call update every frame to change showing.
	def update(self,state = -1):
		if self.imgnum == 0:
			self.surf = self.img[0]
			self.imgnum = 0
			return
		elif state != -1:
			self.surf = self.img[state] #fix this with self.imgnum
		elif self.imgnum == 9:
			self.surf = self.img[0]
			self.imgnum = 0
			self.end()
		else:
			self.imgnum += 1
			self.imgnum = self.imgnum % 10
			self.surf = self.img[self.imgnum]
		print self.imgnum
		self.Draw(self.parsurf)

#end will stop all processes for the object. It makes the object transparent.
	def end(self):
		self.surf = self.img[0]
		self.imgnum = 0
		self.stopped = True
		self.vel = [0,0]
		
		

	def move(self, x, y):
		self.pos[0]+= x
		self.pos[1]+= y

	def moveTo(self, x, y):
		self.pos[0] = x
		self.pos[1] = y


#call Draw in the draw step after update
	def Draw(self, surface):
		surface.blit(self.surf, (self.pos[0]-self.size[0]/2 + self.vel[0]*self.imgnum, self.pos[1]-self.size[1]/2 + self.vel[1]*self.imgnum))
		
