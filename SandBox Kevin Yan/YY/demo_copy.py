import sys
import pygame
import Image
from pygame.locals import Color, KEYUP, K_ESCAPE, K_RETURN
import spritesheet
from sprite_strip_anim import SpriteStripAnim

class Character(object):
    def __init__(self, filename):
        self.filename = filename
        player = pygame.Rect(0, 0, 64, 64)
        char = pygame.image.load(filename)
        surface.blit(char, player)
 
surface = pygame.display.set_mode((832,256))
FPS = 120
frames = FPS / 12

album=['1.png','2.png', '3.png', '4.png', '5.png', '6.png']

for n in album:
   user = Character(n)

#DO I Convert?
done = False

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True
    pygame.display.flip()
    clock.tick(60)
pygame.quit()


left_strips = SpriteStripAnim(user, (0,64,64,64), 13, -1, True, frames)
right_strips = SpriteStripAnim(user, (0,192,64,64), 13, -1, True, frames)
up_strips = SpriteStripAnim(user, (0,0,64,64), 13, -1, True, frames)
down_strips = SpriteStripAnim('human_walking.png', (0,128,64,64), 13, -1, True, frames)