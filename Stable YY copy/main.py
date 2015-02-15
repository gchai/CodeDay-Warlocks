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

		self.x_dist = 10
		self.y_dist = 10

	def move(self, key, prevkey):
		xMove = 0;
		yMove = 0;

		if key == K_UP:
			self.y += -self.y_dist
			if prevkey != K_UP:
				self.currentSpritesheet = human_walking_up_strips
		elif key == K_DOWN:
			self.y += self.y_dist
			if prevkey != K_DOWN:
				self.currentSpritesheet = human_walking_down_strips
		elif key == K_RIGHT:
			self.x += self.x_dist
			if prevkey != K_RIGHT:
				self.currentSpritesheet = human_walking_right_strips
		elif key == K_LEFT:
			self.x += -self.x_dist
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

		self.x_dist = 10
		self.y_dist = 10

	def move(self, key, prevkey):
		xMove = 0;
		yMove = 0;

		if key == K_w:
			self.y += -self.y_dist
			if prevkey != K_w:
				self.currentSpritesheet = skeleton_walking_up_strips
		elif key == K_s:
			self.y += self.y_dist
			if prevkey != K_s:
				self.currentSpritesheet = skeleton_walking_down_strips
		elif key == K_d:
			self.x += self.x_dist
			if prevkey != K_d:
				self.currentSpritesheet = skeleton_walking_right_strips
		elif key == K_a:
			self.x += -self.x_dist
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

	def coord(self):
		return (self.x, self.y)
	def getCurrentSpritesheet(self):
		return self.currentSpritesheet

def main():
	FPS = 100
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
	    		if (keys[K_DOWN] or keys[K_UP ]or keys[K_LEFT] or keys[K_RIGHT] or keys[K_w] or keys[K_a] or keys[K_s] or keys[K_d]):
	    			image1 = player1.move(e.key, prevkey1)
	    			prevkey1 = e.key
	    			image2 = player2.move(e.key, prevkey2)
	    			prevkey2 = e.key
	        elif e.type == KEYUP:
	            if e.key == K_ESCAPE:
	                sys.exit()
	            if (keys[K_DOWN] or keys[K_UP ]or keys[K_LEFT] or keys[K_RIGHT] or keys[K_w] or keys[K_a] or keys[K_s] or keys[K_d]):
	    			image1 = player1.stop(e.key, prevkey1)
	    			prevkey1 = e.key
	    			image2 = player2.stop(e.key, prevkey2)
	    			prevkey2 = e.key
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