import sys
import pygame
from pygame.locals import *
import spritesheet

class SpriteStripAnim(object):
    def __init__(self, filename, rect, count, colorkey=None, loop=False, frames=1):
        self.filename = filename
        ss = spritesheet.spritesheet(filename)
        self.images = ss.load_strip(rect, count, colorkey)
        self.i = 0
        self.loop = loop
        self.frames = frames
        self.f = frames
    def iter(self):
        self.i = 0
        self.f = self.frames
        return self
    def next(self):
        if self.i >= len(self.images):
            if not self.loop:
                raise StopIteration
            else:
                self.i = 0
        image = self.images[self.i]
        self.f -= 1
        if self.f == 0:
            self.i += 1
            self.f = self.frames
        return image
    def __add__(self, ss):
        self.images.extend(ss.images)
        return self

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