import pygame
from pygame.locals import *
import spritesheet
from sprite_strip_anim import SpriteStripAnim
 
surface = pygame.display.set_mode((100,100))
FPS = 120
frames = FPS / 12
strips = [
    SpriteStripAnim('fireball.png', (0,0,64,64), 8, 1, True, frames)
]
black = Color('black')
clock = pygame.time.Clock()
n = 0
strips[n].iter()
image = strips[n].next()
while True:
    for e in pygame.event.get():
        if e.type == KEYUP:
            if e.key == K_ESCAPE:
                sys.exit()
            elif e.key == K_RETURN:
                n += 1
                if n >= len(strips):
                    n = 0
                strips[n].iter()
    surface.fill(black)
    surface.blit(image, (0,0))
    pygame.display.flip()
    image = strips[n].next()
    clock.tick(FPS)