import pygame

class Character(object):
    def __init__(self, filename):
        self.filename = filename
        player = pygame.Rect(0, 0, 64, 64)
        char = pygame.image.load(filename)
        screen.blit(char, player)

bob = Character('1.png')