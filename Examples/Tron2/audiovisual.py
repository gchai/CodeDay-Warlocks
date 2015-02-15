
import pygame
import sys, math
import ArrayLoad
sys.path.append( 'Animation/Blast/' )
sys.path.append( 'ColorMod/' )
sys.path.append( 'Animation/Foxreflector/' )
import ClassReflector, ClassLargeBlast
import ColorModGui
location = 'sounds/'
name = 'Surge'
pygame.init()
Screen = pygame.display.set_mode((360, 240), pygame.FULLSCREEN | pygame.DOUBLEBUF)
Screen.fill((255,255,255))
MyFont = pygame.font.Font(pygame.font.get_default_font(), 14)
pygame.mixer.music.load(location + name + '.mp3')
MyClock = pygame.time.Clock()
title = MyFont.render("audiovisual effect booth", False, (0,0,0))
quit = 0
frame = 0
myBase = ArrayLoad.ReturnBase(location + name + 'bass')
myBase2 = ArrayLoad.ReturnBase(location + name + 'melody')
myBase3 = ArrayLoad.ReturnBase(location + name + 'specs')
myBase4 = ArrayLoad.ReturnBase(location + name + 'drop')
effect = ClassReflector.Reflector(Screen, True, (80,255,255), (48,48), "Animation/Foxreflector/")

#effect2 = []
effect2 = ClassReflector.Reflector(Screen, True, (255,255,80),(48,48), "Animation/Foxreflector/")
effect3 = ClassReflector.Reflector(Screen, True, (255,80,255),(48,48), "Animation/Foxreflector/")
effect.moveTo([Screen.get_width()/2, Screen.get_height()/4])
effect2.moveTo([Screen.get_width()/2, Screen.get_height()/2])
effect3.moveTo([Screen.get_width()/2, Screen.get_height()*3/4])
counter = 15
Sx = Screen.get_width()/2
Sy = Screen.get_height()/2
backCol = (0,0,0)
print myBase
def update(backCol):
		lol = pygame.mixer.music.get_pos()
		#if lol% 1000 > 950:
		#   effect.changeColor((lol/61 % 255,lol/51 %255,lol/41 %255))
		#   effect3.changeColor((255-(lol/61 % 255),255-(lol/51 %255),255-(lol/41 %255)))
		Screen.fill(backCol)
		#if (lol % 100) > 49:
		#		effect.changeColor("r")
		#		effect2.changeColor("b")
		#		effect3.changeColor("r")
		#else:
		#		effect.changeColor("b")
		#		effect2.changeColor("r")
		#		effect3.changeColor("b")
		if lol > myBase[0][0]:
				if effect.stopped:
						x = int(lol%11) - 5
						y = int(myBase[0][1])%11 - 5
						#effect.velocity(x,y)
						
						effect.begin()
				else:
						effect.update()
		if lol > myBase[0][1]:
				effect.end()
				myBase.pop(0)
		lol = pygame.mixer.music.get_pos()
		if lol > myBase2[0][0]:
				'''if flg == False:
						effect2.append( ClassLargeBlast.Blast( screen, "b"))
						effect2[-1].moveTo([Sx, Sy])
						effect2[-1].begin([((lol%21)%7*3), ((lol%53)%5*6)])
						flg = True
				for num in range(len(effect2)-1):
						effect2[num].update()
						ix = effect2[num].pos[0]
						iy = effect2[num].pos[1]
						if ix > (100+Sx) or ix < (Sx-100) or iy < (Sy-100) or iy > (Sy+100):
								effect2.pop(num)
				'''
				if effect2.stopped:
						effect2.begin()
				else:
						effect2.update()
		if lol > myBase2[0][1]:
				effect2.end()
				myBase2.pop(0)
				#flg = False
		lol = pygame.mixer.music.get_pos()
		if lol > myBase3[0][0]:
				if effect3.stopped:
						x = int(lol%11) - 5
						y = int(myBase3[0][1])%11 - 5
						#effect3.velocity(x, y)						
						effect3.begin()
				else:
						effect3.update()
		if lol > myBase3[0][1]:
				effect3.end()
				myBase3.pop(0)
		
		effect.Draw(Screen)

		'''for i in effect2:
				i.Draw(Screen) '''
		effect2.Draw(Screen)
		effect3.Draw(Screen)
		pygame.display.flip()

#def Rotate(dist = Screen.get_height()/4, ef1 = effect, ef2 = effect2, ef3 = effect3, speed = 2, reverse = False):
#	x1 = ef2.pos[0] - ef1.pos[0]
#	y1 = ef2.pos[1] - ef1.pos[1]
#	x3 = ef2.pos[0] - ef3.pos[0]
#	y3 = ef3.pos[1] - ef3.pos[1]
#
#	if y1 = 0 and x1 <0:
#		y1 = asin(
		

flag = True
change = False
pygame.mixer.music.play()
while quit == 0:
		lol = pygame.mixer.music.get_pos()
		if lol > myBase4[0][0]:
				backCol = ((lol/(230*(counter+1)))%255,(lol/(170*(counter+1)))%255,(lol/(370*(counter+1)))%255)
				counter -= 1
				if counter == 0:
						myBase4.pop(0)
						counter = 15
		else:
				backCol = (0,0,0)
		update(backCol)
		for e in pygame.event.get():
				#HitTime = pygame.mixer.music.get_pos()
				if e.type == pygame.KEYDOWN and e.scancode == 9:
						quit = 1
		#Screen.blit(title, (Screen.get_width()/2- title.get_width()/2,Screen.get_height()/2 - title.get_height()/2)) 
		
		#frame = frame +1
		MyClock.tick(80)
Screen.fill((255,255,255))
title = MyFont.render("you chose to quit.", False, (0,0,0))
Screen.blit(title, (Screen.get_width()/2- title.get_width()/2,Screen.get_height()/2 - title.get_height()/2)) 
pygame.display.update()
pygame.time.wait(500)
pygame.quit()
sys.exit()
