import CSegment
import pygame
from pygame.locals import  *
pygame.init()
'''
the Trail class only provides method for manipulating segments. it doesn't
deal with splitting segments, or any collision. If you need to "split" a
segment, that must be a function within whatever objecct needs to do the split.
'''
class Trail():
    def __init__(self, x, y, col):
        '''initialize trail starting first part at x and y'''
        self.Lines = []
        self.Lines.append(CSegment.Segment((x,y),(x,y)))
        self.color = col
        
    def set_last(self, pt):
        '''sets the last segment's end to the pt provided'''
        self.Lines[-1].end[0] = pt[0]
        self.Lines[-1].end[1] = pt[1]
        
    def remove(self, index):
        '''remove the segment at the given index'''
        self.Lines.pop(index)
        
    def add_segment(self, pt):
        '''completes the last segment and adds a new one to the list at point pt'''
        self.set_last(pt)
        self.begin_segment(pt)
        
    def add_amount(self, pt):
        self.Lines[-1].end[0] += pt[0]
        self.Lines[-1].end[1] += pt[1] 
        
    def subtract_length(self, index, dist):
        x1 = self.Lines[index].st[0]
        y1 = self.Lines[index].st[1]
        x2 = self.Lines[index].end[0]
        y2 = self.Lines[index].end[1]
        if x2-x1 == 0:
            #vertical line
            if y2 < y1:
                #line points up
                self.Lines[index].st[1] = y2 + dist 
            elif y1 < y2:
                #line points down
                self.Lines[index].st[1] = y2 - dist
        elif y2-y1 == 0:
            #horizontal line
            if x2 < x1:
                #line points left
                self.Lines[index].st[1] = x2 + dist 
            elif x1 < x2:
                #line points right
                self.Lines[index].st[1] = x2 - dist
    def begin_segment(self,pt):
        self.Lines.append(CSegment.Segment((pt[0],pt[1]),(pt[0],pt[1])))
    
    def draw(self, screen, justpoints = False):
        pts = []
        pts.append((self.Lines[0].st[0],self.Lines[0].st[1]))
        for lne in self.Lines:
            pts.append((int(lne.end[0]),int(lne.end[1])))
        if justpoints:
            print "can't draw just points yet"
        else:
            pygame.draw.lines(screen, self.color, False, pts, 1)
'''            
#PL = 100
#DIR = 0
#PDIR = 0
#AMT = [[1,0],[0,-1],[-1,0],[0,1]]
#while PL > 0:
#    for e in pygame.event.get():
#        if e.type == pygame.KEYDOWN:
#            print e
            # if no unicode, use this
            # button -> key val
            # up -> 273
            # down -> 274
            # left -> 275
            # right -> 276
            if e.unicode == "d":
                DIR = 0
            elif e.unicode == "w":
                DIR = 1
            elif e.unicode == "a":
                DIR = 2
            elif e.unicode == "s":
                DIR = 3
            if e.key == 49:
                for i in Yolo.Lines:
                    print i
            if e.key == 32: # space
                PL = -200
                print "~~~~starting~~~~"
    Yolo = Trail(100,100)
    Yolo.set_last((200,100))
    Yolo.add_segment((200,100))
    Yolo.set_last((200,150))
    Yolo.add_segment((200,150))
    Yolo.set_last((30,90))
    if PDIR == DIR:
        Yolo.add_amount(AMT[DIR])
    else:
        PDIR = DIR
        Yolo.add_segment(Yolo.Lines[-1].end)
        Yolo.add_amount(AMT[DIR])
    Yolo.draw(screen)
    pygame.display.flip()

'''
