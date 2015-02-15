import time
 
import pygame
from pygame.locals import *
 

def move(keylist):
    xMove = 0;
    yMove = 0;

    if keylist[K_w]:
        self.y += -self.y_dist

    if keylist[K_s]:
        self.y += self.y_dist

    if keylist[K_d]:
        self.x += self.x_dist

    if keylist[K_a]:
        self.x += -self.x_dist



def load_frames():
    # build a dict of lists. The event.key name will be used as the key.
    # {'up': [frame0, frame1, ...], 'left': [...], ...}
    walk_dirs = [pygame.key.name(k) for k in [K_UP, K_LEFT, K_DOWN, K_RIGHT]]
    if k==[K_UP]:
        y += -y_dist
    if k==[K_DOWN]:
        y += y_dist
    if k==[K_RIGHT]:
        x += x_dist
    if k==[K_LEFT]:
        x += -x_dist
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
 
body = pygame.image.load('human_walking.png')
hood = pygame.image.load('hood.png')
shirt = pygame.image.load('shirt.png')
shoe = pygame.image.load('shoes.png')
legs = pygame.image.load('legs.png')
body.blit(hood, (0, -10))
body.blit(shirt, (0, -10))
body.blit(legs, (0, -10))
body.blit(shoe, (0, -5))
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