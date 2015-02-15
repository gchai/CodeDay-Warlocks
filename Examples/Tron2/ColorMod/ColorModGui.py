# ColorMod Gui
#
#
#
#
#

import pygame, sys
import ColorMod
import Slider
#screen = pygame.display.set_mode((600, 200))
Rsli = Slider.slider(255, [0,255])
Rsli.SwapColor((255,0,0))
Gsli = Slider.slider(255, [0,255])
Gsli.SwapColor((0, 255, 0))
Bsli = Slider.slider(255, [0,255])
Bsli.SwapColor((0,0,255))
Nsli = Slider.slider(255, [0,255])
Rsl = (10,10)
Gsl = (10, 10+Rsl[1]+Rsli.GetSize()[1])
Bsl = (10, 10+Gsl[1]+Gsli.GetSize()[1])
Nsl = (10, 10+Bsl[1]+Bsli.GetSize()[1])
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`
def GetFilter ( path, pimg, col):
   '''
   path: path to the images.
   pimg: list of images to filter.
   col: the color to filter towards.
   '''
   img = []
   for i in pimg:
      img.append(pygame.image.load(path + i + ".png"))
   for i in range(len(pimg)):
      img[i] = ColorMod.Filter(img[i], col ,255)
   return img
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`
def GetIMG(screen, path, pimg, ttl ):
   '''
   screen: the surface object to draw upon.
   path: the path from your caller to find an image
   pimg: list of image names to load
   ttl: the title to display
   '''
   TitlePos = (Nsl[0], Nsl[1]+10+Nsli.GetSize()[1])
   Title = pygame.font.Font("fonts/T.ttf", int(screen.get_width() / 30))
   TITLE = Title.render( (ttl), False, (255,155,155))
   sys.path.append( path )
   #img is the original list and will never be modified. ever.
   img = []
   #img.append(pygame.transform.scale(pimg,(108,108)))
   for i in pimg:
      img.append(pygame.image.load(path + i + ".png"))
   #img2 however is a copy of img[], and will hold all modified images.
   img2 = []
   for i in pimg:
      img2.append(pygame.image.load(path + i + ".png"))
   #img.append(pygame.transform.scale(pimg,(24,24)))
   #imgcol[] holds the colorize color for the respective img2[] image. this is used for producing line color.
   imgcol = []
   for i in range(len(img)):
      imgcol.append((255,255,255))
   clock = pygame.time.Clock()
   play = 1
   click = 0
   ind = 0
   doDraw = False
   while play:
      screen.fill((0,0,0))
      for e in pygame.event.get():
         if e.type == pygame.QUIT:
            return None
         elif e.type == pygame.MOUSEBUTTONDOWN:
            click = 1
         elif e.type == pygame.MOUSEMOTION and click:
            x = e.pos[0]
            if x > Rsl[0] and x < Rsl[0] + Rsli.GetSize()[0]:
                    #within x ranges for sliders
                    y = e.pos[1]
                    if y > Rsl[1] and y < Rsl[1]+Rsli.GetSize()[1]:
                       Rsli.ParseEvent(x - Rsl[0], "click")
                    if y > Gsl[1] and y < Gsl[1]+Gsli.GetSize()[1]:
                       Gsli.ParseEvent(x - Gsl[0], "click")
                    if y > Bsl[1] and y < Bsl[1]+Bsli.GetSize()[1]:
                       Bsli.ParseEvent(x - Bsl[0], "click")
                    if y > Nsl[1] and y < Nsl[1]+Nsli.GetSize()[1]:
                       Nsli.ParseEvent(x - Nsl[0], "click")
         if e.type == pygame.KEYDOWN:
            if pygame.key.get_pressed()[pygame.K_ESCAPE] or pygame.key.get_pressed()[pygame.K_RETURN]:
               r = (imgcol[0][0]+imgcol[1][0]+imgcol[2][0])/3
               g = (imgcol[0][1]+imgcol[1][1]+imgcol[2][1])/3
               b = (imgcol[0][2]+imgcol[1][2]+imgcol[2][2])/3
               img2.append([r,g,b])
               return img2
            if pygame.key.get_pressed()[pygame.K_w]:
               ind = ind + 1
               ind = ind % len(img)
               Rsli.value = imgcol[ind][0]
               Gsli.value = imgcol[ind][1]
               Bsli.value = imgcol[ind][2]
            elif pygame.key.get_pressed()[pygame.K_q]:
               ind = ind -1
               if ind <0:
                  ind = len(img)-1
               Rsli.value = imgcol[ind][0]
               Gsli.value = imgcol[ind][1]
               Bsli.value = imgcol[ind][2]
            elif pygame.key.get_pressed()[pygame.K_SPACE]:
               doDraw = True
         if e.type == pygame.MOUSEBUTTONUP:
            click = 0
            x = e.pos[0]
            if x > Rsl[0] and x < Rsl[0] + Rsli.GetSize()[0]:
               #within x ranges for sliders
               y = e.pos[1]
               if y > Rsl[1] and y < Rsl[1]+Rsli.GetSize()[1]:
                  Rsli.ParseEvent(x - Rsl[0], "click")
               if y > Gsl[1] and y < Gsl[1]+Gsli.GetSize()[1]:
                  Gsli.ParseEvent(x - Gsl[0], "click")
               if y > Bsl[1] and y < Bsl[1]+Bsli.GetSize()[1]:
                  Bsli.ParseEvent(x - Bsl[0], "click")
               if y > Nsl[1] and y < Nsl[1]+Nsli.GetSize()[1]:
                  Nsli.ParseEvent(x - Nsl[0], "click")
      red = Rsli.GetValue()
      grn = Gsli.GetValue()
      blu = Bsli.GetValue()
      Nsli.SwapColor((red, grn, blu))
      if doDraw:
         imgcol[ind] = (red,grn,blu)
         img2[ind] = ColorMod.Filter(img[ind],(red, grn, blu),255)
         doDraw = False
      for im in img2:
         screen.blit(im,(10 + Rsl[0] + Rsli.GetSize()[0], Rsl[1]))  
      Rsli.Draw(screen, Rsl)
      Gsli.Draw(screen, Gsl)
      Bsli.Draw(screen, Bsl)
      Nsli.Draw(screen, Nsl)  
      screen.blit(TITLE, TitlePos)
      pygame.display.update()
      clock.tick(30)
#lol = GetIMG(screen, "","")
#screen.fill((0,0,0))
#for i in range(len(lol)):
#   screen.blit(lol[i],(12*(2*i + 3),12)) 
#pygame.display.update()
#import time
#time.sleep(1.5)
