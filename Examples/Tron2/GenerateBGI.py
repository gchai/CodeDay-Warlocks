#Generate BGI
#
#the goal is to generate surfaces that have a Backgroun image kind of use. 
#All backgrounds are expected to be generated before play. don't even try to do this while in the middle of action
import pygame, sys

def GenerateTron(res , tile_spacing, color = (0,0,150)):
   '''res is a point with surface width and height. tile_spacing is an int
   '''
   newSurf = pygame.Surface(res)
   newSurf.fill((10,10,10))
   XNum = res[0]/tile_spacing
   XOffset = (res[0] % tile_spacing)/2
   YNum = res[1]/ tile_spacing
   YOffset = (res[1] % tile_spacing)/2
   # now will come the line generation.
   for i in range(XNum+1):
      pygame.draw.line(newSurf, (color[0]/4,color[1]/4,color[2]/4), (i*tile_spacing+XOffset, 0), (i*tile_spacing + XOffset,res[1]),3)
      pygame.draw.line(newSurf, color, (i*tile_spacing+XOffset, 0), (i*tile_spacing + XOffset,res[1]))
   for i in range(YNum+1):
      pygame.draw.line(newSurf, (color[0]/4,color[1]/4,color[2]/4), (0,i*tile_spacing+YOffset), (res[0],i*tile_spacing + YOffset),3)
      pygame.draw.line(newSurf, color, (0,i*tile_spacing+YOffset), (res[0],i*tile_spacing + YOffset))
   return newSurf
