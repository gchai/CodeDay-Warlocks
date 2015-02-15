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
from players import *

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sounds disabled'

def load_tile_table(filename, width, height):
	image = pygame.image.load(filename).convert()
	image_width, image_height = image.get_size()
	tile_table = []
	for tile_x in range(0, image_width/width):
		line = []
		tile_table.append(line)
		for tile_y in range(0, image_height/height):
			rect = (tile_x*width, tile_y*height, width, height)
			line.append(image.subsurface(rect))
	return tile_table

import ConfigParser

class Level(object):
	def load_file(self, filename="level.map"):
		self.map = []
		self.key = {}
		parser = ConfigParser.ConfigParser()
		parser.read(filename)
		self.tileset = parser.get("level", "tileset")
		self.map = parser.get("level", "map").split("\n")
		for section in parser.sections():
			if len(section) == 1:
				desc = dict(parser.items(section))
				self.key[section] = desc
		self.width = len(self.map[0])
		self.height = len(self.map)

	def get_tile(self, x, y):
		"""Tell what's at the specified position of the map."""

		try:
			char = self.map[y][x]
		except IndexError:
			return {}
		try:
			return self.key[char]
		except KeyError:
			return {}

	def get_bool(self, x, y, name):
		"""Tell if the specified flag is set for position on the map."""

		value = self.get_tile(x, y).get(name)
		return value in (True, 1, 'true', 'yes', 'True', 'Yes', '1', 'on', 'On')

	def is_wall(self, x, y):
		"""Is there a wall?"""

		return self.get_bool(x, y, 'wall')

	def render(self):
		wall = self.is_wall
		tiles = MAP_CACHE[self.tileset]
		image = pygame.Surface((self.width*MAP_TILE_WIDTH, self.height*MAP_TILE_HEIGHT))
		overlays = {}
		for map_y, line in enumerate(self.map):
			for map_x, c in enumerate(line):
				if wall(map_x, map_y):
					# Draw different tiles depending on neighbourhood
					if not wall(map_x, map_y+1):
						if wall(map_x+1, map_y) and wall(map_x-1, map_y):
							tile = 1, 2
						elif wall(map_x+1, map_y):
							tile = 0, 2
						elif wall(map_x-1, map_y):
							tile = 2, 2
						else:
							tile = 3, 2
					else:
						if wall(map_x+1, map_y+1) and wall(map_x-1, map_y+1):
							tile = 1, 1
						elif wall(map_x+1, map_y+1):
							tile = 0, 1
						elif wall(map_x-1, map_y+1):
							tile = 2, 1
						else:
							tile = 3, 1
					# Add overlays if the wall may be obscuring something
					if not wall(map_x, map_y-1):
						if wall(map_x+1, map_y) and wall(map_x-1, map_y):
							over = 1, 0
						elif wall(map_x+1, map_y):
							over = 0, 0
						elif wall(map_x-1, map_y):
							over = 2, 0
						else:
							over = 3, 0
						overlays[(map_x, map_y)] = tiles[over[0]][over[1]]
				else:
					try:
						tile = self.key[c]['tile'].split(',')
						tile = int(tile[0]), int(tile[1])
					except (ValueError, KeyError):
						# Default to ground tile
						tile = 0, 3
				tile_image = tiles[tile[0]][tile[0]]
				image.blit(tile_image,
						   (map_x*MAP_TILE_WIDTH, map_y*MAP_TILE_HEIGHT))
		return image, overlays

	def is_blocking(self, x, y):
		"""Is this place blocking movement?"""

		if not 0 <= x < self.width or not 0 <= y < self.height:
			return True
		return self.get_bool(x, y, 'block')

def main():
	FPS = 60
	frames = FPS / 12
	black = Color('black')
	white = Color('white')
	clock = pygame.time.Clock()
	n = 0

	#map

	level = Level()#
	level.load_file('level.map')
	background, overlay_dict = level.render()
	overlays = pygame.sprite.OrderedUpdates()
	for (x, y), image in overlay_dict.iteritems():
		overlay = pygame.sprite.Sprite(overlays)
		overlay.image = image
		overlay.rect = image.get_rect().move(x * 24, y * 16 - 16)

	player1 = Human(240, 100)
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
				if level.get_tile(int(player1.x/64), int(player1.y/64))["name"] == "lava":
					player1.currentSpritesheet = dying_strips
					player1.alive = False
				if level.get_tile(int(player2.x/64), int(player2.y/64))["name"] == "lava":
					player2.currentSpritesheet = skeleton_dying_strips
					player2.alive = False
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
		surface.blit(background, (0, 0))
		overlays.draw(surface)

		if player1.alive:
			surface.blit(image1, player1.coord())
		else:
			image1 = dying_strips.iter()
			image1 = image1.next()
			surface.blit(image1, player1.coord())
		if player2.alive:
			surface.blit(image2, player2.coord())
		else:
			image2 = skeleton_dying_strips.iter()
			image2 = image2.next()
			surface.blit(image2, player2.coord())
		surface.blit(image2, player2.coord())
		pygame.display.flip()
		clock.tick(FPS)

if __name__ == "__main__":
	MAP_TILE_WIDTH = 64
	MAP_TILE_HEIGHT = 64
	MAP_CACHE = {
		'GroundLava.png': load_tile_table('GroundLava.png', MAP_TILE_WIDTH,
									  MAP_TILE_HEIGHT),
	}
	main()