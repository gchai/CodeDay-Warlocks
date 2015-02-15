import sys, random
import pygame
from pygame.locals import *
pygame.init()
Winw = 5.05
Winh = 3
SPEED = 12 
WINDOWW=  int(20 * SPEED * Winw)
WINDOWH =  int(20 * SPEED * Winh)
IQ = 10#1-10 value
Playerpoints = 0
Totalpoints = 0
screen = pygame.display.set_mode((WINDOWW, WINDOWH))
TRAIL_LIMIT = 90
TCE = TRAIL_LIMIT
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
    def begin(self, x, y, bleh):
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
        

class LightBike4(pygame.sprite.Sprite):
    def __init__(self, direction, R = 25, G = 0, B = 0, spriteloc = "gliders/GR" ):
        pygame.sprite.Sprite.__init__(self)
        self.sprite_reference = spriteloc + direction + ".png"
        self.thisimage = spriteloc
        self.image = pygame.image.load(self.sprite_reference)
        self.rect = self.image.get_rect()
        self.R = R
        self.IQ = 10
        self.SHP = 2
        self.G = G
        self.B = B
        self.rect.center = (SPEED * 10, SPEED * 20)
        self.prev_pos = []
        self.speed = SPEED
        self.dir = direction
        self.living = True
        self.hasdirectionchanged = False
        self.Drect = Rect(0,0,8, 28)
        self.Urect = Rect(0,0,8, 28)
        self.Lrect = Rect(0,0,28, 8)
        self.Rrect = Rect(0,0,28, 8)
        self.Lclose = Rect(0,0, 14, 14)
        self.Dclose = Rect(0,0, 14, 14)
        self.Uclose = Rect(0,0, 14, 14)
        self.Rclose = Rect(0,0, 14, 14)
        self.Rfar = 0
        self.Lfar = 0
        self.Ufar = 0
        self.Dfar = 0
        self.Rnear = 0
        self.Lnear = 0
        self.Unear = 0
        self.Dnear = 0
    def Stop(self):
        self.living = False
        self.begin( 6*SPEED* random.randint(3, 15), 2*SPEED* random.randint(3, 29), "L")
        lb.Playerpoints += 10
        lb.Totalpoints += 10
        lb.HP += self.SHP
        lb.TB += 10
    def begin(self, x, y, direction):
        self.living = True
        self.prev_pos = []
        self.dir = direction
        self.rect.centerx = x
        self.rect.centery = y
        self.sprite_reference = self.thisimage + direction + ".png"
    def check(self):
        for Bike in Sprites:
            for point in Bike.prev_pos:
                if self.Rrect.collidepoint(point) or self.Rrect.right > WINDOWW:
                    self.Rfar = 1
                elif self.Lrect.collidepoint(point) or self.Lrect.left < 0:
                    self.Lfar = 1
                elif self.Urect.collidepoint(point) or self.Urect.top < 0:
                    self.Ufar = 1
                elif self.Drect.collidepoint(point) or self.Drect.bottom > WINDOWH:
                    self.Dfar = 1
                if self.Dclose.collidepoint(point) or self.Dclose.bottom > WINDOWH:
                    self.Dnear = 1
                elif self.Uclose.collidepoint(point) or self.Uclose.top < 0:
                    self.Unear = 1
                elif self.Lclose.collidepoint(point) or self.Lclose.left < 0:
                    self.Lnear = 1
                elif self.Rclose.collidepoint(point) or self.Rclose.right > WINDOWW:
                    self.Rnear = 1
        for point in self.prev_pos:
            if self.Rrect.collidepoint(point) or self.Rrect.right > WINDOWW:
                self.Rfar = 1
            elif self.Lrect.collidepoint(point) or self.Lrect.left < 0:
                self.Lfar = 1
            elif self.Urect.collidepoint(point) or self.Urect.top < 0:
                self.Ufar = 1
            elif self.Drect.collidepoint(point) or self.Drect.bottom > WINDOWH:
                self.Dfar = 1
            if self.Dclose.collidepoint(point) or self.Dclose.bottom > WINDOWH:
                self.Dnear = 1
            elif self.Uclose.collidepoint(point) or self.Uclose.top < 0:
                self.Unear = 1
            elif self.Lclose.collidepoint(point) or self.Lclose.left < 0:
                self.Lnear = 1
            elif self.Rclose.collidepoint(point) or self.Rclose.right > WINDOWW:
                self.Rnear = 1
    def collisionIQ(self):
        if self.dir == "L":
                if self.IQ >= 2:
                    if self.Lnear:
                        if self.Dnear and self.Unear:
                            #Action(attack, reverse, jump, etc)
                            self.hasdirectionchanged = True
                        elif self.Unear:
                            self.dir = "D"
                            self.hasdirectionchanged = True
                        elif self.Dnear:
                            self.dir = "U"
                            self.hasdirectionchanged = True
                        elif self.Dfar and self.Ufar:
                            if random.randint(0,3) > 1:
                                self.dir = "U"
                            else:
                                self.dir = "D"
                            self.hasdirectionchanged = True
                        else:
                            if self.rect.centery <= WINDOWH/2:
                                self.dir = "D"
                            else:
                                self.dir = "U"
                            self.hasdirectionchanged = True
                    elif self.Lfar:
                        if self.Dnear and self.Unear:
                            #Action(attack, reverse, jump, etc)
                            self.hasdirectionchanged = True
                        elif self.Unear:
                            self.dir = "D"
                            self.hasdirectionchanged = True
                        elif self.Dnear:
                            self.dir = "U"
                            self.hasdirectionchanged = True
                        elif self.Dfar:
                            self.dir = "U"
                            self.hasdirectionchanged = True
                        elif self.Ufar:
                            self.dir = "D"
                            self.hasdirectionchanged = True
                else:
                    if self.Lfar:
                        if self.Dfar and self.Ufar:
                            if self.rect.centery <= WINDOWH/2:
                                self.dir = "D"
                            else:
                                self.dir = "U"
                            self.hasdirectionchanged = True
                        elif self.Ufar:
                            self.dir = "D"
                            self.hasdirectionchanged = True
                        elif self.Dfar:
                            self.dir = "U"
                            self.hasdirectionchanged = True
                        else:
                            if self.rect.centery <= WINDOWH/2:
                                self.dir = "D"
                                self.hasdirectionchanged = True
                            else:
                                self.dir = "U"
                                self.hasdirectionchanged = True
        elif self.dir == "R":
                if self.IQ >= 2:
                    if self.Rnear:
                        if self.Unear and self.Dnear:
                            #Action(attack, reverse, jump, etc)
                            self.hasdirectionchanged = True
                        elif self.Unear:
                            self.dir = "D"
                            self.hasdirectionchanged = True
                        elif self.Dnear:
                            self.dir = "U"
                            self.hasdirectionchanged = True
                        elif self.Dfar and self.Ufar:
                            if self.rect.centery <= WINDOWH/2:
                                self.dir = "D"
                            else:
                                self.dir = "U"
                            self.hasdirectionchanged = True
                        else:
                            if self.rect.centery <= WINDOWH/2:
                                self.dir = "D"
                            else:
                                self.dir = "U"
                            self.hasdirectionchanged = True
                    elif self.Rfar:
                        if self.Dnear and self.Unear:
                            #Action(attack, reverse, jump, etc)
                            self.hasdirectionchanged = True
                        elif self.Unear:
                            self.dir = "D"
                            self.hasdirectionchanged = True
                        elif self.Dnear:
                            self.dir = "U"
                            self.hasdirectionchanged = True
                        elif self.Dfar:
                            self.dir = "U"
                            self.hasdirectionchanged = True
                        elif self.Ufar:
                            self.dir = "D"
                            self.hasdirectionchanged = True
                else:
                    if self.Rfar:
                        if self.Dfar and self.Ufar:
                            if random.randint(0,3) > 1:
                                self.dir = "D"
                            else:
                                self.dir = "U"
                            self.hasdirectionchanged = True
                        elif self.Ufar:
                            self.dir = "D"
                            self.hasdirectionchanged = True
                        elif self.Dfar:
                            self.dir = "U"
                            self.hasdirectionchanged = True
                        else:
                            if self.rect.centery <= WINDOWH/2:
                                self.dir = "D"
                                self.hasdirectionchanged = True
                            else:
                                self.dir = "U"
                                self.hasdirectionchanged = True
        elif self.dir == "U":
                if self.IQ >= 2:
                    if self.Unear:
                        if self.Lnear and self.Rnear:
                            #Action(attack, reverse, jump, etc)
                            self.hasdirectionchanged = True
                        elif self.Lnear:
                            self.dir = "R"
                            self.hasdirectionchanged = True
                        elif self.Rnear:
                            self.dir = "L"
                            self.hasdirectionchanged = True
                        elif self.Rfar and self.Lfar:
                            if random.randint(0,3) > 1:
                                self.dir = "L"
                            else:
                                self.dir = "R"
                            self.hasdirectionchanged = True
                        else:
                            if self.rect.centerx <= WINDOWW/2:
                                self.dir = "R"
                            else:
                                self.dir = "L"
                            self.hasdirectionchanged = True
                    elif self.Ufar:
                        if self.Lnear and self.Rnear:
                            #Action(attack, reverse, jump, etc)
                            self.hasdirectionchanged = True
                        elif self.Rnear:
                            self.dir = "L"
                            self.hasdirectionchanged = True
                        elif self.Lnear:
                            self.dir = "R"
                            self.hasdirectionchanged = True
                        elif self.Rfar:
                            self.dir = "L"
                            self.hasdirectionchanged = True
                        elif self.Lfar:
                            self.dir = "R"
                            self.hasdirectionchanged = True
                else:
                    if self.Ufar:
                        if self.Lfar and self.Rfar:
                            if random.randint(0,3) > 1:
                                self.dir = "R"
                            else:
                                self.dir = "L"
                            self.hasdirectionchanged = True
                        elif self.Lfar:
                            self.dir = "R"
                            self.hasdirectionchanged = True
                        elif self.Rfar:
                            self.dir = "L"
                            self.hasdirectionchanged = True
                        else:
                            if self.rect.centerx <= WINDOWW/2:
                                self.dir = "R"
                                self.hasdirectionchanged = True
                            else:
                                self.dir = "L"
                                self.hasdirectionchanged = True
        
        elif self.dir == "D":
                if self.IQ >= 2:
                    if self.Dnear:
                        if self.Rnear and self.Lnear:
                            #Action(attack, reverse, jump, etc)
                            self.hasdirectionchanged = True
                        elif self.Lnear:
                            self.dir = "R"
                            self.hasdirectionchanged = True
                        elif self.Rnear:
                            self.dir = "L"
                            self.hasdirectionchanged = True
                        elif self.Lfar and self.Rfar:
                            if random.randint(0,3) > 1:
                                self.dir = "R"
                            else:
                                self.dir = "L"
                            self.hasdirectionchanged = True
                        else:
                            if self.rect.centerx <= WINDOWW/2:
                                self.dir = "R"
                            else:
                                self.dir = "L"
                            self.hasdirectionchanged = True
                    elif self.Dfar:
                        if self.Rnear and self.Lnear:
                            #Action(attack, reverse, jump, etc)
                            self.hasdirectionchanged = True
                        elif self.Lnear:
                            self.dir = "R"
                            self.hasdirectionchanged = True
                        elif self.Rnear:
                            self.dir = "L"
                            self.hasdirectionchanged = True
                        elif self.Rfar:
                            self.dir = "L"
                            self.hasdirectionchanged = True
                        elif self.Lfar:
                            self.dir = "R"
                            self.hasdirectionchanged = True
                else:
                    if self.Dfar:
                        if self.Rfar and self.Lfar:
                            if random.randint(0,3) > 1:
                                self.dir = "L"
                            else:
                                self.dir = "R"
                            self.hasdirectionchanged = True
                        elif self.Lfar:
                            self.dir = "R"
                            self.hasdirectionchanged = True
                        elif self.Rfar:
                            self.dir = "L"
                            self.hasdirectionchanged = True
                        else:
                            if self.rect.centerx <= WINDOWW/2:
                                self.dir = "R"
                                self.hasdirectionchanged = True
                            else:
                                self.dir = "L"
                                self.hasdirectionchanged = True
                if self.hasdirectionchanged != True:
                    if random.randint(0, 100) >= 90:
                        if self.Dfar:
                            self.dir = "U"
                            self.hasdirectionchanged = True
                        if self.Ufar:
                            self.dir = "D"
                            self.hasdirectionchanged = True
                        if self.Lfar:
                            self.dir = "R"
                            self.hasdirectionchanged = True
                        if self.Rfar:
                            self.dir = "L"
                            self.hasdirectionchanged = True
    def checkavoidance(self):
        if random.randint(0, 10) >= 9.6:
            if self.dir == "L":
                if self.IQ > 7:
                    None#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~RETURN HERE TO FINISH 
            elif self.dir == "D":
                for Bike in Sprites:
                    for point in Bike.prev_pos:
                        if self.Rrect.collidepoint(point) or self.Rrect.right > WINDOWW:
                            if self.Lrect.collidepoint(point):
                                self.dir = "D"
                                return True
                            else:
                                self.dir = "L"
                                return True
                        elif self.Lrect.collidepoint(point) or self.Lrect.left< 0:
                            if self.Rrect.collidepoint(point):
                                self.dir = "D"
                                return True
                            else:
                                self.dir = "R"
                                return True
                for point in self.prev_pos:
                    if self.Rrect.collidepoint(point) or self.Rrect.right > WINDOWW:
                        if self.Lrect.collidepoint(point):
                            self.dir = "D"
                            return True
                        else:
                            self.dir = "L"
                            return True
                    elif self.Lrect.collidepoint(point) or self.Lrect.left< 0:
                        if self.Rrect.collidepoint(point):
                            self.dir = "D"
                            return True
                        else:
                            self.dir = "R"
                            return True
            elif self.dir == "R":
                for Bike in Sprites:
                    for point in Bike.prev_pos:
                        if self.Urect.collidepoint(point) or self.Urect.top <0:
                            if self.Drect.collidepoint(point):
                                self.dir = "R"
                                return True
                            else:
                                self.dir = "D"
                                return True
                        elif self.Drect.collidepoint(point) or self.Drect.bottom >  WINDOWH:
                            if self.Urect.collidepoint(point):
                                self.dir = "R"
                                return True
                            else:
                                self.dir = "U"
                                return True
                for point in Bike.prev_pos:
                    if self.Urect.collidepoint(point) or self.Urect.top <0:
                        if self.Drect.collidepoint(point):
                            self.dir = "R"
                            return True
                        else:
                            self.dir = "D"
                            return True
                    elif self.Drect.collidepoint(point) or self.Drect.bottom >  WINDOWH:
                        if self.Urect.collidepoint(point):
                            self.dir = "R"
                            return True
                        else:
                            self.dir = "U"
                            return True
            elif self.dir == "U":
                for Bike in Sprites:
                    for point in Bike.prev_pos:
                        if self.Rrect.collidepoint(point) or self.Rrect.right > WINDOWW:
                            if self.Lrect.collidepoint(point):
                                self.dir = "U"
                                return True
                            else:
                                self.dir = "L"
                                return True
                        elif self.Lrect.collidepoint(point) or self.Lrect.left< 0:
                            if self.Rrect.collidepoint(point):
                                self.dir = "U"
                                return True
                            else:
                                self.dir = "R"
                                return True
                for point in Bike.prev_pos:
                    if self.Rrect.collidepoint(point) or self.Rrect.right > WINDOWW:
                        if self.Lrect.collidepoint(point):
                            self.dir = "U"
                            return True
                        else:
                            self.dir = "L"
                            return True
                    elif self.Lrect.collidepoint(point) or self.Lrect.left< 0:
                        if self.Rrect.collidepoint(point):
                            self.dir = "U"
                            return True
                        else:
                            self.dir = "R"
                            return True
        else:
            return False
    def update(self, COL):
        self.x = WINDOWW - 3 * SPEED
        self.y = WINDOWH - 3 * SPEED
        self.Drect.centerx = self.rect.centerx
        self.Drect.centery = self.rect.centery + 24
        self.Rrect.centerx = self.rect.centerx + 24
        self.Rrect.centery = self.rect.centery
        self.Lrect.centerx = self.rect.centerx - 24
        self.Lrect.centery = self.rect.centery
        self.Urect.centerx = self.rect.centerx
        self.Urect.centery = self.rect.centery - 24
        self.Uclose.centerx = self.rect.centerx
        self.Uclose.centery = self.rect.centery - 12
        self.Lclose.centerx = self.rect.centerx - 12
        self.Lclose.centery = self.rect.centery 
        self.Dclose.centerx = self.rect.centerx
        self.Dclose.centery = self.rect.centery + 12
        self.Rclose.centerx = self.rect.centerx +12
        self.Rclose.centery = self.rect.centery 
        if self.living:
            self.check()
            if random.randint(0, 10) <= self.IQ:
                self.collisionIQ()
            #if not self.hasdirectionchanged:
              #  self.checkavoidance()
            self.hasdirectionchanged = False
            self.Rfar = 0
            self.Rnear = 0
            self.Lfar = 0
            self.Lnear = 0
            self.Ufar = 0
            self.Unear = 0
            self.Dfar = 0
            self.Dnear = 0
            
# Sets the self.dir variable. Helps ensure constant movement despite a player not pressing a button
            self.sprite_reference = self.thisimage + self.dir + ".png"
# Moves the Character's bike              
            if self.dir == "R":
                self.moveright()
            if self.dir == "D":
                self.movedown()
            if self.dir == "L":
                self.moveleft()
            if self.dir == "U":
                self.moveup()
            for Bike in Sprites:
               if (self.rect.center in Bike.prev_pos):
                   self.Stop()
            if (self.rect.center in self.prev_pos):
                self.Stop()
            self.prev_pos.append(self.rect.center)
# Actually sets the sprite, using the reference
        else:
            pygame.draw.circle(screen, (255, 20, 20), self.rect.center, 12, 1)
 
         
            self.sprite_reference = "transparent.png"
            if len(self.prev_pos) > 0:
                self.prev_pos.pop(0)
        if len(self.prev_pos) > 1:
            pygame.draw.aalines(screen,((int(4*COL/self.R) % 100) + 154, int(4*COL/self.G) % 254, int(4*COL/self.B) % 254),False,self.prev_pos)
        if len(self.prev_pos) > (TRAIL_LIMIT + lb.TB):
            self.prev_pos.pop(0)
            if len(self.prev_pos) > (TRAIL_LIMIT + lb.TB):
                self.prev_pos.pop(0)
        
        self.image = pygame.image.load(self.sprite_reference)
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





clock = pygame.time.Clock()

lb = LightBike( 1, "lights/GLOWBLUE")
lb2 = LightBike4( "R", 14, 14, 14, "tanks/GLOWBLUE")
lb3 = []
lb3.append(LightBike4("L", 11, 11, 11))
lb3.append(LightBike4("R", 11.5, 11.5, 11.5))
lb3.append(LightBike4("U", 12, 12, 12))
lb3.append(LightBike4("D", 12.5, 12.5, 12.5))
lb3.append(LightBike4("L", 13, 13, 13))
lb3.append(LightBike4("R", 13.5, 13.5, 13.5))
#lb3.append(LightBike4("U", 14, 14, 14))
#lb3.append(LightBike4("D", 14.5, 14.5, 14.5))



IsPaused = False
Sprites = pygame.sprite.Group(lb, lb2 )
Enemies = pygame.sprite.Group(lb3)
Corners = []
Corners.append((1,1))
Corners.append((WINDOWW- 2, 1))
Corners.append((WINDOWW-2, WINDOWH-2))
Corners.append((1, WINDOWH-2))
Corners.append((1,1))
Stats = pygame.font.Font("fonts/B.ttf", int(Winw * 4))
Title = pygame.font.Font("fonts/T.ttf", int(Winw * 8)) 
Credit = pygame.font.Font("fonts/F.ttf", int(Winw * 4))
Timer = pygame.font.Font("fonts/T.ttf", int(Winw * 24))

pygame.mixer.init()
Play = True
def main():
    Playerpoints = 0
    Totalpoints = 0
    pygame.mixer.music.load( 'sounds/gamemusic.mp3')
    pygame.mixer.music.play(-1)
    play = True
    xs = 1
    PAUSE = 3
    P = 0
    while play:
        CLOCKRATE = 30
        #if pygame.time.get_ticks() % 541 >= 400:
        #    lb3.append(LightBike4("U"))
        COL = pygame.time.get_ticks()
        CRED = Title.render( ("Pts/Tot: " + str(lb.Playerpoints) + "/" + str(lb.Totalpoints)) , False, (115,115,115))
        TITLE = Title.render( ("HP: "+ str(lb.HP)), False, (115,115,115))
        STATS = Title.render( "<TRON>", False, ((COL/5) % 254, (COL/ 7) % 254, (COL/9) % 254))
        pygame.event.set_blocked((pygame.MOUSEMOTION, pygame.MOUSEBUTTONUP, pygame.MOUSEBUTTONDOWN))
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            play = False
            Play = False
        if lb.living == False:
            for b in range(len(lb3)): 
                lb3[b].begin(((543*b) % (WINDOWW/SPEED - 1) + 1) * SPEED , ((554*b)% (WINDOWH/SPEED - 1) + 1) * SPEED, lb3[b].dir)
            PAUSE = 3
            for Bike in Sprites:
                lb.Playerpoints= 0
                lb.TB = 0
                Bike.begin(SPEED*10, SPEED*10, lb.dir)
        if pygame.key.get_pressed()[K_2]:
            CLOCKRATE = 15
        elif pygame.key.get_pressed()[K_3]:
            CLOCKRATE = 10
        elif pygame.key.get_pressed()[K_4]:
            CLOCKRATE = 7
        elif pygame.key.get_pressed()[K_1]:
            CLOCKRATE = 3
        if pygame.key.get_pressed()[K_p]:
            P = 1
        while P == 1:
            pygame.event.get()
            pygame.time.wait(250)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                
                    P = 0
        clock.tick(CLOCKRATE)
        pygame.mouse.set_visible(False)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False
       
        #bgi = pygame.image.load('BlackBackground.gif')
        #screen.blit(bgi,(0,0))
        screen.fill((230,230,230))
        pygame.draw.lines(screen,((COL/5) % 254, (COL/ 7) % 254, (COL/9) % 254),False, Corners, int((Winw + Winh) / 3))
        
        #Sprites.update()
        screen.blit(TITLE, ( WINDOWW/2 - TITLE.get_width() /2 , WINDOWH/2 -TITLE.get_height()))
        screen.blit(STATS, (WINDOWW/2 - STATS.get_width()/2, WINDOWH/2 ))
        screen.blit(CRED, (WINDOWW/2 - CRED.get_width()/2, WINDOWH/2 + STATS.get_height()))
        Sprites.update(pygame.time.get_ticks())
        Enemies.update(pygame.time.get_ticks())
        Sprites.draw(screen)
        Enemies.draw(screen)
        while PAUSE > 0:
            Sprites.update(pygame.time.get_ticks())
            Enemies.update(pygame.time.get_ticks())
            Sprites.draw(screen)
            Enemies.draw(screen)
            screen.fill((245,245,245,40))
            intro = Timer.render(str(PAUSE), False, ((COL/5) % 254, (COL/ 7) % 254, (COL/9) % 254))
            screen.blit(intro, ( WINDOWW/2 - TITLE.get_width() /2 , WINDOWH/2 -TITLE.get_height()))
            pygame.display.flip()
            PAUSE -= 1
            pygame.time.wait(750)
            pygame.display.flip()
        pygame.display.flip()
    pygame.mouse.set_visible(True)
    

if __name__ == "__main__":
    main()
pygame.quit()
sys.exit()
        
