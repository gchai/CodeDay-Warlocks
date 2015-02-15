import pygame
from pygame.locals import *
 
 
pygame.init()
 
resolution = 1024, 768
screen = pygame.display.set_mode(resolution)
screen_rect = screen.get_rect()
 
clock = pygame.time.Clock()
max_fps = 60
 
body = pygame.image.load('1.png')
armor = pygame.image.load('2.png')
body.blit(armor, (0, 0))
 
frames = []
rect = Rect(0, 0, 64, 64)
for x in range(0, 64 * 9, 64):
    im = pygame.Surface((64, 64))
    im.blit(body, (0, 0), rect.move(x, 0))
    frames.append(im)
 
pace = 2.0 / max_fps
i = 0
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(frames[i], (0, 0))
    pygame.display.flip()
 
    for e in pygame.event.get():
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                running = False
        elif e.type == QUIT:
            running = False
 
    dt = clock.tick(max_fps) / 1000.0
    pace -= dt
    if pace <= 0.0:
        pace += 2.0 / max_fps
        i += 1
        if i == len(frames):
            i = 0
        print('.')