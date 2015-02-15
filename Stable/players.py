import pygame
from strips import *

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

		self.alive = True

	def move(self, keylist, prevkey):
		xMove = 0;
		yMove = 0;

		if not self.alive:
			return self.currentSpritesheet
		else:
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

		self.alive = True
	def move(self, keylist, prevkey):
		xMove = 0;
		yMove = 0;

		if not self.alive:
			return self.currentSpritesheet
		else:
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

	def coord(self):
		return (self.x, self.y)

	def getCurrentSpritesheet(self):
		return self.currentSpritesheet