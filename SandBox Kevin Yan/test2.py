import pygame
from sprite_strip_anim import SpriteStripAnim

class Overlay(pygame.sprite.Sprite):
	def __init__(self, layer, width, height):
		super(Overlay, self).__init__()
		self.image = pygame.Surface([width, height])
		self.rect = self.image.get_rect()

pygame.init()

screen_width = 832
screen_height = 256
screen = pygame.display.set_mode([screen_width, screen_height])

#man = pygame.image.load("BODY_animation.png")
player = pygame.Rect(0, 0, 64, 64)
head = pygame.Rect(0, 0, 64, 64)
leg = pygame.Rect(0, 0, 64, 64)
torso = pygame.Rect(0, 0, 64, 64)
playerImage = pygame.image.load('1.png')
headImage = pygame.image.load('2.png')
legImage = pygame.image.load('3.png')
torsoImage = pygame.image.load('4.png')
#one = Overlay(man, 64, 64)

characters = pygame.sprite.Group()
all_characters_list = pygame.sprite.Group()

#characters.add(one)
#all_characters_list.add(one)
done = False

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True

	screen.blit(playerImage, player)
	screen.blit(headImage, head)
	screen.blit(legImage, leg)
	screen.blit(torsoImage, torso)
	characters.draw(screen)
	pygame.display.flip()
	clock.tick(60)
pygame.quit()