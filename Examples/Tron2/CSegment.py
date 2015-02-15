#Please only use the Segment class
import pygame 
from pygame.locals import *
#segments will not collide if they have the same end/start point
#Tboning a segment is not a collision, so it gives  an advantage
#to those who can barely scratch a corner.
def ccw(A,B,C):
    return ((C[1]-A[1])*(B[0]-A[0]) > (B[1]-A[1])*(C[0]-A[0]))
def intersect(A,B,C,D):
    return (ccw(A,C,D) != ccw(B,C,D)) and (ccw(A,B,C) != ccw(A,B,D))


class Segment():
    def __init__(self, pt1 = (0,0), pt2 = (0,0)):
        '''pt1 needs to be a Point object, as does pt2. start point = pt1, end point = pt2'''
        #self.st = start point of the segment
        self.st = [pt1[0],pt1[1]]
        #self.end = end point of the segment
        self.end = [pt2[0],pt2[1]]
        #self.lngt = the length of the segment
        
    def PRINT(self):
        print "{"+str(self.st)+":"+str(self.end)+"}"
    def draw(self, screen):
        pts = []
        pts.append((self.st[0],self.st[1]))
        pts.append((self.end[0],self.end[1]))
        pygame.draw.lines(screen, (255,255,255), False,pts,  2)    
    def length(self):
        return (((self.end[0] - self.st[0])**2 + (self.end[1] - self.st[1]) ** 2 ) ** .5)
    def collideswith(S1, S2):
        '''pass another segment to see if they collide'''
        return intersect(S1.st, S1.end, S2.st, S2.end)
#This tests collision logic. CTrail.py calls it.
def TEST():
    vert = Segment((0,-2),(0,100))
    horiz = Segment((20,0),(-5,0))
    obliq1 = Segment((-3,-4),(20, 100))
    obliq2 = Segment ((-3,4),(20, 102))
    tbone1 = Segment((0,0),(0.001,3))
    tbone2 = Segment((0,0),(0.002,2))
    print "vert-horiz test (true): " + str(vert.collideswith(horiz))
    print "vert-oblique test (true): " + str(vert.collideswith(obliq1))
    print "vert-oblique2 test (true): " + str(vert.collideswith(obliq2))
    print "horiz-oblique2 test (false): " + str(horiz.collideswith(obliq2))
    print "oblique1-2 test (false): " + str(obliq1.collideswith(obliq2))
    print "TBone endpt collision (true): " + str(tbone1.collideswith(tbone2))



        
