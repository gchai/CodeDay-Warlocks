#powerups are just different update and draw methods which will pull from the method list at the bottom
import sys
sys.path.append('PowerUps/')
import pygame
import CSegment

def NONE(self):
   return
HPCONST = 10
   
class Powerup():
   def __init__(self, attrib = "time", pos = [0,0] , xframe = 10):
      '''attrib = str value. pos = position to be drawn. xframe = how many frames before updating image'''
      # attrib can be time, invin, hp, line, speed, jump
      self._type = attrib
      self._pos = pos
      self._img = []
      self.Frames = 0
      self.EXF = xframe
      self.imgnum = 0
      #collision lines are larger than sprite on purpose
      self.colliders = [CSegment.Segment((self._img[0].left-self._img[0].get_width()/2, self.y), (self._img[0].right+self._img[0].get_width()/2, self.y)), CSegment.Segment((self.x, self._img[0].top-self._img[0].get_height()/2), (self.x, self._img[0].bottom+self._img[0].get_height()/2))]
      #set _img array
      if attrib == "time":
         self._img.append(pygame.image.load('Time.png'))
      elif attrib == "invin":
         self._img.append(pygame.image.load('Invin1.png'))
         self._img.append(pygame.image.load('Invin2.png'))
      elif attrib == "hp":
         self._img.append(pygame.image.load('hp1.png'))
         self._img.append(pygame.image.load('hp2.png'))
      elif attrib == "line":
         self._img.append(pygame.image.load('Line1.png'))
         self._img.append(pygame.image.load('Line2.png'))
         self._img.append(pygame.image.load('Line3.png'))
      elif attrib == "speed":
         self._img.append(pygame.image.load('spd1.png'))
         self._img.append(pygame.image.load('spd2.png'))
      elif attrib == "jump":
         self._img.append(pygame.image.load('jmp1.png'))
         self._img.append(pygame.image.load('jmp2.png'))
         
   #update will return false if collision occured. this means it deletes itself
   #returns true if no collisions
   def update(self, players):
      self.Frames+=1
      #update imgnum and assign proper picture.
      if self.Frames >= self.EXF:
         self.Frames = 0
         self.imgnum += 1
         self.imgnum %= len(self._img)
         self.surf = self._img[self.imgnum ]
      for plyr in players:
         for seg in plyr.trail.Lines:
            #seg is now a segment
            if seg.collideswith(self.colliders[0]) or seg.collideswith(self.colliders[1]):
               #collision.
               self.GivePower(plyr)
               return False
      return True
         
   def GivePower(self, OBJ):
      if self._type == "time":
         OBJ.Power = TIME
      elif self._type == "hp":
         OBJ.Power = HP
      elif self._type == "invin":
         OBJ.Power = INVIN
      elif self._type == "line":
         OBJ.Power = LINE
      elif self._type == "speed":
         OBJ.Power = SPEED
      elif self._type == "jump":
         OBJ.Power = JUMP
      else:
         OBJ.Power = NONE
      return 
         
         
         
   def TIME(self, OBJ1):
      #destruction aspect
      if OBJ1.__PowerFrame >= 60 or OBJ1.__reset == True:
         OBJ1.__reset = False
         OBJ1.Power = NONE
         OBJ1.spMultiplier = 1.0
         OBJ1.__PowerFrame = 0
         return
      OBJ1.spMultiplier = 0.5
      OBJ1.__PowerFrame+=1
      return
      
   def JUMP(self, OBJ1):
      #destruction aspect
      if OBJ1.__PowerFrame >= 60 or OBJ1.__reset == True:
         OBJ1.__reset = False
         OBJ1.Power = NONE
         OBJ1.__invincibility = 60
         OBJ1.__PowerFrame = 0
         OBJ1.__DLINENEW = True
         return
      OBJ1.__invincibility = 60
      OBJ1.__PowerFrame+=1
      OBJ1.__DLINE = False
      OBJ1.__DLINENEW = False
      return  
      
   def SPEED(self, OBJ1):
      #destruction aspect
      if OBJ1.__PowerFrame >= 60 or OBJ1.__reset == True:
         OBJ1.__reset = False
         OBJ1.Power = NONE
         OBJ1.spMultiplier = 1.0
         OBJ1.__PowerFrame = 0
         return
      if OBJ1.__PowerFrame == 0:
         OBJ1.spMultiplier = 2.0
      OBJ1.__PowerFrame+=1
      return
      
   def HP(self,OBJ1):
      OBJ1.Power = NONE
      OBJ1.__PowerFrame = 0
      OBJ1.hp += HPCONST
      return
      
   def INVIN(self, OBJ1):
      OBJ1.__invincibility = 60
      #destruction aspect
      if OBJ1.__PowerFrame >= 60 or OBJ1.__reset == True:
         OBJ1.__reset = False
         OBJ1.Power = NONE
         OBJ1.__PowerFrame = 0
         return
      OBJ1.__PowerFrame+=1
      return
        
   def LINE(self, OBJ1):
      #destruction aspect
      if OBJ1.__PowerFrame >= 60 or OBJ1.__reset == True:
         OBJ1.__reset = False
         OBJ1.Power = NONE
         OBJ1.__PowerFrame = 0
         OBJ1.TrailLength = OBJ1.__TrailMem
         OBJ1.__TrailMem = 0
         return
      #begining aspect
      if OBJ1.__PowerFrame == 0:
         OBJ1.__TrailMem = OBJ1.TrailLength
      OBJ1.TrailLength = 3*OBJ1.__TrailMem/2 
      
