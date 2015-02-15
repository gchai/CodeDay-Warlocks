import sys, random
import pygame
from pygame.locals import *
pygame.init()
import GenerateBGI
sys.path.append( 'Health/' )
import health
sys.path.append( 'ColorMod/' )
import ColorMod
sys.path.append('PowerUps/')
sys.path.append('Animation/Foxreflector/')
import CTrail, CSegment, health, ColorMod, Pup, CAI, ClassReflector, CLightBike, CCar
NUMHUM = 0
NUMAI = 0
HPCONST = 4
WARPING = True
Winw = 5.1
Winh = 3
SPEED = 12
WINDOWW=  int(18 * SPEED * Winw)
WINDOWH =  int(18 * SPEED * Winh)

dirs = ["U","R","L","D"]
clock = pygame.time.Clock()
#lb = CLightBike.LightBike( 0, 300,300, (50,20,200))
#lb2 = CLightBike.LightBike( -1, 330,310, (50,200,160))

Sprites = []
Stats = pygame.font.Font("fonts/B.ttf", int(Winw * 4))
Title = pygame.font.Font("fonts/T.ttf", int(Winw * 8)) 
Credit = pygame.font.Font("fonts/F.ttf", int(Winw * 4))
Timer = pygame.font.Font("fonts/T.ttf", int(Winw * SPEED/1.5))
pygame.mixer.init()
Play = True
def main():
    
    for i in range(NUMHUM):
        r = int(raw_input("red value for player "+str(i+1)+": "))
        g = int(raw_input("green value for player "+str(i+1)+": "))
        b = int(raw_input("blue value for player "+str(i+1)+": "))
        Sprites.append(CCar.Car(i, 100*(i+1), 100*(i+1), (r,g,b)))
    for i in range(NUMAI):
        Sprites.append(CLightBike.LightBike(-1, 300*i% WINDOWW, 400*i % WINDOWH, (130*i%200+50, 170*(i+1)*(i+1)%250, 200000/(i+1)%250)))
        Sprites[i+NUMHUM].dir = dirs[random.randint(0,4)%4]
    
    screen = pygame.display.set_mode((WINDOWW, WINDOWH))
    bgi = GenerateBGI.GenerateTron((WINDOWW,WINDOWH), 3*SPEED, (20,20,40))
    CLOCKRATE = 30
    pygame.mixer.music.load( 'sounds/gamemusic.mp3')
    pygame.mixer.music.play(-1)
    play = True
    xs = 1
    PAUSE = 5
    P = 0
    while play:
        CLOCKRATE = 30
        STATS = Title.render( "Re:Tron", False, (100,100,100))
        pygame.event.set_blocked((pygame.MOUSEMOTION, pygame.MOUSEBUTTONUP, pygame.MOUSEBUTTONDOWN))
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            play = False
            Play = False
        numdead = 0
        for bike in Sprites:
            if bike.living == False:
                numdead += 1        
            if numdead == len(Sprites) - 1:
                for bike in Sprites: 
                    bike.begin(screen, Sprites)
                    bike.hp = HPCONST
                PAUSE = 5
        if pygame.key.get_pressed()[K_1]:
            CLOCKRATE = 5
        if pygame.key.get_pressed()[K_p]:
            P = 1
        while P == 1:
            pygame.event.get()
            pygame.mixer.music.pause()
            pygame.time.wait(200)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    P = 0
                    pygame.mixer.music.unpause()
        clock.tick(CLOCKRATE)
        
        pygame.mouse.set_visible(False)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False
        screen.blit(bgi,(0,0))
        #pygame.draw.lines(screen,((COL/5) % 254, (COL/ 7) % 254, (COL/9) % 254),False, Corners, int((Winw + Winh) / 3))
        
        screen.blit(STATS, (WINDOWW/2 - STATS.get_width()/2, WINDOWH/3 ))
        for bike in Sprites:
            bike.update(screen, Sprites)
            if WARPING:
                if bike.x < 0:
                    bike.x = screen.get_width()
                    bike.Lines.append(CSegment.Segment((bike.x,bike.y),(bike.x,bike.y)))
                elif bike.x > screen.get_width():
                    bike.x = 0
                    bike.Lines.append(CSegment.Segment((bike.x,bike.y),(bike.x,bike.y)))
                if bike.y < 0:
                    bike.y = screen.get_height()
                    bike.Lines.append(CSegment.Segment((bike.x,bike.y),(bike.x,bike.y)))
                elif bike.y > screen.get_height():
                    bike.y = 0
                    bike.Lines.append(CSegment.Segment((bike.x,bike.y),(bike.x,bike.y)))
            else:
                if bike.x < 0 or bike.x > screen.get_width():
                    bike.takeDamage(1)
                if bike.y < 0 or bike.y > screen.get_height():
                    bike.takeDamage(1) 
            bike.Draw(screen)
            if bike.style != "player":
                for line in bike.AIColliders:
                    pygame.draw.lines(screen, (255,255,255), False, (line.st,line.end), 1)
        while PAUSE > 0:
            screen.fill(((PAUSE-1)*15 ,(PAUSE-1)*15,(PAUSE-1) * 15))
            for bike in Sprites:
                bike.update(screen, Sprites)
                bike.Draw(screen)
            
            intro = Timer.render((str(PAUSE) + " Use arrow keys to move " + str(PAUSE)), False, (0,100,200))
            screen.blit(intro, ( WINDOWW/2 - intro.get_width() /2 , WINDOWH/2 - intro.get_height()))
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
        
