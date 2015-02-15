#Large Blast animation
import pygame, sys, os
IMGDIR = ''
class Blast():
   def __init__(self, par, col = "b" ,size = [48,48],dirt = "./All/Tron2/Animation/Blast/"):	
      i = 1
      self.directory = dirt
      self.parsurf = par
      self.color = col
      self.img = []
      self.stopped = True
      self.pos = [-1,-1]
      self.imgnum = 0
      self.vector = [0,0]
      self.img.append(pygame.transform.scale(pygame.image.load( self.directory + '0.png'),(size[0],size[1])))
      #self.img.append(pygame.image.load( self.directory + '0.png'))
      while i < 5:
         self.img.append(pygame.transform.scale(pygame.image.load( self.directory + col + str(i)+'.png'),(size[0],size[1])))
         #self.img.append(pygame.image.load( self.directory + col + str(i)+ ".png"))
         i += 1
      self.size = [self.img[0].get_width(), self.img[0].get_height()]
      self.surf = self.img[0]


#begin starts the animation. you need to call update for it to continue 
   def begin(self,start = -1, vect = [0, 0]):
      self.surf = self.img[0]
      self.imgnum = 0
      self.stopped = False
      self.vector = vect

#changes colors b,g,o,r,p
   def changeColor(self, col = "b"):
      i = 1
      self.color = col
      while i < 5:
         self.img.pop(1)
         self.img.append(pygame.transform.scale(pygame.image.load( self.directory + col + str(i)+'.png'),(self.size[0],self.size[1])))
         #self.img.append(pygame.image.load( self.directory + col + str(i)+ ".png"))
         i += 1

   def changeVector(self, vect):
      self.vector = vect
	
#call update every frame to change showing.
   def update(self,state = -1):
      if self.stopped == True:
         self.surf = self.img[0]
         self.Draw(self.parsurf)
         return
      elif state != -1:
         self.surf = self.img[state] #fix this with self.imgnum
      elif self.imgnum == 4:
         self.surf = self.img[1]
         self.imgnum = 1
      else:
         self.imgnum = (self.imgnum % 4) + 1
         self.surf = self.img[self.imgnum]
         self.move(self.vector)
      self.Draw(self.parsurf)

#end will stop all processes for the object. It makes the object transparent.
   def end(self):
      self.surf = self.img[0]
      self.imgnum = 0
      self.stopped = True
      self.Draw(self.parsurf)
	
   def move(self, vect):
      self.pos[0]+= vect[0]
      self.pos[1]+= vect[1]

   def moveTo(self, vect):
      self.pos[0] = vect[0]
      self.pos[1] = vect[1]

#call Draw in the draw step after update
   def Draw(self, surface):
      surface.blit(self.surf, (self.pos[0]-self.size[0]/2, self.pos[1]-self.size[1]/2))
	
