#Fox Reflector animation
import pygame, sys, os
sys.path.append( 'Animation/Foxreflector/' )
import ColorModGui



class Reflector():
   def __init__(self, par, loopOnFinish = True, col = (255,100,100) ,size = [48,48] ,dirt= "Animation/Foxreflector/"):
      ''' par = the default parent surface to draw to. loopOnFinish
      '''
      self.img = ColorModGui.GetFilter(dirt, ["0","1","2","3","4","5","6","7","8","9","10","11"], col)	
      i = 0
      self.directory = dirt
      self.loop = loopOnFinish
      self.parsurf = par
      self.color = col
      self.stopped = True
      #self.pos is the position on the screen where the Reflector will draw
      self.pos = [-1,-1]
      #
      self.imgnum = 0
		#self.img.append(pygame.image.load( self.directory + '0.png'))
		#self.img.append(pygame.transform.scale(pygame.image.load( self.directory + '0.png'),(size[0],size[1])))
      while i < 12:
         #self.img.append(pygame.image.load( self.directory + col + str(i)+ ".png"))
         self.img[i] = pygame.transform.scale(self.img[i],(size[0],size[1]))
         i += 1
      self.size = [self.img[0].get_width(), self.img[0].get_height()]
      self.surf = self.img[0]


#begin starts the animation. you need to call update for it to continue 
   def begin(self,start = -1):
      self.surf = self.img[0]
      self.imgnum = 0
      self.stopped = False
#changes colors
   def changeColor(self, col = (255,100,100)):
      self.img = ColorModGui.GetFilter (self.directory, ["0","1","2","3","4","5","6","7","8","9","10","11"], col)	
      i = 0
      self.color = col
      while i < 12:
         self.img[i] = pygame.transform.scale(self.img[i],self.size)
         #self.img.append(pygame.image.load( self.directory + col + str(i)+ ".png"))
         #self.img.append(pygame.transform.scale(pygame.image.load( self.directory + col + str(i)+'.png'),(self.size[0],self.size[1])))
         i += 1
   #call update every frame to change showing.
   def update(self,state = -1):
      if self.stopped == True:
         self.surf = self.img[0]
         return
      elif state != -1:
         self.surf = self.img[state] #fix this with self.imgnum
      elif self.imgnum == 11:
         if self.loop:
            self.surf = self.img[7]
            self.imgnum = 7
         else:
            self.surf = self.img[0]
      else:
         self.imgnum += 1
         self.imgnum = self.imgnum % 12
         self.surf = self.img[self.imgnum]
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
      
   #def moveTo(self, x, y):
   #   self.pos[0] = x
   #   self.pos[1] = y
#call Draw in the draw step after update
   def Draw(self, surface):
      '''provide a surface to draw to. Currently only supports drawing to topleft.'''
      if surface == None:
         return
      surface.blit(self.surf, (self.pos[0]-self.size[0]/2, self.pos[1]-self.size[1]/2))
