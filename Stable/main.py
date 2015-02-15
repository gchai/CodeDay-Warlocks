# Tiles/Mapping: http://qq.readthedocs.org/en/latest/tiles.html
# Installing Pygame: http://www.frihost.com/forums/vt-160879.html

import os, sys
import pygame

pygame.init()
surface = pygame.display.set_mode((1024,768))

from pygame.locals import *
from spritesheet import *
from sprite_strip_anim import *
from strips import *

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sounds disabled'

class Human(pygame.sprite.Sprite):
	def __init__(self, startx, starty):
		pygame.sprite.Sprite.__init__(self)

		self.x = startx
		self.y = starty

		self.currentSpritesheet = human_idle_down_strips

		self.x_dist = 12
		self.y_dist = 12
		self.x_momentum = 0
		self.x_momentumInc = 2
		self.x_momentumDec = 1.5
		self.x_momentumDecay = .5
		self.y_momentum = 0
		self.y_momentumInc = 2
		self.y_momentumDec = 1.5
		self.y_momentumDecay = .5

	def move(self, keylist, prevkey):
		xMove = 0;
		yMove = 0;

		if keylist[K_UP]:
			self.y += -self.y_dist
			self.y_momentum += self.y_momentumInc
			self.y += -self.y_momentum
			self.y_momentum -= self.y_momentumDec
			if prevkey != K_UP:
				self.currentSpritesheet = human_walking_up_strips
		if keylist[K_DOWN]:
			self.y += self.y_dist
			self.y_momentum += -self.y_momentumInc
			self.y += -self.y_momentum
			self.y_momentum -= -self.y_momentumDec
			if prevkey != K_DOWN:
				self.currentSpritesheet = human_walking_down_strips
		if keylist[K_RIGHT]:
			self.x += self.x_dist
			self.x_momentum += self.x_momentumInc
			self.x += self.x_momentum
			self.x_momentum -= self.x_momentumDec
			if prevkey != K_RIGHT:
				self.currentSpritesheet = human_walking_right_strips
		if keylist[K_LEFT]:
			self.x += -self.x_dist
			self.x_momentum += -self.x_momentumInc
			self.x += self.x_momentum
			self.x_momentum -= -self.x_momentumDec
			if prevkey != K_LEFT:
				self.currentSpritesheet = human_walking_left_strips
		return self.currentSpritesheet

	def stop(self, key, prevkey):
		if key == K_UP:
			self.currentSpritesheet = human_idle_up_strips
		elif key == K_DOWN:
			self.currentSpritesheet = human_idle_down_strips
		elif key == K_RIGHT:
			self.currentSpritesheet = human_idle_right_strips
		elif key == K_LEFT:
			self.currentSpritesheet = human_idle_left_strips
		return self.currentSpritesheet


	def coord(self):
		return (self.x, self.y)

	def getCurrentSpritesheet(self):
		return self.currentSpritesheet

class Skeleton(pygame.sprite.Sprite):
	def __init__(self, startx, starty):
		pygame.sprite.Sprite.__init__(self)

		self.x = startx
		self.y = starty

		self.currentSpritesheet = skeleton_idle_down_strips

		self.x_dist = 12
		self.y_dist = 12
		self.x_momentum = 0
		self.x_momentumInc = 2
		self.x_momentumDec = 1.5
		self.x_momentumDecay = .5
		self.y_momentum = 0
		self.y_momentumInc = 2
		self.y_momentumDec = 1.5
		self.y_momentumDecay = .5

	def move(self, keylist, prevkey):
		xMove = 0;
		yMove = 0;

		if keylist[K_w]:
			self.y += -self.y_dist
			self.y_momentum += self.y_momentumInc
			self.y += -self.y_momentum
			self.y_momentum -= self.y_momentumDec
			if prevkey != K_w:
				self.currentSpritesheet = skeleton_walking_up_strips
		if keylist[K_s]:
			self.y += self.y_dist
			self.y_momentum += -self.y_momentumInc
			self.y += -self.y_momentum
			self.y_momentum -= -self.y_momentumDec
			if prevkey != K_s:
				self.currentSpritesheet = skeleton_walking_down_strips
		if keylist[K_d]:
			self.x += self.x_dist
			self.x_momentum += self.x_momentumInc
			self.x += self.x_momentum
			self.x_momentum -= self.x_momentumDec
			if prevkey != K_d:
				self.currentSpritesheet = skeleton_walking_right_strips
		if keylist[K_a]:
			self.x += -self.x_dist
			self.x_momentum += -self.x_momentumInc
			self.x += self.x_momentum
			self.x_momentum -= -self.x_momentumDec
			if prevkey != K_a:
				self.currentSpritesheet = skeleton_walking_left_strips
		return self.currentSpritesheet
	
	def stop(self, key, prevkey):
		if key == K_w:
			self.currentSpritesheet = skeleton_idle_up_strips
		elif key == K_s:
			self.currentSpritesheet = skeleton_idle_down_strips
		elif key == K_d:
			self.currentSpritesheet = skeleton_idle_right_strips
		elif key == K_a:
			self.currentSpritesheet = skeleton_idle_left_strips
		return self.currentSpritesheet

	# def loseMomentum(self):
	# 	if self.x_momentum > 0:
	# 		self.x -= self.x_momentum
	# 		if self.x_momentumDecay > self.x_momentum:
	# 			self.x_momentum = 0
	# 		else:
	# 			self.x_momentum -= self.x_momentumDecay
	# 	elif self.x_momentum < 0:
	# 		self.x += self.x_momentum
	# 		if self.x_momentumDecay > self.x_momentum:
	# 			self.x_momentum = 0
	# 		else:
	# 			self.x_momentum += self.x_momentumDecay
		
	# 	if self.y_momentum > 0:
	# 		self.y -= self.y_momentum
	# 		if self.y_momentumDecay > self.y_momentum:
	# 			self.y_momentum = 0
	# 		else:
	# 			self.y_momentum -= self.y_momentumDecay
	# 	elif self.y_momentum < 0:
	# 		self.y += self.y_momentum
	# 		if self.y_momentumDecay > self.y_momentum:
	# 			self.y_momentum = 0
	# 		else:
	# 			self.y_momentum += self.y_momentumDecay

	def coord(self):
		return (self.x, self.y)
	def getCurrentSpritesheet(self):
		return self.currentSpritesheet

def main():
	FPS = 60
	frames = FPS / 12
	black = Color('black')
	white = Color('white')
	clock = pygame.time.Clock()
	n = 0

	player1 = Human(0, 0)
	player2 = Skeleton(500, 500)

	prevkey1 = ""
	prevkey2 = ""

	pygame.key.set_repeat(100, 50)

	while True:
	    for e in pygame.event.get():
	    	if e.type == KEYDOWN:
	    		keys = pygame.key.get_pressed()
	    		if (e.key == K_DOWN or e.key == K_UP or e.key == K_LEFT or e.key == K_RIGHT or e.key == K_w or e.key == K_a or e.key == K_s or e.key == K_d):
	    			image1 = player1.move(keys, prevkey1)
	    			prevkey1 = e.key
	    			image2 = player2.move(keys, prevkey2)
	    			prevkey2 = e.key
	        elif e.type == KEYUP:
	            if e.key == K_ESCAPE:
	                sys.exit()
	            if (e.key == K_DOWN or e.key == K_UP or e.key == K_LEFT or e.key == K_RIGHT or e.key == K_w or e.key == K_a or e.key == K_s or e.key == K_d):
	    			image1 = player1.stop(e.key, prevkey1)
	    			prevkey1 = e.key
	    			image2 = player2.stop(e.key, prevkey2)
	    			prevkey2 = e.key
	    # player1.loseMomentum()
	    # player2.loseMomentum()
	    image1 = player1.getCurrentSpritesheet()
	    image1 = image1.next()

	    image2 = player2.getCurrentSpritesheet()
	    image2 = image2.next()

	    surface.fill(black)
	    surface.blit(image1, player1.coord())
	    surface.blit(image2, player2.coord())
	    pygame.display.flip()
	    clock.tick(FPS)

if __name__ == "__main__":
	main()