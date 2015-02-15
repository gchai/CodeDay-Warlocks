import pygame, os, system, math
from pygame.locals import*
pygame.init()

Winw = 5.05
Winh = 3
SPEED = 12 
WINDOWW=  int(20 * SPEED * Winw)
WINDOWH =  int(20 * SPEED * Winh)
IQ = 10#1-10 value
Playerpoints = 0
Totalpoints = 0
screen = pygame.display.set_mode((WindowX, WindowH), pygame.FULLSCREEN | pygame.DOUBLEBUFF )
TRAIL_LIMIT = 90
CLOCKRATE = 30
COL = pygame.time.get_ticks()

class LightBike(pygame.sprite.Sprite):
    def __init__(self, controls = 3, SpSet = "lights/GLOWRED"):
        self.Control = controls
        self.Playerpoints = 0
        self.HP = 10
        self.TB = 10
        self.SpSet = SpSet
        self.Totalpoints = 0
        self.point = 0
        pygame.sprite.Sprite.__init__(self)
        self.sprite_reference = self.SpSet + "R.png"
        self.image = pygame.image.load(self.sprite_reference)
        self.rect = self.image.get_rect()
        self.rect.center = (SPEED,SPEED)
        self.prev_pos = []
        self.speed = SPEED
        self.dir = "R"
        self.living = True
    def begin(self):
        self.living = True
        self.prev_pos = []
        self.dir = "R"
        self.rect.centerx = SPEED * 5 * self.Control
        self.rect.centery = SPEED * 5 * self.Control
        self.HP = 10
        self.sprite_reference = self.SpSet + "R.png"
    def update(self, COL):
        self.x = SPEED * 5 * self.Control
        self.y = SPEED * 5 * self.Control
        if self.TB >= 200:
            self.TB = 0
            
        if self.living:
            if self.rect.centery >= screen.get_height()+ SPEED:
                self.Stop()
            if self.rect.centerx >= screen.get_width()+ SPEED:
                self.Stop()
            if self.rect.centery <= 0-SPEED:
                self.Stop()
            if self.rect.centerx <= 0-SPEED:
                self.Stop()
            
# Sets the self.dir variable. Helps ensure constant movement despite a player not pressing a button
            if self.Control == 1: #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
                if pygame.key.get_pressed()[pygame.K_RIGHT]:
                    self.dir = "R"
                elif pygame.key.get_pressed()[pygame.K_DOWN]:
                    self.dir = "D"
                elif pygame.key.get_pressed()[pygame.K_LEFT]:
                    self.dir = "L"
                elif pygame.key.get_pressed()[pygame.K_UP]:
                    self.dir = "U"
            elif self.Control ==2:#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                if pygame.key.get_pressed()[pygame.K_d]:
                    self.dir = "R"
                elif pygame.key.get_pressed()[pygame.K_s]:
                    self.dir = "D"
                elif pygame.key.get_pressed()[pygame.K_a]:
                    self.dir = "L"
                elif pygame.key.get_pressed()[pygame.K_w]:
                    self.dir = "U"
            elif self.Control == 3:#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                if pygame.key.get_pressed()[pygame.K_l]:
                    self.dir = "R"
                elif pygame.key.get_pressed()[pygame.K_k]:
                    self.dir = "D"
                elif pygame.key.get_pressed()[pygame.K_j]:
                    self.dir = "L"
                elif pygame.key.get_pressed()[pygame.K_i]:
                    self.dir = "U"
            #elif self.Control == .1:#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                
            self.sprite_reference = self.SpSet + self.dir + ".png"#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                for Bike in Enemies:
                    if len(Bike.prev_pos) > 4:
                        for i in range (0,len(Bike.prev_pos) - 4):
                            Bike.prev_pos.pop(0)
                    elif len(Bike.prev_pos) > 0:
                        Bike.prev_pos.pop(0)
# Moves the Character's bike              
            if self.dir == "R":
                self.moveright()
            if self.dir == "D":
                self.movedown()
            if self.dir == "L":
                self.moveleft()
            if self.dir == "U":
                self.moveup()
            for Bike in Enemies:
               if self.rect.center in Bike.prev_pos:
                   self.Stop()
            if self.rect.center in self.prev_pos:
                self.Stop()
            self.prev_pos.append(self.rect.center)
# Actually sets the sprite, using the reference
        else:
            pygame.draw.circle(screen, ((COL/5) % 254, (COL/ 7) % 254, (COL/9) % 254), self.rect.center, 12, 1)
            self.sprite_reference = "transparent.png"
            if len(self.prev_pos) > 0:
                self.prev_pos.pop(0)
        if len(self.prev_pos) > 1:
            pygame.draw.aalines(screen,((COL/5) % 254, self.Control * 122, (COL/9) % 254),False,self.prev_pos)
            
        if len(self.prev_pos) > (TRAIL_LIMIT + self.TB):
            self.prev_pos.pop(0)
            if len(self.prev_pos) > (TRAIL_LIMIT + self.TB):
                self.prev_pos.pop(0)
        
        self.image = pygame.image.load(self.sprite_reference)
    def Stop(self):
        lb.HP-= 1
        if lb.HP <= 0:
            self.living = False
    def movedown(self):
        self.rect.centery += self.speed
    def moveup(self):
        self.rect.centery -= self.speed
    def moveleft(self):
        self.rect.centerx -= self.speed
    def moveright(self):
        self.rect.centerx += self.speed
    def addpoints(self):
        self.point += 10
        
