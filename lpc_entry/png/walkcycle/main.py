import time
 
import pygame
from pygame.locals import *
 
 
def load_frames():
    # build a dict of lists. The event.key name will be used as the key.
    # {'up': [frame0, frame1, ...], 'left': [...], ...}
    walk_dirs = [pygame.key.name(k) for k in [K_UP, K_LEFT, K_DOWN, K_RIGHT]]
    walking = {}
    rect = Rect(0, 0, 64, 64)
    for y in range(0, 64 * 4, 64):
        # each row...
        walk_dir = walk_dirs.pop(0)
        print('loading {}'.format(walk_dir))
        frames = []
        walking[walk_dir] = frames
        for x in range(0, 64 * 9, 64):
            # each column...
            im = pygame.Surface((64, 64))
            im.blit(body, (0, 0), rect.move(x, y))
            frames.append(im)
    return walking
 
 
pygame.init()
 
resolution = 1024, 768
screen = pygame.display.set_mode(resolution)
screen_rect = screen.get_rect()
 
clock = pygame.time.Clock()
max_fps = 60
 
body = pygame.image.load('BODY_male.png')
armor = pygame.image.load('TORSO_chain_armor_torso.png')
body.blit(armor, (0, 0))
walking = load_frames()
 
face_dir = 'down'  # standing still is frame[0]
walk_dir = None    # walking is frame[1:]
pace = 1.0 / len(walking['up'][1:])   # anim cycle runs 1.0 real seconds
i = 1
running = True
while running:
    screen.fill((0, 0, 0))
    if walk_dir is None:
        # standing still
        screen.blit(walking[face_dir][0], (0, 0))
    else:
        # walking
        screen.blit(walking[walk_dir][i], (0, 0))
    pygame.display.flip()
 
    for e in pygame.event.get():
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                running = False
            elif e.key in (K_UP, K_LEFT, K_DOWN, K_RIGHT):
                # face_dir: remember the direction for standing still
                face_dir = walk_dir = pygame.key.name(e.key)
                print('walking {}'.format(walk_dir))
                i = 0
        elif e.type == KEYUP:
            if e.key in (K_UP, K_LEFT, K_DOWN, K_RIGHT):
                walk_dir = None
                print('stopped')
        elif e.type == QUIT:
            running = False
 
    dt = clock.tick(max_fps) / 1000.0
    if walk_dir is not None:
        pace -= dt
        if pace <= 0.0:
            pace += 1.0 / len(walking['up'])
            i += 1
            if i == len(walking[walk_dir]):
                i = 1
                print('new walking sequence {}'.format(time.time()))