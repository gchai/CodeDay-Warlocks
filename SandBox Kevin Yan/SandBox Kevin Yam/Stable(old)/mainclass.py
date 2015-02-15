# Tiles/Mapping: http://qq.readthedocs.org/en/latest/tiles.html
# Installing Pygame: http://www.frihost.com/forums/vt-160879.html

# Sound - Gabe
# Grahics - ACE
# Input - Samson
# ? - SLOTH

import os, sys
import pygame

from pygame.locals import *
from spritesheet import *

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sounds disabled'
class PyMain:
	def __init__(self, width=1024, height = 768):
		pygame.init()
		self.width = width
		self.height = height
		self.screen = pygame.display.set_mode((self.width, self.height))

	def MainLoop(self):
		self.loadSprites()

		pygame.key.set_repeat(500, 30)

		while 1:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				elif event.type == KEYDOWN:
					if ((event.key == K_UP)
					or (event.key == K_DOWN)
					or (event.key == K_LEFT)
					or (event.key == K_RIGHT)):
						self.player.move(event.key)

			# self.player_sprites.draw(self.screen)

	def loadSprites(self):
		pass

class Player(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image, self.rect = load_image('Assets/Player/Body_animation.png')

		self.x_dist = 10
		self.y_dist = 10

	def move(self, key):
		xMove = 0;
		yMove = 0;

		if key == K_UP:
			ymove = -self.y_dist
		elif key == K_DOWN:
			ymove = self.y_dist
		if key == K_RIGHT:
			xmove = self.x_dist
		if key == K_LEFT:
			xmove = -self.x_dist

def load_image(name, colorkey=None):
    fullname = os.path.join(os.path.dirname(__file__), name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', fullname
        raise SystemExit, message
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()

if __name__ == "__main__":
	MainWindow = PyMain()
	MainWindow.MainLoop()

# surface = pygame.display.set_mode((100,100))
# FPS = 120
# frames = FPS / 12
# strips = [
#     SpriteStripAnim('BODY_skeleton.png', (64,192,64,64), 9, 1, True, frames)
#     #SpriteStripAnim('BODY_skeleton.png', (0,64,64,64), 5, 1, True, frames),
#     #SpriteStripAnim('BODY_skeleton.png', (0,128,64,64), 5, 1, True, frames)
# ]
# black = Color('black')
# clock = pygame.time.Clock()
# n = 0
# strips[n].iter()
# image = strips[n].next()
# while True:
#     for e in pygame.event.get():
#         if e.type == KEYUP:
#             if e.key == K_ESCAPE:
#                 sys.exit()
#             elif e.key == K_RETURN:
#                 n += 1
#                 if n >= len(strips):
#                     n = 0
#                 strips[n].iter()
#     surface.fill(black)
#     surface.blit(image, (0,0))
#     pygame.display.flip()
#     image = strips[n].next()
#     clock.tick(FPS)