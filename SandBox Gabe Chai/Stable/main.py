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

import ConfigParser

#kevin Begin
MAP_TILE_WIDTH, MAP_TILE_HEIGHT = 64, 64


class TileCache(object):
	"""Load the tilesets lazily into global cache"""

	def __init__(self,  width=32, height=None):
		self.width = width
		self.height = height or width
		self.cache = {}

	def __getitem__(self, filename):
		"""Return a table of tiles, load it from disk if needed."""

		key = (filename, self.width, self.height)
		try:
			return self.cache[key]
		except KeyError:
			tile_table = self._load_tile_table(filename, self.width,
											   self.height)
			self.cache[key] = tile_table
			return tile_table

	def _load_tile_table(self, filename, width, height):
		"""Load an image and split it into tiles."""

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
class Level(object):
	"""Load and store the map of the level, together with all the items."""

	def __init__(self, filename="level.map"):
		self.tileset = ''
		self.map = []
		self.items = {}
		self.key = {}
		self.width = 0
		self.height = 0
		self.load_file(filename)

	def load_file(self, filename="level.map"):
		"""Load the level from specified file."""

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
		for y, line in enumerate(self.map):
			for x, c in enumerate(line):
				if not self.is_wall(x, y) and 'sprite' in self.key[c]:
					self.items[(x, y)] = self.key[c]

	def render(self):
		"""Draw the level on the surface."""

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
				tile_image = tiles[tile[0]][tile[1]]
				image.blit(tile_image,
						   (map_x*MAP_TILE_WIDTH, map_y*MAP_TILE_HEIGHT))
		return image, overlays

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

	def is_blocking(self, x, y):
		"""Is this place blocking movement?"""

		if not 0 <= x < self.width or not 0 <= y < self.height:
			return True
		return self.get_bool(x, y, 'block')

# class Level(object):
#     def load_file(self, filename="level.map"):
#         self.map = []
#         self.key = {}
#         parser = ConfigParser.ConfigParser()
#         parser.read(filename)
#         self.tileset = parser.get("level", "tileset")
#         self.map = parser.get("level", "map").split("\n")
#         for section in parser.sections():
#             if len(section) == 1:
#                 desc = dict(parser.items(section))
#                 self.key[section] = desc
#         self.width = len(self.map[0])
#         self.height = len(self.map)

#     def get_tile(self, x, y):
#         """Tell what's at the specified position of the map."""

#         try:
#             char = self.map[y][x]
#         except IndexError:
#             return {}
#         try:
#             return self.key[char]
#         except KeyError:
#             return {}

#     def get_bool(self, x, y, name):
#         """Tell if the specified flag is set for position on the map."""

#         value = self.get_tile(x, y).get(name)
#         return value in (True, 1, 'true', 'yes', 'True', 'Yes', '1', 'on', 'On')

#     def is_wall(self, x, y):
#         """Is there a wall?"""

#         return self.get_bool(x, y, 'wall')

#     def render(self):
#         wall = self.is_wall
#         tiles = MAP_CACHE[self.tileset]
#         image = pygame.Surface((self.width*MAP_TILE_WIDTH, self.height*MAP_TILE_HEIGHT))
#         overlays = {}
#         for map_y, line in enumerate(self.map):
#             for map_x, c in enumerate(line):
#                 if wall(map_x, map_y):
#                     # Draw different tiles depending on neighbourhood
#                     if not wall(map_x, map_y+1):
#                         if wall(map_x+1, map_y) and wall(map_x-1, map_y):
#                             tile = 1, 2
#                         elif wall(map_x+1, map_y):
#                             tile = 0, 2
#                         elif wall(map_x-1, map_y):
#                             tile = 2, 2
#                         else:
#                             tile = 3, 2
#                     else:
#                         if wall(map_x+1, map_y+1) and wall(map_x-1, map_y+1):
#                             tile = 1, 1
#                         elif wall(map_x+1, map_y+1):
#                             tile = 0, 1
#                         elif wall(map_x-1, map_y+1):
#                             tile = 2, 1
#                         else:
#                             tile = 3, 1
#                     # Add overlays if the wall may be obscuring something
#                     if not wall(map_x, map_y-1):
#                         if wall(map_x+1, map_y) and wall(map_x-1, map_y):
#                             over = 1, 0
#                         elif wall(map_x+1, map_y):
#                             over = 0, 0
#                         elif wall(map_x-1, map_y):
#                             over = 2, 0
#                         else:
#                             over = 3, 0
#                         overlays[(map_x, map_y)] = tiles[over[0]][over[1]]
#                 else:
#                     try:
#                         tile = self.key[c]['tile'].split(',')
#                         tile = int(tile[0]), int(tile[1])
#                     except (ValueError, KeyError):
#                         # Default to ground tile
#                         tile = 0, 3
#                 tile_image = tiles[tile[0]][tile[1]]
#                 image.blit(tile_image,
#                            (map_x*MAP_TILE_WIDTH, map_y*MAP_TILE_HEIGHT))
#         return image, overlays

# #Kevin end
	# def is_blocking(self, x, y):
	#     """Is this place blocking movement?"""

	#     if not 0 <= x < self.width or not 0 <= y < self.height:
	#         return True
	#     return self.get_bool(x, y, 'block')



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
		if key == K_DOWN:
			self.currentSpritesheet = human_idle_down_strips
		if key == K_RIGHT:
			self.currentSpritesheet = human_idle_right_strips
		if key == K_LEFT:
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
		if key == K_UP:
			self.currentSpritesheet = skeleton_idle_up_strips
		if key == K_DOWN:
			self.currentSpritesheet = skeleton_idle_down_strips
		if key == K_RIGHT:
			self.currentSpritesheet = skeleton_idle_right_strips
		if key == K_LEFT:
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
#Mapping properties

	MAP_CACHE = TileCache(MAP_TILE_WIDTH, MAP_TILE_HEIGHT)#not sure
	TILE_CACHE = TileCache(64, 64)

	level = Level()
	level.load_file('level.map')
	

	background, overlay_dict = level.render()
	overlays = pygame.sprite.RenderUpdates()
	for (x, y), image in overlay_dict.iteritems():
		overlay = pygame.sprite.Sprite(overlays)
		overlay.image = image
		overlay.rect = image.get_rect().move(x * 24, y * 16 - 16)
	screen.blit(background, (0, 0))
	overlays.draw(screen)


	player1 = Human(0, 0)
	player2 = Skeleton(500, 500)

	prevkey1 = ""
	prevkey2 = ""

	pygame.key.set_repeat(100, 40)

	while True:
		for e in pygame.event.get():
			if e.type == KEYDOWN:
				if (e.key == K_DOWN or e.key == K_UP or e.key == K_LEFT or e.key == K_RIGHT):
					image1 = player1.move(e.key, prevkey1)
					# image1.iter()
					prevkey1 = e.key
				if (e.key == K_w or e.key == K_a or e.key == K_s or e.key == K_d):
					image2 = player2.move(e.key, prevkey2)
					# image2.iter()
					prevkey2 = e.key
			elif e.type == KEYUP:
				if e.key == K_ESCAPE:
					sys.exit()
				if (e.key == K_DOWN or e.key == K_UP or e.key == K_LEFT or e.key == K_RIGHT):
					image1 = player1.stop(e.key, prevkey1)	    			
					prevkey1 = e.key
				if (e.key == K_w or e.key == K_a or e.key == K_s or e.key == K_d):
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