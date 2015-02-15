# Tiles/Mapping: http://qq.readthedocs.org/en/latest/tiles.html
# Installing Pygame: http://www.frihost.com/forums/vt-160879.html

# Sound - Gabe
# Grahics - ACE
# Input - Samson
# Compiling - SLOTH

import os, sys
import pygame

from pygame.locals import*

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sounds disabled'

class PyMain:
    def __init__(self, width=640, height = 480):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
    def MainLoop(self):
	    while 1:
	        for event in pygame.event.get():
	            if event.type == pygame.QUIT:
	                sys.exit()
	        pygame.display.flip()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image()

if __name__ == "__main__":
    MainWindow = PyMain()
    MainWindow.MainLoop()   
    
    
#Kevin Yam - Tiles
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

# Sound Loader - Gabe
def load_sound(name):
    class NoneSound:
        def play(self): pass
    if not pygame.mixer or not pygame.mixer.get_init():
        return NoneSound()
    fullname = os.path.join('data', name)
    try:
        sound = pygame.mixer.Sound(fullname)
    except pygame.error, message:
        print 'Cannot load sound:', fullname
        raise SystemExit, message
    return sound
#End sound loader

#Prepare Game Objects
    clock = pygame.time.Clock()
    #Example_Sound = load_sound('bowarrow.ogg')
    #punch_sound = load_sound('punch.wav')
  


if __name__=='__main__':
    pygame.init()
    screen = pygame.display.set_mode((128, 98))
    screen.fill((255, 255, 255))
    table = load_tile_table("ground.png", 24, 16)
    for x, row in enumerate(table):
        for y, tile in enumerate(row):
            screen.blit(tile, (x*32, y*24))
    pygame.display.flip()
    while pygame.event.wait().type != pygame.locals.QUIT:
        pass
    