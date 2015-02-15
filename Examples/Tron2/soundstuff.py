# just going to test audio handles

import pygame
import sys
location = 'sounds/'
name = 'Vim'
pygame.init()
Screen = pygame.display.set_mode((480, 320))
Screen.fill((255,255,255))
MyFont = pygame.font.Font(pygame.font.get_default_font(), 14)
pygame.mixer.music.load(location + name + '.mp3')
MyClock = pygame.time.Clock()
title = MyFont.render("audiovisual effect booth", False, (0,0,0))
quit = 0
frame = 0
# q
#bass = open(location + name + 'bass', 'w') 
# w
#melody = open(location + name + 'melody', 'w')
# e
#special = open(location + name + 'specs', 'w')
# r
drop = open(location + name + 'drop', 'w')
pygame.mixer.music.play()
offset = 0
#q,w,e,r,t,y = 24,25,26,27,28,29
while quit == 0:
   Screen.fill((255,255,255))
   Screen.blit(title, (Screen.get_width()/2- title.get_width()/2,Screen.get_height()/2 - title.get_height()/2)) 
   pygame.display.update()
   frame = frame +1
   HitTime = pygame.mixer.music.get_pos() - offset
   for e in pygame.event.get():
      if e.type == pygame.KEYDOWN:
         if e.scancode == 24: 
            bass.write(str(HitTime) + " ")
         if e.scancode == 25:
            melody.write(str(HitTime) + " ")
         if e.scancode == 26:
            special.write(str(HitTime) + " ")
         if e.scancode == 27:
            drop.write(str(HitTime) + " ")
         elif e.scancode == 9:
            quit = 1
         elif e.scancode == 33:
            offset = 1
         else:
            print e.scancode
      if e.type == pygame.KEYUP:
         if e.scancode == 24:
            bass.write(str(HitTime) + "\n")
         if e.scancode == 25:
            melody.write(str(HitTime) + "\n")
         if e.scancode == 26:
            special.write(str(HitTime) + "\n")
         if e.scancode == 27:
            drop.write(str(HitTime) + "\n")
   MyClock.tick(60)
Screen.fill((255,255,255))
title = MyFont.render("you chose to quit.", False, (0,0,0))
Screen.blit(title, (Screen.get_width()/2- title.get_width()/2,Screen.get_height()/2 - title.get_height()/2)) 
pygame.display.update()
pygame.time.wait(300)
pygame.quit()
sys.exit()
