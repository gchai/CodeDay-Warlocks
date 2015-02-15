import CTrail, CSegment, pygame, random
# AI CODE File. This contains the Tron code for containing the AI for agressive or passive behavior.
#
#
#
#
#
#
#
#
#
#
#

#AI_NONE is func for player controlled vehicles
def AI_NONE(OBJ = None, style = "passive", num = 0,spGroup = None):
   return

#for tanks
def AI_TANK( OBJ = None, style = "passive", num = 0, spGroup = None ):
   if OBJ == None:
      return

#for jets
def AI_JET(OBJ = None, style = "passive", num = 0,spGroup= None ):
   if OBJ == None:
      return

#for cars
def AI_CAR(OBJ, style = "passive", num = 0,spGroup = None ):
   '''style can be passive, aggro, or evasive '''
   OBJ.AIColliders = []
   OBJ.AIColliders.append(CSegment.Segment((0,0),(0,0)))
   OBJ.AIColliders.append(CSegment.Segment((0,0),(0,0)))
   OBJ.AIColliders.append(CSegment.Segment((0,0),(0,0)))
   OBJ.AIColliders.append(CSegment.Segment((0,0),(0,0)))
   OBJ.AIColliders.append(CSegment.Segment((0,0),(0,0)))
   OBJ.AIColliders.append(CSegment.Segment((0,0),(0,0)))
   OBJ.AIColliders.append(CSegment.Segment((0,0),(0,0)))
   OBJ.AIColliders.append(CSegment.Segment((0,0),(0,0)))
   OBJ.AIColliders.append(CSegment.Segment((0,0),(0,0)))
   
   #self.style is the style of the AI, which can be passive, evasive, or agressive.
   if style == "evasive":
       OBJ.AIColliders.append(CSegment.Segment((0,0),(0,0)))
       OBJ.AIColliders.append(CSegment.Segment((0,0),(0,0)))
       if num >5:
           OBJ.dirChanged = True
           return
       if OBJ.dir == "U":
           OBJ.AIColliders[0].st = (OBJ.x-OBJ.speed,OBJ.y-OBJ.speed/2 )
           OBJ.AIColliders[1].st = (OBJ.x+OBJ.speed,OBJ.y-OBJ.speed/2 )
           OBJ.AIColliders[0].end = (OBJ.x-OBJ.speed,OBJ.y-2*OBJ.speed-4 )
           OBJ.AIColliders[1].end = (OBJ.x+OBJ.speed,OBJ.y-2*OBJ.speed-4 )
           
           OBJ.AIColliders[2].st = (OBJ.x-OBJ.speed/2,OBJ.y)
           OBJ.AIColliders[3].st = (OBJ.x+OBJ.speed/2,OBJ.y)
           OBJ.AIColliders[2].end = (OBJ.x-2*OBJ.speed,OBJ.y)
           OBJ.AIColliders[3].end = (OBJ.x+2*OBJ.speed,OBJ.y)

           OBJ.AIColliders[4].st = (OBJ.x-OBJ.speed,OBJ.y-2*OBJ.speed)
           OBJ.AIColliders[5].st = (OBJ.x+OBJ.speed,OBJ.y-2*OBJ.speed)
           OBJ.AIColliders[4].end = (OBJ.x-OBJ.speed,OBJ.y-5*OBJ.speed)
           OBJ.AIColliders[5].end = (OBJ.x+OBJ.speed,OBJ.y-5*OBJ.speed)
           
           OBJ.AIColliders[6].st = (OBJ.x-2*OBJ.speed,OBJ.y)
           OBJ.AIColliders[7].st = (OBJ.x+2*OBJ.speed,OBJ.y)
           OBJ.AIColliders[6].end = (OBJ.x-4*OBJ.speed,OBJ.y)
           OBJ.AIColliders[7].end = (OBJ.x+4*OBJ.speed,OBJ.y)
           
           OBJ.AIColliders[8].st = (OBJ.x-OBJ.speed/2,OBJ.y-OBJ.speed)
           OBJ.AIColliders[8].end = (OBJ.x+OBJ.speed/2, OBJ.y-OBJ.speed)
           
           OBJ.AIColliders[9].st = (OBJ.x-3*OBJ.speed, OBJ.y- 3*OBJ.speed)
           OBJ.AIColliders[10].st = (OBJ.x+3*OBJ.speed, OBJ.y - 3*OBJ.speed)
           OBJ.AIColliders[9].end = (OBJ.x-OBJ.speed, OBJ.y-5*OBJ.speed)
           OBJ.AIColliders[10].end = (OBJ.x+OBJ.speed, OBJ.y-5*OBJ.speed)
           
           A=[0,0,0,0,0,0,0,0,0,0,0]
           for i in range(len(OBJ.AIColliders)):
               for bike in spGroup:
                   if A[i]:
                       pass
                   for line in bike.Lines:
                       if OBJ.AIColliders[i].collideswith(line):
                           A[i] = True
                           break
           if (A[0] and A[1]) or A[8]:
               #dead ahead line
               if A[2] and A[3]:
                   if random.randint(0,2)>1:
                       OBJ.dir = "L"
                   else:
                       OBJ.dir = "R"
               elif A[3]:
                   OBJ.dir = "L"
               elif A[2]:
                   OBJ.dir = "R"
               elif A[6] and A[7]:
                   if random.randint(0,3) > 1:
                       OBJ.dir = "R"
                   else:
                       OBJ.dir = "L"
               elif random.randint(0,2) >= 1:
                   OBJ.dir = "L"
               else:
                   OBJ.dir = "R"
           elif A[0] and not A[3]:
               OBJ.dir = "R"
           elif A[1] and not A[2]:
               OBJ.dir = "L"
           elif A[3]:
               OBJ.dir = "L"
           elif A[2]:
               OBJ.dir = "R"
           elif A[4] or A[5]: #ufar
               if A[2] and A[3]:
                   pass    
               elif A[3]:
                   OBJ.dir = "L"
                   if random.randint(0,7)>6:
                       OBJ.Action()
               elif A[2]:
                   OBJ.dir = "R"
                   if random.randint(0,7)>6:
                       OBJ.Action()
               elif A[6]:
                   OBJ.dir = "R"
                   if random.randint(0,7)>6:
                       OBJ.Action()
               elif A[7]:
                   OBJ.dir = "L"
                   if random.randint(0,7)>6:
                       OBJ.Action()
           elif A[9] and not (A[3]or A[7] or A[10]) and random.randint(0,5)>4:
               OBJ.dir = "R"
               OBJ.Action()
           elif A[10] and not (A[2]or A[6] or A[9]) and random.randint(0,5)>4:
               OBJ.dir = "L"
               OBJ.Action()
           elif A[9] and A[2]:
               OBJ.dir = "R"
               OBJ.Action()
           elif A[10] and A[3]:
               OBJ.dir = "L"
               OBJ.Action()
               
       if OBJ.dir == "D":
           OBJ.AIColliders[0].st = (OBJ.x+OBJ.speed,OBJ.y+OBJ.speed/2 )
           OBJ.AIColliders[1].st = (OBJ.x-OBJ.speed,OBJ.y+OBJ.speed/2 )
           OBJ.AIColliders[0].end = (OBJ.x+OBJ.speed,OBJ.y+2*OBJ.speed+4 )
           OBJ.AIColliders[1].end = (OBJ.x-OBJ.speed,OBJ.y+2*OBJ.speed+4 )
           
           OBJ.AIColliders[2].st = (OBJ.x+OBJ.speed/2,OBJ.y)
           OBJ.AIColliders[3].st = (OBJ.x-OBJ.speed/2,OBJ.y)
           OBJ.AIColliders[2].end = (OBJ.x+2*OBJ.speed,OBJ.y)
           OBJ.AIColliders[3].end = (OBJ.x-2*OBJ.speed,OBJ.y)

           OBJ.AIColliders[4].st = (OBJ.x+OBJ.speed,OBJ.y+2*OBJ.speed)
           OBJ.AIColliders[5].st = (OBJ.x-OBJ.speed,OBJ.y+2*OBJ.speed)
           OBJ.AIColliders[4].end = (OBJ.x+OBJ.speed,OBJ.y+5*OBJ.speed)
           OBJ.AIColliders[5].end = (OBJ.x-OBJ.speed,OBJ.y+5*OBJ.speed)
           
           OBJ.AIColliders[6].st = (OBJ.x+2*OBJ.speed,OBJ.y)
           OBJ.AIColliders[7].st = (OBJ.x-2*OBJ.speed,OBJ.y)
           OBJ.AIColliders[6].end = (OBJ.x+4*OBJ.speed,OBJ.y)
           OBJ.AIColliders[7].end = (OBJ.x-4*OBJ.speed,OBJ.y)
           
           OBJ.AIColliders[8].st = (OBJ.x+OBJ.speed/2,OBJ.y+OBJ.speed)
           OBJ.AIColliders[8].end = (OBJ.x-OBJ.speed/2, OBJ.y+OBJ.speed)
           
           OBJ.AIColliders[9].st = (OBJ.x+3*OBJ.speed, OBJ.y+ 3*OBJ.speed)
           OBJ.AIColliders[10].st = (OBJ.x+3*OBJ.speed, OBJ.y + 3*OBJ.speed)
           OBJ.AIColliders[9].end = (OBJ.x+OBJ.speed, OBJ.y+5*OBJ.speed)
           OBJ.AIColliders[10].end = (OBJ.x-OBJ.speed, OBJ.y+5*OBJ.speed)
           
           A=[0,0,0,0,0,0,0,0,0,0,0]
           for i in range(len(OBJ.AIColliders)):
               for bike in spGroup:
                   if A[i]:
                       pass
                   for line in bike.Lines:
                       if OBJ.AIColliders[i].collideswith(line):
                           A[i] = True
                           break
           if (A[0] and A[1]) or A[8]:
               #dead ahead line
               if A[2] and A[3]:
                   if random.randint(0,2)>1:
                       OBJ.dir = "R"
                   else:
                       OBJ.dir = "L"
               elif A[3]:
                   OBJ.dir = "R"
               elif A[2]:
                   OBJ.dir = "L"
               elif A[6] and A[7]:
                   if random.randint(0,3) > 1:
                       OBJ.dir = "L"
                   else:
                       OBJ.dir = "R"
               elif random.randint(0,2) >= 1:
                   OBJ.dir = "R"
               else:
                   OBJ.dir = "L"
           elif A[0] and not A[3]:
               OBJ.dir = "L"
           elif A[1] and not A[2]:
               OBJ.dir = "R"
           elif A[3]:
               OBJ.dir = "R"
           elif A[2]:
               OBJ.dir = "L"
           elif A[4] or A[5]: #ufar
               if A[2] and A[3]:
                   pass    
               elif A[3]:
                   OBJ.dir = "R"
                   if random.randint(0,7)>6:
                       OBJ.Action()
               elif A[2]:
                   OBJ.dir = "L"
                   if random.randint(0,7)>6:
                       OBJ.Action()
               elif A[6]:
                   OBJ.dir = "L"
                   if random.randint(0,7)>6:
                       OBJ.Action()
               elif A[7]:
                   OBJ.dir = "R"
                   if random.randint(0,7)>6:
                       OBJ.Action()
           elif A[9] and not (A[3]or A[7] or A[10]) and random.randint(0,5)>4:
               OBJ.dir = "L"
               OBJ.Action()
           elif A[10] and not (A[2]or A[6] or A[9]) and random.randint(0,5)>4:
               OBJ.dir = "R"
               OBJ.Action()
           elif A[9] and A[2]:
               OBJ.dir = "L"
               OBJ.Action()
           elif A[10] and A[3]:
               OBJ.dir = "R"
               OBJ.Action()      
       
       if OBJ.dir == "R":
           OBJ.AIColliders[0].st = (OBJ.x+OBJ.speed/2,OBJ.y-OBJ.speed )
           OBJ.AIColliders[1].st = (OBJ.x+OBJ.speed/2,OBJ.y+OBJ.speed )
           OBJ.AIColliders[0].end = (OBJ.x+2*OBJ.speed+4,OBJ.y-OBJ.speed )
           OBJ.AIColliders[1].end = (OBJ.x+2*OBJ.speed+4,OBJ.y+OBJ.speed )
           
           OBJ.AIColliders[2].st = (OBJ.x,OBJ.y-OBJ.speed/2)
           OBJ.AIColliders[3].st = (OBJ.x,OBJ.y+OBJ.speed/2)
           OBJ.AIColliders[2].end = (OBJ.x,OBJ.y-2*OBJ.speed)
           OBJ.AIColliders[3].end = (OBJ.x,OBJ.y+2*OBJ.speed)

           OBJ.AIColliders[4].st = (OBJ.x+2*OBJ.speed,OBJ.y-OBJ.speed)
           OBJ.AIColliders[5].st = (OBJ.x+2*OBJ.speed,OBJ.y+OBJ.speed)
           OBJ.AIColliders[4].end = (OBJ.x+5*OBJ.speed,OBJ.y-OBJ.speed)
           OBJ.AIColliders[5].end = (OBJ.x+5*OBJ.speed,OBJ.y+OBJ.speed)
           
           OBJ.AIColliders[6].st = (OBJ.x,OBJ.y-2*OBJ.speed)
           OBJ.AIColliders[7].st = (OBJ.x,OBJ.y+2*OBJ.speed)
           OBJ.AIColliders[6].end = (OBJ.x,OBJ.y-4*OBJ.speed)
           OBJ.AIColliders[7].end = (OBJ.x,OBJ.y+4*OBJ.speed)
           
           OBJ.AIColliders[8].st = (OBJ.x+OBJ.speed,OBJ.y-OBJ.speed/2)
           OBJ.AIColliders[8].end = (OBJ.x+OBJ.speed, OBJ.y+OBJ.speed/2)
           
           OBJ.AIColliders[9].st = (OBJ.x+3*OBJ.speed, OBJ.y- 3*OBJ.speed)
           OBJ.AIColliders[10].st = (OBJ.x+3*OBJ.speed, OBJ.y + 3*OBJ.speed)
           OBJ.AIColliders[9].end = (OBJ.x+5*OBJ.speed, OBJ.y-OBJ.speed)
           OBJ.AIColliders[10].end = (OBJ.x+5*OBJ.speed, OBJ.y+OBJ.speed)
           
           A=[0,0,0,0,0,0,0,0,0,0,0]
           for i in range(len(OBJ.AIColliders)):
               for bike in spGroup:
                   if A[i]:
                       pass
                   for line in bike.Lines:
                       if OBJ.AIColliders[i].collideswith(line):
                           A[i] = True
                           break
           if (A[0] and A[1]) or A[8]:
               #dead ahead line
               if A[2] and A[3]:
                   if random.randint(0,2)>1:
                       OBJ.dir = "U"
                   else:
                       OBJ.dir = "D"
               elif A[3]:
                   OBJ.dir = "U"
               elif A[2]:
                   OBJ.dir = "D"
               elif A[6] and A[7]:
                   if random.randint(0,3) > 1:
                       OBJ.dir = "D"
                   else:
                       OBJ.dir = "U"
               elif random.randint(0,2) >= 1:
                   OBJ.dir = "U"
               else:
                   OBJ.dir = "D"
           elif A[0] and not A[3]:
               OBJ.dir = "D"
           elif A[1] and not A[2]:
               OBJ.dir = "U"
           elif A[3]:
               OBJ.dir = "U"
           elif A[2]:
               OBJ.dir = "D"
           elif A[4] or A[5]: #ufar
               if A[2] and A[3]:
                   pass    
               elif A[3]:
                   OBJ.dir = "U"
                   if random.randint(0,7)>6:
                       OBJ.Action()
               elif A[2]:
                   OBJ.dir = "D"
                   if random.randint(0,7)>6:
                       OBJ.Action()
               elif A[6]:
                   OBJ.dir = "D"
                   if random.randint(0,7)>6:
                       OBJ.Action()
               elif A[7]:
                   OBJ.dir = "U"
                   if random.randint(0,7)>6:
                       OBJ.Action()
           elif A[9] and not (A[3]or A[7] or A[10]) and random.randint(0,5)>4:
               OBJ.dir = "D"
               OBJ.Action()
           elif A[10] and not (A[2]or A[6] or A[9]) and random.randint(0,5)>4:
               OBJ.dir = "U"
               OBJ.Action()
           elif A[9] and A[2]:
               OBJ.dir = "D"
               OBJ.Action()
           elif A[10] and A[3]:
               OBJ.dir = "U"
               OBJ.Action()
       if OBJ.dir == "L":
           OBJ.AIColliders[0].st = (OBJ.x-OBJ.speed/2,OBJ.y+OBJ.speed )
           OBJ.AIColliders[1].st = (OBJ.x-OBJ.speed/2,OBJ.y-OBJ.speed )
           OBJ.AIColliders[0].end = (OBJ.x-2*OBJ.speed+4,OBJ.y+OBJ.speed )
           OBJ.AIColliders[1].end = (OBJ.x-2*OBJ.speed+4,OBJ.y-OBJ.speed )
           
           OBJ.AIColliders[2].st = (OBJ.x,OBJ.y+OBJ.speed/2)
           OBJ.AIColliders[3].st = (OBJ.x,OBJ.y-OBJ.speed/2)
           OBJ.AIColliders[2].end = (OBJ.x,OBJ.y+2*OBJ.speed)
           OBJ.AIColliders[3].end = (OBJ.x,OBJ.y-2*OBJ.speed)

           OBJ.AIColliders[4].st = (OBJ.x-2*OBJ.speed,OBJ.y+OBJ.speed)
           OBJ.AIColliders[5].st = (OBJ.x-2*OBJ.speed,OBJ.y-OBJ.speed)
           OBJ.AIColliders[4].end = (OBJ.x-5*OBJ.speed,OBJ.y+OBJ.speed)
           OBJ.AIColliders[5].end = (OBJ.x-5*OBJ.speed,OBJ.y-OBJ.speed)
           
           OBJ.AIColliders[6].st = (OBJ.x,OBJ.y+2*OBJ.speed)
           OBJ.AIColliders[7].st = (OBJ.x,OBJ.y-2*OBJ.speed)
           OBJ.AIColliders[6].end = (OBJ.x,OBJ.y+4*OBJ.speed)
           OBJ.AIColliders[7].end = (OBJ.x,OBJ.y-4*OBJ.speed)
           
           OBJ.AIColliders[8].st = (OBJ.x-OBJ.speed,OBJ.y+OBJ.speed/2)
           OBJ.AIColliders[8].end = (OBJ.x-OBJ.speed, OBJ.y-OBJ.speed/2)
           
           OBJ.AIColliders[9].st = (OBJ.x-3*OBJ.speed, OBJ.y+3*OBJ.speed)
           OBJ.AIColliders[10].st = (OBJ.x-3*OBJ.speed, OBJ.y-3*OBJ.speed)
           OBJ.AIColliders[9].end = (OBJ.x-5*OBJ.speed, OBJ.y+OBJ.speed)
           OBJ.AIColliders[10].end = (OBJ.x-5*OBJ.speed, OBJ.y-OBJ.speed)
           
           A=[0,0,0,0,0,0,0,0,0,0,0]
           for i in range(len(OBJ.AIColliders)):
               for bike in spGroup:
                   if A[i]:
                       pass
                   for line in bike.Lines:
                       if OBJ.AIColliders[i].collideswith(line):
                           A[i] = True
                           break
           if (A[0] and A[1]) or A[8]:
               #dead ahead line
               if A[2] and A[3]:
                   if random.randint(0,2)>1:
                       OBJ.dir = "D"
                   else:
                       OBJ.dir = "U"
               elif A[3]:
                   OBJ.dir = "D"
               elif A[2]:
                   OBJ.dir = "U"
               elif A[6] and A[7]:
                   if random.randint(0,3) > 1:
                       OBJ.dir = "U"
                   else:
                       OBJ.dir = "D"
               elif random.randint(0,2) >= 1:
                   OBJ.dir = "D"
               else:
                   OBJ.dir = "U"
           elif A[0] and not A[3]:
               OBJ.dir = "U"
           elif A[1] and not A[2]:
               OBJ.dir = "D"
           elif A[3]:
               OBJ.dir = "D"
           elif A[2]:
               OBJ.dir = "U"
           elif A[4] or A[5]: #ufar
               if A[2] and A[3]:
                   pass    
               elif A[3]:
                   OBJ.dir = "D"
                   if random.randint(0,7)>6:
                       OBJ.Action()
               elif A[2]:
                   OBJ.dir = "U"
                   if random.randint(0,7)>6:
                       OBJ.Action()
               elif A[6]:
                   OBJ.dir = "U"
                   if random.randint(0,7)>6:
                       OBJ.Action()
               elif A[7]:
                   OBJ.dir = "D"
                   if random.randint(0,7)>6:
                       OBJ.Action()
           elif A[9] and not (A[3]or A[7] or A[10]) and random.randint(0,5)>4:
               OBJ.dir = "U"
               OBJ.Action()
           elif A[10] and not (A[2]or A[6] or A[9]) and random.randint(0,5)>4:
               OBJ.dir = "D"
               OBJ.Action()
           elif A[9] and A[2]:
               OBJ.dir = "U"
               OBJ.Action()
           elif A[10] and A[3]:
               OBJ.dir = "D"
               OBJ.Action()     
               
               
   elif style == "aggro":
       if num > 5:
           OBJ.dirChanged = True
           return
       OBJ.AIColliders.append(CSegment.Segment((0,0),(0,0)))
       OBJ.AIColliders.append(CSegment.Segment((0,0),(0,0)))
       if OBJ.dir == "U":
           OBJ.AIColliders[0].st = (OBJ.x-OBJ.speed/2,OBJ.y-OBJ.speed/2 )
           OBJ.AIColliders[1].st = (OBJ.x+OBJ.speed/2,OBJ.y-OBJ.speed/2 )
           OBJ.AIColliders[0].end = (OBJ.x-OBJ.speed,OBJ.y-2*OBJ.speed-4 )
           OBJ.AIColliders[1].end = (OBJ.x+OBJ.speed,OBJ.y-2*OBJ.speed-4 )
           
           OBJ.AIColliders[2].st = (OBJ.x-OBJ.speed/2,OBJ.y)
           OBJ.AIColliders[3].st = (OBJ.x+OBJ.speed/2,OBJ.y)
           OBJ.AIColliders[2].end = (OBJ.x-2*OBJ.speed,OBJ.y)
           OBJ.AIColliders[3].end = (OBJ.x+2*OBJ.speed,OBJ.y)

           OBJ.AIColliders[4].st = (OBJ.x-OBJ.speed-1,OBJ.y-2*OBJ.speed)
           OBJ.AIColliders[5].st = (OBJ.x+OBJ.speed+1,OBJ.y-2*OBJ.speed)
           OBJ.AIColliders[4].end = (OBJ.x,OBJ.y-5*OBJ.speed)
           OBJ.AIColliders[5].end = (OBJ.x,OBJ.y-5*OBJ.speed)
           
           OBJ.AIColliders[6].st = (OBJ.x-2*OBJ.speed,OBJ.y)
           OBJ.AIColliders[7].st = (OBJ.x+2*OBJ.speed,OBJ.y)
           OBJ.AIColliders[6].end = (OBJ.x-3.5*OBJ.speed,OBJ.y)
           OBJ.AIColliders[7].end = (OBJ.x+3.5*OBJ.speed,OBJ.y)
           
           OBJ.AIColliders[8].st = (OBJ.x-OBJ.speed/2,OBJ.y-OBJ.speed)
           OBJ.AIColliders[8].end = (OBJ.x+OBJ.speed/2, OBJ.y-OBJ.speed)
           
           OBJ.AIColliders[9].st = (OBJ.x-OBJ.speed/2,OBJ.y+3*OBJ.speed)
           OBJ.AIColliders[10].st = (OBJ.x+OBJ.speed/2, OBJ.y+3*OBJ.speed)
           OBJ.AIColliders[9].end = (OBJ.x-OBJ.speed,OBJ.y+OBJ.speed*6)
           OBJ.AIColliders[10].end = (OBJ.x+OBJ.speed, OBJ.y+OBJ.speed*6)
           A=[0,0,0,0,0,0,0,0,0,0,0]
           for i in range(len(OBJ.AIColliders)):
               for bike in spGroup:
                   if A[i]:
                       pass
                   for line in bike.Lines:
                       if OBJ.AIColliders[i].collideswith(line):
                           if i != 9 and i != 10:
                               A[i] = True
                           elif bike != OBJ:
                               A[i] = True
                           break
           if (A[0] and A[1]) or A[8]:
               #dead ahead line
               if A[2] and A[3]:
                   OBJ.Action()
               elif A[3]:
                   OBJ.dir = "L"
               elif A[2]:
                   OBJ.dir = "R"
               elif A[6] and A[7]:
                   if random.randint(0,3) > 1:
                       OBJ.dir = "R"
                   else:
                       OBJ.dir = "L"
               elif random.randint(0,2) >= 1:
                   OBJ.dir = "L"
               else:
                   OBJ.dir = "R"
           elif A[0]:
               OBJ.dir = "R"
           elif A[1]:
               OBJ.dir = "L"
           elif A[4] or A[5]: #ufar
               if A[2] and A[3]:
                   OBJ.Action()    
               elif A[3]:
                   OBJ.dir = "L"
               elif A[2]:
                   OBJ.dir = "R"
               elif A[6]:
                   OBJ.dir = "R"
               elif A[7]:
                   OBJ.dir = "L"
           elif A[9] and not (A[0] or A[2] or A[6] or A[10]):
               OBJ.Action()
           elif A[10] and not (A[1] or A[3] or A[7] or A[9]):
               OBJ.Action()
           elif A[6] and not A[3] and random.randint(0,35) > 28:
               OBJ.dir = "R"
           elif A[7] and not A[2] and random.randint(0,35) > 28:
               OBJ.dir = "L"

       if OBJ.dir == "D":
           OBJ.AIColliders[0].st = (OBJ.x+OBJ.speed/2,OBJ.y+OBJ.speed/2 )
           OBJ.AIColliders[1].st = (OBJ.x-OBJ.speed/2,OBJ.y+OBJ.speed/2 )
           OBJ.AIColliders[0].end = (OBJ.x+OBJ.speed,OBJ.y+2*OBJ.speed+4 )
           OBJ.AIColliders[1].end = (OBJ.x-OBJ.speed,OBJ.y+2*OBJ.speed+4 )
           
           OBJ.AIColliders[2].st = (OBJ.x+OBJ.speed/2,OBJ.y)
           OBJ.AIColliders[3].st = (OBJ.x-OBJ.speed/2,OBJ.y)
           OBJ.AIColliders[2].end = (OBJ.x+2*OBJ.speed,OBJ.y)
           OBJ.AIColliders[3].end = (OBJ.x-2*OBJ.speed,OBJ.y)

           OBJ.AIColliders[4].st = (OBJ.x+OBJ.speed+1,OBJ.y+2*OBJ.speed)
           OBJ.AIColliders[5].st = (OBJ.x-OBJ.speed-1,OBJ.y+2*OBJ.speed)
           OBJ.AIColliders[4].end = (OBJ.x,OBJ.y+5*OBJ.speed)
           OBJ.AIColliders[5].end = (OBJ.x,OBJ.y+5*OBJ.speed)
           
           OBJ.AIColliders[6].st = (OBJ.x+2*OBJ.speed,OBJ.y)
           OBJ.AIColliders[7].st = (OBJ.x-2*OBJ.speed,OBJ.y)
           OBJ.AIColliders[6].end = (OBJ.x+3.5*OBJ.speed,OBJ.y)
           OBJ.AIColliders[7].end = (OBJ.x-3.5*OBJ.speed,OBJ.y)
           
           OBJ.AIColliders[8].st = (OBJ.x+OBJ.speed/2,OBJ.y+OBJ.speed)
           OBJ.AIColliders[8].end = (OBJ.x-OBJ.speed/2, OBJ.y+OBJ.speed)
           
           OBJ.AIColliders[9].st = (OBJ.x+OBJ.speed/2,OBJ.y-3*OBJ.speed)
           OBJ.AIColliders[10].st = (OBJ.x-OBJ.speed/2, OBJ.y-3*OBJ.speed)
           OBJ.AIColliders[9].end = (OBJ.x+OBJ.speed,OBJ.y-OBJ.speed*6)
           OBJ.AIColliders[10].end = (OBJ.x-OBJ.speed, OBJ.y-OBJ.speed*6)
           A=[0,0,0,0,0,0,0,0,0,0,0]
           for i in range(len(OBJ.AIColliders)):
               for bike in spGroup:
                   if A[i]:
                       pass
                   for line in bike.Lines:
                       if OBJ.AIColliders[i].collideswith(line):
                           if i != 9 and i != 10:
                               A[i] = True
                           elif bike != OBJ:
                               A[i] = True
                           break
           if (A[0] and A[1]) or A[8]:
               #dead ahead line
               if A[2] and A[3]:
                   OBJ.Action()
               elif A[3]:
                   OBJ.dir = "R"
               elif A[2]:
                   OBJ.dir = "L"
               elif A[6] and A[7]:
                   if random.randint(0,3) > 1:
                       OBJ.dir = "L"
                   else:
                       OBJ.dir = "R"
               elif random.randint(0,2) >= 1:
                   OBJ.dir = "R"
               else:
                   OBJ.dir = "L"
           elif A[0]:
               OBJ.dir = "L"
           elif A[1]:
               OBJ.dir = "R"
           elif A[4] or A[5]: #ufar
               if A[2] and A[3]:
                   OBJ.Action()    
               elif A[3]:
                   OBJ.dir = "R"
               elif A[2]:
                   OBJ.dir = "L"
               elif A[6]:
                   OBJ.dir = "L"
               elif A[7]:
                   OBJ.dir = "R"
           elif A[9] and not (A[0] or A[2] or A[6] or A[10]):
               OBJ.Action()
           elif A[10] and not (A[1] or A[3] or A[7] or A[9]):
               OBJ.Action()
           elif A[6] and not A[3] and random.randint(0,35) > 28:
               OBJ.dir = "L"
           elif A[7] and not A[2] and random.randint(0,35) > 28:
               OBJ.dir = "R"

       if OBJ.dir == "L":
           OBJ.AIColliders[0].st = (OBJ.x-OBJ.speed/2,OBJ.y+OBJ.speed/2 )
           OBJ.AIColliders[1].st = (OBJ.x-OBJ.speed/2,OBJ.y-OBJ.speed/2 )
           OBJ.AIColliders[0].end = (OBJ.x-2*OBJ.speed-4,OBJ.y+OBJ.speed/2 )
           OBJ.AIColliders[1].end = (OBJ.x-2*OBJ.speed-4,OBJ.y-OBJ.speed/2 )
           
           OBJ.AIColliders[2].st = (OBJ.x,OBJ.y+OBJ.speed/2)
           OBJ.AIColliders[3].st = (OBJ.x,OBJ.y-OBJ.speed/2)
           OBJ.AIColliders[2].end = (OBJ.x,OBJ.y+2*OBJ.speed)
           OBJ.AIColliders[3].end = (OBJ.x,OBJ.y-2*OBJ.speed)

           OBJ.AIColliders[4].st = (OBJ.x-2*OBJ.speed,OBJ.y+OBJ.speed)
           OBJ.AIColliders[5].st = (OBJ.x-2*OBJ.speed,OBJ.y-OBJ.speed)
           OBJ.AIColliders[4].end = (OBJ.x-5*OBJ.speed,OBJ.y)
           OBJ.AIColliders[5].end = (OBJ.x-5*OBJ.speed,OBJ.y)
           
           OBJ.AIColliders[6].st = (OBJ.x,OBJ.y+2*OBJ.speed)
           OBJ.AIColliders[7].st = (OBJ.x,OBJ.y-2*OBJ.speed)
           OBJ.AIColliders[6].end = (OBJ.x,OBJ.y+3.5*OBJ.speed)
           OBJ.AIColliders[7].end = (OBJ.x,OBJ.y-3.5*OBJ.speed)
           
           OBJ.AIColliders[8].st = (OBJ.x-OBJ.speed,OBJ.y-OBJ.speed/2)
           OBJ.AIColliders[8].end = (OBJ.x-OBJ.speed, OBJ.y+OBJ.speed/2)
           
           OBJ.AIColliders[9].st = (OBJ.x+3*OBJ.speed ,OBJ.y+OBJ.speed/2)
           OBJ.AIColliders[10].st = (OBJ.x+3*OBJ.speed, OBJ.y-OBJ.speed/2)
           OBJ.AIColliders[9].end = (OBJ.x+OBJ.speed*6,OBJ.y+OBJ.speed)
           OBJ.AIColliders[10].end = (OBJ.x+OBJ.speed*6, OBJ.y-OBJ.speed)
           A=[0,0,0,0,0,0,0,0,0,0,0]
           for i in range(len(OBJ.AIColliders)):
               for bike in spGroup:
                   if A[i]:
                       pass
                   for line in bike.Lines:
                       if OBJ.AIColliders[i].collideswith(line):
                           if i != 9 and i != 10:
                               A[i] = True
                           elif bike != OBJ:
                               A[i] = True
                           break
           if (A[0] and A[1]) or A[8]:
               #dead ahead line
               if A[2] and A[3]:
                   OBJ.Action()
               elif A[3]:
                   OBJ.dir = "D"
               elif A[2]:
                   OBJ.dir = "U"
               elif A[6] and A[7]:
                   if random.randint(0,3) > 1:
                       OBJ.dir = "U"
                   else:
                       OBJ.dir = "D"
               elif random.randint(0,2) >= 1:
                   OBJ.dir = "D"
               else:
                   OBJ.dir = "U"
           elif A[0]:
               OBJ.dir = "U"
           elif A[1]:
               OBJ.dir = "D"
           elif A[4] or A[5]: #ufar
               if A[2] and A[3]:
                   OBJ.Action()    
               elif A[3]:
                   OBJ.dir = "D"
               elif A[2]:
                   OBJ.dir = "U"
               elif A[6]:
                   OBJ.dir = "U"
               elif A[7]:
                   OBJ.dir = "D"
           elif A[9] and not (A[0] or A[2] or A[6] or A[10]):
               OBJ.Action()
           elif A[10] and not (A[1] or A[3] or A[7] or A[9]):
               OBJ.Action()
           elif A[6] and not A[3] and random.randint(0,35) > 28:
               OBJ.dir = "U"
           elif A[7] and not A[2] and random.randint(0,35) > 28:
               OBJ.dir = "D"

       if OBJ.dir == "R":
           OBJ.AIColliders[0].st = (OBJ.x+OBJ.speed/2,OBJ.y-OBJ.speed/2 )
           OBJ.AIColliders[1].st = (OBJ.x+OBJ.speed/2,OBJ.y+OBJ.speed/2 )
           OBJ.AIColliders[0].end = (OBJ.x+2*OBJ.speed+4,OBJ.y-OBJ.speed/2 )
           OBJ.AIColliders[1].end = (OBJ.x+2*OBJ.speed+4,OBJ.y+OBJ.speed/2 )
           
           OBJ.AIColliders[2].st = (OBJ.x,OBJ.y-OBJ.speed/2)
           OBJ.AIColliders[3].st = (OBJ.x,OBJ.y+OBJ.speed/2)
           OBJ.AIColliders[2].end = (OBJ.x,OBJ.y-2*OBJ.speed)
           OBJ.AIColliders[3].end = (OBJ.x,OBJ.y+2*OBJ.speed)

           OBJ.AIColliders[4].st = (OBJ.x+2*OBJ.speed,OBJ.y-OBJ.speed)
           OBJ.AIColliders[5].st = (OBJ.x+2*OBJ.speed,OBJ.y+OBJ.speed)
           OBJ.AIColliders[4].end = (OBJ.x+5*OBJ.speed,OBJ.y)
           OBJ.AIColliders[5].end = (OBJ.x+5*OBJ.speed,OBJ.y)
           
           OBJ.AIColliders[6].st = (OBJ.x,OBJ.y-2*OBJ.speed)
           OBJ.AIColliders[7].st = (OBJ.x,OBJ.y+2*OBJ.speed)
           OBJ.AIColliders[6].end = (OBJ.x,OBJ.y-3.5*OBJ.speed)
           OBJ.AIColliders[7].end = (OBJ.x,OBJ.y+3.5*OBJ.speed)
           
           OBJ.AIColliders[8].st = (OBJ.x+OBJ.speed,OBJ.y+OBJ.speed/2)
           OBJ.AIColliders[8].end = (OBJ.x+OBJ.speed, OBJ.y-OBJ.speed/2)
           
           OBJ.AIColliders[9].st = (OBJ.x-3*OBJ.speed ,OBJ.y-OBJ.speed/2)
           OBJ.AIColliders[10].st = (OBJ.x-3*OBJ.speed, OBJ.y+OBJ.speed/2)
           OBJ.AIColliders[9].end = (OBJ.x-OBJ.speed*6,OBJ.y-OBJ.speed)
           OBJ.AIColliders[10].end = (OBJ.x-OBJ.speed*6, OBJ.y+OBJ.speed)
           A=[0,0,0,0,0,0,0,0,0,0,0]
           for i in range(len(OBJ.AIColliders)):
               for bike in spGroup:
                   if A[i]:
                       pass
                   for line in bike.Lines:
                       if OBJ.AIColliders[i].collideswith(line):
                           if i != 9 and i != 10:
                               A[i] = True
                           elif bike != OBJ:
                               A[i] = True
                           break
           if (A[0] and A[1]) or A[8]:
               #dead ahead line
               if A[2] and A[3]:
                   OBJ.Action()
               elif A[3]:
                   OBJ.dir = "U"
               elif A[2]:
                   OBJ.dir = "D"
               elif A[6] and A[7]:
                   if random.randint(0,3) > 1:
                       OBJ.dir = "D"
                   else:
                       OBJ.dir = "U"
               elif random.randint(0,2) >= 1:
                   OBJ.dir = "U"
               else:
                   OBJ.dir = "D"
           elif A[0]:
               OBJ.dir = "D"
           elif A[1]:
               OBJ.dir = "U"
           elif A[4] or A[5]: #ufar
               if A[2] and A[3]:
                   OBJ.Action()    
               elif A[3]:
                   OBJ.dir = "U"
               elif A[2]:
                   OBJ.dir = "D"
               elif A[6]:
                   OBJ.dir = "D"
               elif A[7]:
                   OBJ.dir = "U"
           elif A[9] and not (A[0] or A[2] or A[6] or A[10]):
               OBJ.Action()
           elif A[10] and not (A[1] or A[3] or A[7] or A[9]):
               OBJ.Action()
           elif A[6] and not A[3] and random.randint(0,35) > 28:
               OBJ.dir = "D"
           elif A[7] and not A[2] and random.randint(0,35) > 28:
               OBJ.dir = "U"

   # now if it's passive
   else:
       if num > 5:
           OBJ.dirChanged = True
           return
       if OBJ.dir == "U":
           OBJ.AIColliders[0].st = (OBJ.x-OBJ.speed,OBJ.y-OBJ.speed/2 )
           OBJ.AIColliders[1].st = (OBJ.x+OBJ.speed,OBJ.y-OBJ.speed/2 )
           OBJ.AIColliders[0].end = (OBJ.x-OBJ.speed,OBJ.y-2*OBJ.speed-4 )
           OBJ.AIColliders[1].end = (OBJ.x+OBJ.speed,OBJ.y-2*OBJ.speed-4 )
           
           OBJ.AIColliders[2].st = (OBJ.x-OBJ.speed/2,OBJ.y)
           OBJ.AIColliders[3].st = (OBJ.x+OBJ.speed/2,OBJ.y)
           OBJ.AIColliders[2].end = (OBJ.x-2*OBJ.speed,OBJ.y)
           OBJ.AIColliders[3].end = (OBJ.x+2*OBJ.speed,OBJ.y)

           OBJ.AIColliders[4].st = (OBJ.x-OBJ.speed,OBJ.y-2*OBJ.speed)
           OBJ.AIColliders[5].st = (OBJ.x+OBJ.speed,OBJ.y-2*OBJ.speed)
           OBJ.AIColliders[4].end = (OBJ.x-OBJ.speed,OBJ.y-5*OBJ.speed)
           OBJ.AIColliders[5].end = (OBJ.x+OBJ.speed,OBJ.y-5*OBJ.speed)
           
           OBJ.AIColliders[6].st = (OBJ.x-2*OBJ.speed,OBJ.y)
           OBJ.AIColliders[7].st = (OBJ.x+2*OBJ.speed,OBJ.y)
           OBJ.AIColliders[6].end = (OBJ.x-4*OBJ.speed,OBJ.y)
           OBJ.AIColliders[7].end = (OBJ.x+4*OBJ.speed,OBJ.y)
           
           OBJ.AIColliders[8].st = (OBJ.x-OBJ.speed/2,OBJ.y-OBJ.speed)
           OBJ.AIColliders[8].end = (OBJ.x+OBJ.speed/2, OBJ.y-OBJ.speed)
           A=[0,0,0,0,0,0,0,0,0]
           for i in range(len(OBJ.AIColliders)):
               for bike in spGroup:
                   if A[i]:
                       pass
                   for line in bike.Lines:
                       if OBJ.AIColliders[i].collideswith(line):
                           A[i] = True
                           break
           if (A[0] and A[1]) or A[8]:
               #dead ahead line
               if A[2] and A[3]:
                   OBJ.Action()
               elif A[3]:
                   OBJ.dir = "L"
               elif A[2]:
                   OBJ.dir = "R"
               elif A[6] and A[7]:
                   if random.randint(0,3) > 1:
                       OBJ.dir = "R"
                   else:
                       OBJ.dir = "L"
               elif random.randint(0,2) >= 1:
                   OBJ.dir = "L"
               else:
                   OBJ.dir = "R"
           elif A[0]:
               OBJ.dir = "R"
           elif A[1]:
               OBJ.dir = "L"
           elif A[4] or A[5]: #ufar
               if A[2] and A[3]:
                   OBJ.Action()    
               elif A[3]:
                   OBJ.dir = "L"
               elif A[2]:
                   OBJ.dir = "R"
               elif A[6]:
                   OBJ.dir = "R"
               elif A[7]:
                   OBJ.dir = "L"
                   
       elif OBJ.dir == "D":
           OBJ.AIColliders[0].st = (OBJ.x+OBJ.speed,OBJ.y+OBJ.speed/2 )
           OBJ.AIColliders[1].st = (OBJ.x-OBJ.speed,OBJ.y+OBJ.speed/2 )
           OBJ.AIColliders[0].end = (OBJ.x+OBJ.speed,OBJ.y+2*OBJ.speed-4 )
           OBJ.AIColliders[1].end = (OBJ.x-OBJ.speed,OBJ.y+2*OBJ.speed-4 )
           
           OBJ.AIColliders[2].st = (OBJ.x+OBJ.speed/2,OBJ.y)
           OBJ.AIColliders[3].st = (OBJ.x-OBJ.speed/2,OBJ.y)
           OBJ.AIColliders[2].end = (OBJ.x+4*OBJ.speed,OBJ.y)
           OBJ.AIColliders[3].end = (OBJ.x-4*OBJ.speed,OBJ.y)

           OBJ.AIColliders[4].st = (OBJ.x+OBJ.speed,OBJ.y+2*OBJ.speed)
           OBJ.AIColliders[5].st = (OBJ.x-OBJ.speed,OBJ.y+2*OBJ.speed)
           OBJ.AIColliders[4].end = (OBJ.x+OBJ.speed,OBJ.y+5*OBJ.speed)
           OBJ.AIColliders[5].end = (OBJ.x-OBJ.speed,OBJ.y+5*OBJ.speed)
           
           OBJ.AIColliders[6].st = (OBJ.x+2*OBJ.speed,OBJ.y)
           OBJ.AIColliders[7].st = (OBJ.x-2*OBJ.speed,OBJ.y)
           OBJ.AIColliders[6].end = (OBJ.x+4*OBJ.speed,OBJ.y)
           OBJ.AIColliders[7].end = (OBJ.x-4*OBJ.speed,OBJ.y)
           
           OBJ.AIColliders[8].st = (OBJ.x-OBJ.speed/2,OBJ.y+OBJ.speed)
           OBJ.AIColliders[8].end = (OBJ.x+OBJ.speed/2, OBJ.y+OBJ.speed)
           
           A=[0,0,0,0,0,0,0,0,0]
           for i in range(len(OBJ.AIColliders)):
               for bike in spGroup:
                   if A[i]:
                       pass
                   for line in bike.Lines:
                       if OBJ.AIColliders[i].collideswith(line):
                           A[i] = True
                           break
           if (A[0] and A[1]) or A[8]:
               #dead ahead line
               if A[2] and A[3]:
                   OBJ.Action()
               elif A[3]:
                   OBJ.dir = "R"
               elif A[2]:
                   OBJ.dir = "L"
               elif A[6] and A[7]:
                   if random.randint(0,3) > 1:
                       OBJ.dir = "L"
                   else:
                       OBJ.dir = "R"
               elif random.randint(0,2) >= 1:
                   OBJ.dir = "R"
               else:
                   OBJ.dir = "L"
           elif A[0]:
               OBJ.dir = "L"
           elif A[1]:
               OBJ.dir = "R"
           elif A[4] or A[5]: #ufar
               if A[2] and A[3]:
                   OBJ.Action()    
               elif A[3]:
                   OBJ.dir = "R"
               elif A[2]:
                   OBJ.dir = "L"
               elif A[6]:
                   OBJ.dir = "L"
               elif A[7]:
                   OBJ.dir = "R"

       elif OBJ.dir == "R":
           OBJ.AIColliders[0].st = (OBJ.x+OBJ.speed/2,OBJ.y-OBJ.speed )
           OBJ.AIColliders[1].st = (OBJ.x+OBJ.speed/2,OBJ.y+OBJ.speed )
           OBJ.AIColliders[0].end = (OBJ.x+2*OBJ.speed+4,OBJ.y-OBJ.speed)
           OBJ.AIColliders[1].end = (OBJ.x+2*OBJ.speed+4,OBJ.y+OBJ.speed )
           
           OBJ.AIColliders[2].st = (OBJ.x,OBJ.y-OBJ.speed/2)
           OBJ.AIColliders[3].st = (OBJ.x,OBJ.y+OBJ.speed/2)
           OBJ.AIColliders[2].end = (OBJ.x,OBJ.y-2*OBJ.speed)
           OBJ.AIColliders[3].end = (OBJ.x,OBJ.y+2*OBJ.speed)

           OBJ.AIColliders[4].st = (OBJ.x+OBJ.speed*2,OBJ.y-OBJ.speed)
           OBJ.AIColliders[5].st = (OBJ.x+OBJ.speed*2,OBJ.y+OBJ.speed)
           OBJ.AIColliders[4].end = (OBJ.x+5*OBJ.speed,OBJ.y-OBJ.speed)
           OBJ.AIColliders[5].end = (OBJ.x+5*OBJ.speed,OBJ.y+OBJ.speed)
           
           OBJ.AIColliders[6].st = (OBJ.x,OBJ.y-2*OBJ.speed)
           OBJ.AIColliders[7].st = (OBJ.x,OBJ.y+2*OBJ.speed)
           OBJ.AIColliders[6].end = (OBJ.x,OBJ.y-4*OBJ.speed)
           OBJ.AIColliders[7].end = (OBJ.x,OBJ.y+4*OBJ.speed)
           
           OBJ.AIColliders[8].st = (OBJ.x+OBJ.speed,OBJ.y-OBJ.speed/2)
           OBJ.AIColliders[8].end = (OBJ.x+OBJ.speed, OBJ.y+OBJ.speed/2)
           
           A=[0,0,0,0,0,0,0,0,0]
           for i in range(len(OBJ.AIColliders)):
               for bike in spGroup:
                   if A[i]:
                       pass
                   for line in bike.Lines:
                       if OBJ.AIColliders[i].collideswith(line):
                           A[i] = True
                           break
           if (A[0] and A[1]) or A[8]:
               #dead ahead line
               if A[2] and A[3]:
                   OBJ.Action()
               elif A[3]:
                   OBJ.dir = "U"
               elif A[2]:
                   OBJ.dir = "D"
               elif A[6] and A[7]:
                   if random.randint(0,3) > 1:
                       OBJ.dir = "D"
                   else:
                       OBJ.dir = "U"
               elif random.randint(0,2) >= 1:
                   OBJ.dir = "U"
               else:
                   OBJ.dir = "D"
           elif A[0]:
               OBJ.dir = "D"
           elif A[1]:
               OBJ.dir = "U"
           elif A[4] or A[5]: #ufar
               if A[2] and A[3]:
                   OBJ.Action()    
               elif A[3]:
                   OBJ.dir = "U"
               elif A[2]:
                   OBJ.dir = "D"
               elif A[6]:
                   OBJ.dir = "D"
               elif A[7]:
                   OBJ.dir = "U"

       elif OBJ.dir == "L":
           OBJ.AIColliders[0].st = (OBJ.x-OBJ.speed/2,OBJ.y+OBJ.speed )
           OBJ.AIColliders[1].st = (OBJ.x-OBJ.speed/2,OBJ.y-OBJ.speed )
           OBJ.AIColliders[0].end = (OBJ.x-2*OBJ.speed-4,OBJ.y+OBJ.speed)
           OBJ.AIColliders[1].end = (OBJ.x-2*OBJ.speed-4,OBJ.y-OBJ.speed )
           
           OBJ.AIColliders[2].st = (OBJ.x,OBJ.y+OBJ.speed/2)
           OBJ.AIColliders[3].st = (OBJ.x,OBJ.y-OBJ.speed/2)
           OBJ.AIColliders[2].end = (OBJ.x,OBJ.y+2*OBJ.speed)
           OBJ.AIColliders[3].end = (OBJ.x,OBJ.y-2*OBJ.speed)

           OBJ.AIColliders[4].st = (OBJ.x-OBJ.speed*2,OBJ.y+OBJ.speed)
           OBJ.AIColliders[5].st = (OBJ.x-OBJ.speed*2,OBJ.y-OBJ.speed)
           OBJ.AIColliders[4].end = (OBJ.x-5*OBJ.speed,OBJ.y+OBJ.speed)
           OBJ.AIColliders[5].end = (OBJ.x-5*OBJ.speed,OBJ.y-OBJ.speed)
           
           OBJ.AIColliders[6].st = (OBJ.x,OBJ.y+2*OBJ.speed)
           OBJ.AIColliders[7].st = (OBJ.x,OBJ.y-2*OBJ.speed)
           OBJ.AIColliders[6].end = (OBJ.x,OBJ.y+4*OBJ.speed)
           OBJ.AIColliders[7].end = (OBJ.x,OBJ.y-4*OBJ.speed)
           
           OBJ.AIColliders[8].st = (OBJ.x-OBJ.speed,OBJ.y+OBJ.speed/2)
           OBJ.AIColliders[8].end = (OBJ.x-OBJ.speed, OBJ.y-OBJ.speed/2)
           
           A=[0,0,0,0,0,0,0,0,0]
           for i in range(len(OBJ.AIColliders)):
               for bike in spGroup:
                   if A[i]:
                       pass
                   for line in bike.Lines:
                       if OBJ.AIColliders[i].collideswith(line):
                           A[i] = True
                           break
           if (A[0] and A[1]) or A[8]:
               #dead ahead line
               if A[2] and A[3]:
                   OBJ.Action()
               elif A[3]:
                   OBJ.dir = "D"
               elif A[2]:
                   OBJ.dir = "U"
               elif A[6] and A[7]:
                   if random.randint(0,3) > 1:
                       OBJ.dir = "U"
                   else:
                       OBJ.dir = "D"
               elif random.randint(0,2) >= 1:
                   OBJ.dir = "D"
               else:
                   OBJ.dir = "U"
           elif A[0]:
               OBJ.dir = "U"
           elif A[1]:
               OBJ.dir = "D"
           elif A[4] or A[5]: #ufar
               if A[2] and A[3]:
                   OBJ.Action()    
               elif A[3]:
                   OBJ.dir = "D"
               elif A[2]:
                   OBJ.dir = "U"
               elif A[6]:
                   OBJ.dir = "U"
               elif A[7]:
                   OBJ.dir = "D"
       OBJ.dirChanged = True
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#
#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#for lightbikes
def AI_LIGHT(OBJ, style = "passive", num = 0, spGroup = None):
   '''style can be passive, aggro, or evasive '''
   OBJ.AIColliders = []
   OBJ.AIColliders.append(CSegment.Segment((0,0),(0,0)))
   OBJ.AIColliders.append(CSegment.Segment((0,0),(0,0)))
   OBJ.AIColliders.append(CSegment.Segment((0,0),(0,0)))
   OBJ.AIColliders.append(CSegment.Segment((0,0),(0,0)))
   OBJ.AIColliders.append(CSegment.Segment((0,0),(0,0)))
   OBJ.AIColliders.append(CSegment.Segment((0,0),(0,0)))
   OBJ.AIColliders.append(CSegment.Segment((0,0),(0,0)))
   OBJ.AIColliders.append(CSegment.Segment((0,0),(0,0)))
   OBJ.AIColliders.append(CSegment.Segment((0,0),(0,0)))
   
   #self.style is the style of the AI, which can be passive, evasive, or agressive.
   if style == "evasive":
       OBJ.AIColliders.append(CSegment.Segment((0,0),(0,0)))
       OBJ.AIColliders.append(CSegment.Segment((0,0),(0,0)))
       if num >5:
           OBJ.dirChanged = True
           return
       if OBJ.dir == "U":
           OBJ.AIColliders[0].st = (OBJ.x-OBJ.speed,OBJ.y-OBJ.speed/2 )
           OBJ.AIColliders[1].st = (OBJ.x+OBJ.speed,OBJ.y-OBJ.speed/2 )
           OBJ.AIColliders[0].end = (OBJ.x-OBJ.speed,OBJ.y-2*OBJ.speed-4 )
           OBJ.AIColliders[1].end = (OBJ.x+OBJ.speed,OBJ.y-2*OBJ.speed-4 )
           
           OBJ.AIColliders[2].st = (OBJ.x-OBJ.speed/2,OBJ.y)
           OBJ.AIColliders[3].st = (OBJ.x+OBJ.speed/2,OBJ.y)
           OBJ.AIColliders[2].end = (OBJ.x-2*OBJ.speed,OBJ.y)
           OBJ.AIColliders[3].end = (OBJ.x+2*OBJ.speed,OBJ.y)

           OBJ.AIColliders[4].st = (OBJ.x-OBJ.speed,OBJ.y-2*OBJ.speed)
           OBJ.AIColliders[5].st = (OBJ.x+OBJ.speed,OBJ.y-2*OBJ.speed)
           OBJ.AIColliders[4].end = (OBJ.x-OBJ.speed,OBJ.y-5*OBJ.speed)
           OBJ.AIColliders[5].end = (OBJ.x+OBJ.speed,OBJ.y-5*OBJ.speed)
           
           OBJ.AIColliders[6].st = (OBJ.x-2*OBJ.speed,OBJ.y)
           OBJ.AIColliders[7].st = (OBJ.x+2*OBJ.speed,OBJ.y)
           OBJ.AIColliders[6].end = (OBJ.x-4*OBJ.speed,OBJ.y)
           OBJ.AIColliders[7].end = (OBJ.x+4*OBJ.speed,OBJ.y)
           
           OBJ.AIColliders[8].st = (OBJ.x-OBJ.speed/2,OBJ.y-OBJ.speed)
           OBJ.AIColliders[8].end = (OBJ.x+OBJ.speed/2, OBJ.y-OBJ.speed)
           
           OBJ.AIColliders[9].st = (OBJ.x-3*OBJ.speed, OBJ.y)
           OBJ.AIColliders[10].st = (OBJ.x+3*OBJ.speed, OBJ.y)
           OBJ.AIColliders[9].end = (OBJ.x-OBJ.speed, OBJ.y-5*OBJ.speed)
           OBJ.AIColliders[10].end = (OBJ.x+OBJ.speed, OBJ.y-5*OBJ.speed)
           
           A=[0,0,0,0,0,0,0,0,0,0,0]
           for i in range(len(OBJ.AIColliders)):
               for bike in spGroup:
                   if A[i]:
                       pass
                   for line in bike.Lines:
                       if OBJ.AIColliders[i].collideswith(line):
                           A[i] = True
                           break
           if (A[0] and A[1]) or A[8]:
               #dead ahead line
               if A[2] and A[3]:
                   OBJ.Action()
               elif A[3]:
                   OBJ.dir = "L"
               elif A[2]:
                   OBJ.dir = "R"
               elif A[6] and A[7]:
                   if random.randint(0,3) > 1:
                       OBJ.dir = "R"
                   else:
                       OBJ.dir = "L"
               elif random.randint(0,2) >= 1:
                   OBJ.dir = "L"
               else:
                   OBJ.dir = "R"
           elif A[0]:
               OBJ.dir = "R"
           elif A[1]:
               OBJ.dir = "L"
           elif A[4] or A[5]: #ufar
               if A[2] and A[3]:
                   OBJ.Action()    
               elif A[3]:
                   OBJ.dir = "L"
               elif A[2]:
                   OBJ.dir = "R"
               elif A[6]:
                   OBJ.dir = "R"
               elif A[7]:
                   OBJ.dir = "L"
           elif A[9] and not (A[3]or A[7] or A[10]) and random.randint(0,5)>4:
               OBJ.dir = "R"
           elif A[10] and not (A[2]or A[6] or A[9]) and random.randint(0,5)>4:
               OBJ.dir = "L"
               
       elif OBJ.dir == "D":
           OBJ.AIColliders[0].st = (OBJ.x+OBJ.speed,OBJ.y+OBJ.speed/2 )
           OBJ.AIColliders[1].st = (OBJ.x-OBJ.speed,OBJ.y+OBJ.speed/2 )
           OBJ.AIColliders[0].end = (OBJ.x+OBJ.speed,OBJ.y+2*OBJ.speed-4 )
           OBJ.AIColliders[1].end = (OBJ.x-OBJ.speed,OBJ.y+2*OBJ.speed-4 )
           
           OBJ.AIColliders[2].st = (OBJ.x+OBJ.speed/2,OBJ.y)
           OBJ.AIColliders[3].st = (OBJ.x-OBJ.speed/2,OBJ.y)
           OBJ.AIColliders[2].end = (OBJ.x+4*OBJ.speed,OBJ.y)
           OBJ.AIColliders[3].end = (OBJ.x-4*OBJ.speed,OBJ.y)

           OBJ.AIColliders[4].st = (OBJ.x+OBJ.speed,OBJ.y+2*OBJ.speed)
           OBJ.AIColliders[5].st = (OBJ.x-OBJ.speed,OBJ.y+2*OBJ.speed)
           OBJ.AIColliders[4].end = (OBJ.x+OBJ.speed,OBJ.y+5*OBJ.speed)
           OBJ.AIColliders[5].end = (OBJ.x-OBJ.speed,OBJ.y+5*OBJ.speed)
           
           OBJ.AIColliders[6].st = (OBJ.x+2*OBJ.speed,OBJ.y)
           OBJ.AIColliders[7].st = (OBJ.x-2*OBJ.speed,OBJ.y)
           OBJ.AIColliders[6].end = (OBJ.x+4*OBJ.speed,OBJ.y)
           OBJ.AIColliders[7].end = (OBJ.x-4*OBJ.speed,OBJ.y)
           
           OBJ.AIColliders[8].st = (OBJ.x-OBJ.speed/2,OBJ.y+OBJ.speed)
           OBJ.AIColliders[8].end = (OBJ.x+OBJ.speed/2, OBJ.y+OBJ.speed)
           
           OBJ.AIColliders[9].st = (OBJ.x+3*OBJ.speed, OBJ.y)
           OBJ.AIColliders[10].st = (OBJ.x-3*OBJ.speed, OBJ.y)
           OBJ.AIColliders[9].end = (OBJ.x+OBJ.speed, OBJ.y+5*OBJ.speed)
           OBJ.AIColliders[10].end = (OBJ.x-OBJ.speed, OBJ.y+5*OBJ.speed)
           
           A=[0,0,0,0,0,0,0,0,0,0,0]
           for i in range(len(OBJ.AIColliders)):
               for bike in spGroup:
                   if A[i]:
                       pass
                   for line in bike.Lines:
                       if OBJ.AIColliders[i].collideswith(line):
                           A[i] = True
                           break
           if (A[0] and A[1]) or A[8]:
               #dead ahead line
               if A[2] and A[3]:
                   OBJ.Action()
               elif A[3]:
                   OBJ.dir = "R"
               elif A[2]:
                   OBJ.dir = "L"
               elif A[6] and A[7]:
                   if random.randint(0,3) > 1:
                       OBJ.dir = "L"
                   else:
                       OBJ.dir = "R"
               elif random.randint(0,2) >= 1:
                   OBJ.dir = "R"
               else:
                   OBJ.dir = "L"
           elif A[0]:
               OBJ.dir = "L"
           elif A[1]:
               OBJ.dir = "R"
           elif A[4] or A[5]: #ufar
               if A[2] and A[3]:
                   OBJ.Action()    
               elif A[3]:
                   OBJ.dir = "R"
               elif A[2]:
                   OBJ.dir = "L"
               elif A[6]:
                   OBJ.dir = "L"
               elif A[7]:
                   OBJ.dir = "R"
           elif A[9] and not (A[3]or A[7] or A[10]) and random.randint(0,5)>4:
               OBJ.dir = "L"
           elif A[10] and not (A[2]or A[6] or A[9]) and random.randint(0,5)>4:
               OBJ.dir = "R"

       elif OBJ.dir == "R":
           OBJ.AIColliders[0].st = (OBJ.x+OBJ.speed/2,OBJ.y-OBJ.speed )
           OBJ.AIColliders[1].st = (OBJ.x+OBJ.speed/2,OBJ.y+OBJ.speed )
           OBJ.AIColliders[0].end = (OBJ.x+2*OBJ.speed+4,OBJ.y-OBJ.speed)
           OBJ.AIColliders[1].end = (OBJ.x+2*OBJ.speed+4,OBJ.y+OBJ.speed )
           
           OBJ.AIColliders[2].st = (OBJ.x,OBJ.y-OBJ.speed/2)
           OBJ.AIColliders[3].st = (OBJ.x,OBJ.y+OBJ.speed/2)
           OBJ.AIColliders[2].end = (OBJ.x,OBJ.y-2*OBJ.speed)
           OBJ.AIColliders[3].end = (OBJ.x,OBJ.y+2*OBJ.speed)

           OBJ.AIColliders[4].st = (OBJ.x+OBJ.speed*2,OBJ.y-OBJ.speed)
           OBJ.AIColliders[5].st = (OBJ.x+OBJ.speed*2,OBJ.y+OBJ.speed)
           OBJ.AIColliders[4].end = (OBJ.x+5*OBJ.speed,OBJ.y-OBJ.speed)
           OBJ.AIColliders[5].end = (OBJ.x+5*OBJ.speed,OBJ.y+OBJ.speed)
           
           OBJ.AIColliders[6].st = (OBJ.x,OBJ.y-2*OBJ.speed)
           OBJ.AIColliders[7].st = (OBJ.x,OBJ.y+2*OBJ.speed)
           OBJ.AIColliders[6].end = (OBJ.x,OBJ.y-4*OBJ.speed)
           OBJ.AIColliders[7].end = (OBJ.x,OBJ.y+4*OBJ.speed)
           
           OBJ.AIColliders[8].st = (OBJ.x+OBJ.speed,OBJ.y-OBJ.speed/2)
           OBJ.AIColliders[8].end = (OBJ.x+OBJ.speed, OBJ.y+OBJ.speed/2)
           
           OBJ.AIColliders[9].st = (OBJ.x, OBJ.y-3*OBJ.speed)
           OBJ.AIColliders[10].st = (OBJ.x, OBJ.y+3*OBJ.speed)
           OBJ.AIColliders[9].end = (OBJ.x+5*OBJ.speed, OBJ.y-OBJ.speed)
           OBJ.AIColliders[10].end = (OBJ.x+5*OBJ.speed, OBJ.y+OBJ.speed)
           
           A=[0,0,0,0,0,0,0,0,0,0,0]
           for i in range(len(OBJ.AIColliders)):
               for bike in spGroup:
                   if A[i]:
                       pass
                   for line in bike.Lines:
                       if OBJ.AIColliders[i].collideswith(line):
                           A[i] = True
                           break
           if (A[0] and A[1]) or A[8]:
               #dead ahead line
               if A[2] and A[3]:
                   OBJ.Action()
               elif A[3]:
                   OBJ.dir = "U"
               elif A[2]:
                   OBJ.dir = "D"
               elif A[6] and A[7]:
                   if random.randint(0,3) > 1:
                       OBJ.dir = "D"
                   else:
                       OBJ.dir = "U"
               elif random.randint(0,2) >= 1:
                   OBJ.dir = "U"
               else:
                   OBJ.dir = "D"
           elif A[0]:
               OBJ.dir = "D"
           elif A[1]:
               OBJ.dir = "U"
           elif A[4] or A[5]: #ufar
               if A[2] and A[3]:
                   OBJ.Action()    
               elif A[3]:
                   OBJ.dir = "U"
               elif A[2]:
                   OBJ.dir = "D"
               elif A[6]:
                   OBJ.dir = "D"
               elif A[7]:
                   OBJ.dir = "U"
           elif A[9] and not (A[3]or A[7] or A[10]) and random.randint(0,5)>4:
               OBJ.dir = "D"
           elif A[10] and not (A[2]or A[6] or A[9]) and random.randint(0,5)>4:
               OBJ.dir = "U"

       elif OBJ.dir == "L":
           OBJ.AIColliders[0].st = (OBJ.x-OBJ.speed/2,OBJ.y+OBJ.speed )
           OBJ.AIColliders[1].st = (OBJ.x-OBJ.speed/2,OBJ.y-OBJ.speed )
           OBJ.AIColliders[0].end = (OBJ.x-2*OBJ.speed-4,OBJ.y+OBJ.speed)
           OBJ.AIColliders[1].end = (OBJ.x-2*OBJ.speed-4,OBJ.y-OBJ.speed )
           
           OBJ.AIColliders[2].st = (OBJ.x,OBJ.y+OBJ.speed/2)
           OBJ.AIColliders[3].st = (OBJ.x,OBJ.y-OBJ.speed/2)
           OBJ.AIColliders[2].end = (OBJ.x,OBJ.y+2*OBJ.speed)
           OBJ.AIColliders[3].end = (OBJ.x,OBJ.y-2*OBJ.speed)

           OBJ.AIColliders[4].st = (OBJ.x-OBJ.speed*2,OBJ.y+OBJ.speed)
           OBJ.AIColliders[5].st = (OBJ.x-OBJ.speed*2,OBJ.y-OBJ.speed)
           OBJ.AIColliders[4].end = (OBJ.x-5*OBJ.speed,OBJ.y+OBJ.speed)
           OBJ.AIColliders[5].end = (OBJ.x-5*OBJ.speed,OBJ.y-OBJ.speed)
           
           OBJ.AIColliders[6].st = (OBJ.x,OBJ.y+2*OBJ.speed)
           OBJ.AIColliders[7].st = (OBJ.x,OBJ.y-2*OBJ.speed)
           OBJ.AIColliders[6].end = (OBJ.x,OBJ.y+4*OBJ.speed)
           OBJ.AIColliders[7].end = (OBJ.x,OBJ.y-4*OBJ.speed)
           
           OBJ.AIColliders[8].st = (OBJ.x-OBJ.speed,OBJ.y+OBJ.speed/2)
           OBJ.AIColliders[8].end = (OBJ.x-OBJ.speed, OBJ.y-OBJ.speed/2)
           
           OBJ.AIColliders[9].st = (OBJ.x, OBJ.y+3*OBJ.speed)
           OBJ.AIColliders[10].st = (OBJ.x, OBJ.y-3*OBJ.speed)
           OBJ.AIColliders[9].end = (OBJ.x-5*OBJ.speed, OBJ.y+OBJ.speed)
           OBJ.AIColliders[10].end = (OBJ.x-5*OBJ.speed, OBJ.y-OBJ.speed)
           
           A=[0,0,0,0,0,0,0,0,0,0,0]
           for i in range(len(OBJ.AIColliders)):
               for bike in spGroup:
                   if A[i]:
                       pass
                   for line in bike.Lines:
                       if OBJ.AIColliders[i].collideswith(line):
                           A[i] = True
                           break
           if (A[0] and A[1]) or A[8]:
               #dead ahead line
               if A[2] and A[3]:
                   OBJ.Action()
               elif A[3]:
                   OBJ.dir = "D"
               elif A[2]:
                   OBJ.dir = "U"
               elif A[6] and A[7]:
                   if random.randint(0,3) > 1:
                       OBJ.dir = "U"
                   else:
                       OBJ.dir = "D"
               elif random.randint(0,2) >= 1:
                   OBJ.dir = "D"
               else:
                   OBJ.dir = "U"
           elif A[0]:
               OBJ.dir = "U"
           elif A[1]:
               OBJ.dir = "D"
           elif A[4] or A[5]: #ufar
               if A[2] and A[3]:
                   OBJ.Action()    
               elif A[3]:
                   OBJ.dir = "D"
               elif A[2]:
                   OBJ.dir = "U"
               elif A[6]:
                   OBJ.dir = "U"
               elif A[7]:
                   OBJ.dir = "D"
           elif A[9] and not (A[3]or A[7] or A[10]) and random.randint(0,5)>4:
               OBJ.dir = "U"
           elif A[10] and not (A[2]or A[6] or A[9]) and random.randint(0,5)>4:
               OBJ.dir = "D"
       OBJ.dirChanged = True
       
   elif style == "aggro":
       if num > 5:
           OBJ.dirChanged = True
           return
       OBJ.AIColliders.append(CSegment.Segment((0,0),(0,0)))
       OBJ.AIColliders.append(CSegment.Segment((0,0),(0,0)))
       if OBJ.dir == "U":
           OBJ.AIColliders[0].st = (OBJ.x-OBJ.speed/2,OBJ.y-OBJ.speed/2 )
           OBJ.AIColliders[1].st = (OBJ.x+OBJ.speed/2,OBJ.y-OBJ.speed/2 )
           OBJ.AIColliders[0].end = (OBJ.x-OBJ.speed,OBJ.y-2*OBJ.speed-4 )
           OBJ.AIColliders[1].end = (OBJ.x+OBJ.speed,OBJ.y-2*OBJ.speed-4 )
           
           OBJ.AIColliders[2].st = (OBJ.x-OBJ.speed/2,OBJ.y)
           OBJ.AIColliders[3].st = (OBJ.x+OBJ.speed/2,OBJ.y)
           OBJ.AIColliders[2].end = (OBJ.x-2*OBJ.speed,OBJ.y)
           OBJ.AIColliders[3].end = (OBJ.x+2*OBJ.speed,OBJ.y)

           OBJ.AIColliders[4].st = (OBJ.x-OBJ.speed-1,OBJ.y-2*OBJ.speed)
           OBJ.AIColliders[5].st = (OBJ.x+OBJ.speed+1,OBJ.y-2*OBJ.speed)
           OBJ.AIColliders[4].end = (OBJ.x,OBJ.y-5*OBJ.speed)
           OBJ.AIColliders[5].end = (OBJ.x,OBJ.y-5*OBJ.speed)
           
           OBJ.AIColliders[6].st = (OBJ.x-2*OBJ.speed,OBJ.y)
           OBJ.AIColliders[7].st = (OBJ.x+2*OBJ.speed,OBJ.y)
           OBJ.AIColliders[6].end = (OBJ.x-3.5*OBJ.speed,OBJ.y)
           OBJ.AIColliders[7].end = (OBJ.x+3.5*OBJ.speed,OBJ.y)
           
           OBJ.AIColliders[8].st = (OBJ.x-OBJ.speed/2,OBJ.y-OBJ.speed)
           OBJ.AIColliders[8].end = (OBJ.x+OBJ.speed/2, OBJ.y-OBJ.speed)
           
           OBJ.AIColliders[9].st = (OBJ.x-OBJ.speed/2,OBJ.y+OBJ.speed)
           OBJ.AIColliders[10].st = (OBJ.x+OBJ.speed/2, OBJ.y+OBJ.speed)
           OBJ.AIColliders[9].end = (OBJ.x-OBJ.speed,OBJ.y+OBJ.speed*2)
           OBJ.AIColliders[10].end = (OBJ.x+OBJ.speed, OBJ.y+OBJ.speed*2)
           A=[0,0,0,0,0,0,0,0,0,0,0]
           for i in range(len(OBJ.AIColliders)):
               for bike in spGroup:
                   if A[i]:
                       pass
                   for line in bike.Lines:
                       if OBJ.AIColliders[i].collideswith(line):
                           if i != 9 and i != 10:
                               A[i] = True
                           elif bike != OBJ:
                               A[i] = True
                           break
           if (A[0] and A[1]) or A[8]:
               #dead ahead line
               if A[2] and A[3]:
                   OBJ.Action()
               elif A[3]:
                   OBJ.dir = "L"
               elif A[2]:
                   OBJ.dir = "R"
               elif A[6] and A[7]:
                   if random.randint(0,3) > 1:
                       OBJ.dir = "R"
                   else:
                       OBJ.dir = "L"
               elif random.randint(0,2) >= 1:
                   OBJ.dir = "L"
               else:
                   OBJ.dir = "R"
           elif A[0]:
               OBJ.dir = "R"
           elif A[1]:
               OBJ.dir = "L"
           elif A[4] or A[5]: #ufar
               if A[2] and A[3]:
                   OBJ.Action()    
               elif A[3]:
                   OBJ.dir = "L"
               elif A[2]:
                   OBJ.dir = "R"
               elif A[6]:
                   OBJ.dir = "R"
               elif A[7]:
                   OBJ.dir = "L"
           elif A[9] and not (A[0] or A[2] or A[6] or A[10]):
               OBJ.dir= "L"
           elif A[10] and not (A[1] or A[3] or A[7] or A[9]):
               OBJ.dir = "R"
           elif A[6] and not A[3] and random.randint(0,35) > 28:
               OBJ.dir = "R"
           elif A[7] and not A[2] and random.randint(0,35) > 28:
               OBJ.dir = "L"
       elif OBJ.dir == "D":
           OBJ.AIColliders[0].st = (OBJ.x+OBJ.speed/2,OBJ.y+OBJ.speed/2 )
           OBJ.AIColliders[1].st = (OBJ.x-OBJ.speed/2,OBJ.y+OBJ.speed/2 )
           OBJ.AIColliders[0].end = (OBJ.x+OBJ.speed,OBJ.y+2*OBJ.speed-4 )
           OBJ.AIColliders[1].end = (OBJ.x-OBJ.speed,OBJ.y+2*OBJ.speed-4 )
           
           OBJ.AIColliders[2].st = (OBJ.x+OBJ.speed/2,OBJ.y)
           OBJ.AIColliders[3].st = (OBJ.x-OBJ.speed/2,OBJ.y)
           OBJ.AIColliders[2].end = (OBJ.x+4*OBJ.speed,OBJ.y)
           OBJ.AIColliders[3].end = (OBJ.x-4*OBJ.speed,OBJ.y)

           OBJ.AIColliders[4].st = (OBJ.x+OBJ.speed+1,OBJ.y+2*OBJ.speed)
           OBJ.AIColliders[5].st = (OBJ.x-OBJ.speed-1,OBJ.y+2*OBJ.speed)
           OBJ.AIColliders[4].end = (OBJ.x,OBJ.y+5*OBJ.speed)
           OBJ.AIColliders[5].end = (OBJ.x, OBJ.y+5*OBJ.speed)
           
           OBJ.AIColliders[6].st = (OBJ.x+2*OBJ.speed,OBJ.y)
           OBJ.AIColliders[7].st = (OBJ.x-2*OBJ.speed,OBJ.y)
           OBJ.AIColliders[6].end = (OBJ.x+3.5*OBJ.speed,OBJ.y)
           OBJ.AIColliders[7].end = (OBJ.x-3.5*OBJ.speed,OBJ.y)
           
           OBJ.AIColliders[8].st = (OBJ.x-OBJ.speed/2,OBJ.y+OBJ.speed)
           OBJ.AIColliders[8].end = (OBJ.x+OBJ.speed/2, OBJ.y+OBJ.speed)
           
           OBJ.AIColliders[9].st = (OBJ.x+OBJ.speed/2,OBJ.y-OBJ.speed)
           OBJ.AIColliders[10].st = (OBJ.x-OBJ.speed/2, OBJ.y-OBJ.speed)
           OBJ.AIColliders[9].end = (OBJ.x+OBJ.speed,OBJ.y-OBJ.speed*2)
           OBJ.AIColliders[10].end = (OBJ.x-OBJ.speed, OBJ.y-OBJ.speed*2)
           A=[0,0,0,0,0,0,0,0,0,0,0]
           for i in range(len(OBJ.AIColliders)):
               for bike in spGroup:
                   if A[i]:
                       pass
                   for line in bike.Lines:
                       if OBJ.AIColliders[i].collideswith(line):
                           if i != 9 and i != 10:
                               A[i] = True
                           elif bike != OBJ:
                               A[i] = True
                           break
           if (A[0] and A[1]) or A[8]:
               #dead ahead line
               if A[2] and A[3]:
                   OBJ.Action()
               elif A[3]:
                   OBJ.dir = "R"
               elif A[2]:
                   OBJ.dir = "L"
               elif A[6] and A[7]:
                   if random.randint(0,3) > 1:
                       OBJ.dir = "L"
                   else:
                       OBJ.dir = "R"
               elif random.randint(0,2) >= 1:
                   OBJ.dir = "R"
               else:
                   OBJ.dir = "L"
           elif A[0]:
               OBJ.dir = "L"
           elif A[1]:
               OBJ.dir = "R"
           elif A[4] or A[5]: #ufar
               if A[2] and A[3]:
                   OBJ.Action()    
               elif A[3]:
                   OBJ.dir = "R"
               elif A[2]:
                   OBJ.dir = "L"
               elif A[6]:
                   OBJ.dir = "L"
               elif A[7]:
                   OBJ.dir = "R"
           elif A[9] and not (A[0] or A[2] or A[6] or A[10]):
               OBJ.dir= "R"
           elif A[10] and not (A[1] or A[3] or A[7] or A[9]):
               OBJ.dir = "L"
           elif A[6] and not A[3] and random.randint(0,35) > 28:
               OBJ.dir = "L"
           elif A[7] and not A[2] and random.randint(0,35) > 28:
               OBJ.dir = "R"

       elif OBJ.dir == "R":
           OBJ.AIColliders[0].st = (OBJ.x+OBJ.speed/2,OBJ.y-OBJ.speed/2 )
           OBJ.AIColliders[1].st = (OBJ.x+OBJ.speed/2,OBJ.y+OBJ.speed/2 )
           OBJ.AIColliders[0].end = (OBJ.x+2*OBJ.speed+4,OBJ.y-OBJ.speed)
           OBJ.AIColliders[1].end = (OBJ.x+2*OBJ.speed+4,OBJ.y+OBJ.speed )
           
           OBJ.AIColliders[2].st = (OBJ.x,OBJ.y-OBJ.speed/2)
           OBJ.AIColliders[3].st = (OBJ.x,OBJ.y+OBJ.speed/2)
           OBJ.AIColliders[2].end = (OBJ.x,OBJ.y-2*OBJ.speed)
           OBJ.AIColliders[3].end = (OBJ.x,OBJ.y+2*OBJ.speed)

           OBJ.AIColliders[4].st = (OBJ.x+OBJ.speed*2,OBJ.y-OBJ.speed-1)
           OBJ.AIColliders[5].st = (OBJ.x+OBJ.speed*2,OBJ.y+OBJ.speed+1)
           OBJ.AIColliders[4].end = (OBJ.x+5*OBJ.speed,OBJ.y)
           OBJ.AIColliders[5].end = (OBJ.x+5*OBJ.speed,OBJ.y)
           
           OBJ.AIColliders[6].st = (OBJ.x,OBJ.y-2*OBJ.speed)
           OBJ.AIColliders[7].st = (OBJ.x,OBJ.y+2*OBJ.speed)
           OBJ.AIColliders[6].end = (OBJ.x,OBJ.y-3.5*OBJ.speed)
           OBJ.AIColliders[7].end = (OBJ.x,OBJ.y+3.5*OBJ.speed)
           
           OBJ.AIColliders[8].st = (OBJ.x+OBJ.speed,OBJ.y-OBJ.speed/2)
           OBJ.AIColliders[8].end = (OBJ.x+OBJ.speed, OBJ.y+OBJ.speed/2)
           
           OBJ.AIColliders[9].st = (OBJ.x-OBJ.speed,OBJ.y-OBJ.speed/2)
           OBJ.AIColliders[10].st = (OBJ.x-OBJ.speed, OBJ.y+OBJ.speed/2)
           OBJ.AIColliders[9].end = (OBJ.x-OBJ.speed*2,OBJ.y-OBJ.speed)
           OBJ.AIColliders[10].end = (OBJ.x-OBJ.speed*2, OBJ.y+OBJ.speed)
           
           A=[0,0,0,0,0,0,0,0,0,0,0]
           for i in range(len(OBJ.AIColliders)):
               for bike in spGroup:
                   if A[i]:
                       pass
                   for line in bike.Lines:
                       if OBJ.AIColliders[i].collideswith(line):
                           if i != 9 and i != 10:
                               A[i] = True
                           elif bike != OBJ:
                               A[i] = True
                           break
           if (A[0] and A[1]) or A[8]:
               #dead ahead line
               if A[2] and A[3]:
                   OBJ.Action()
               elif A[3]:
                   OBJ.dir = "U"
               elif A[2]:
                   OBJ.dir = "D"
               elif A[6] and A[7]:
                   if random.randint(0,3) > 1:
                       OBJ.dir = "D"
                   else:
                       OBJ.dir = "U"
               elif random.randint(0,2) >= 1:
                   OBJ.dir = "U"
               else:
                   OBJ.dir = "D"
           elif A[0]:
               OBJ.dir = "D"
           elif A[1]:
               OBJ.dir = "U"
           elif A[4] or A[5]: #ufar
               if A[2] and A[3]:
                   OBJ.Action()    
               elif A[3]:
                   OBJ.dir = "U"
               elif A[2]:
                   OBJ.dir = "D"
               elif A[6]:
                   OBJ.dir = "D"
               elif A[7]:
                   OBJ.dir = "U"
           elif A[9] and not (A[0] or A[2] or A[6] or A[10]):
               OBJ.dir= "U"
           elif A[10] and not (A[1] or A[3] or A[7] or A[9]):
               OBJ.dir = "D"
           elif A[6] and not A[3] and random.randint(0,35) > 28:
               OBJ.dir = "D"
           elif A[7] and not A[2] and random.randint(0,35) > 28:
               OBJ.dir = "U"

       elif OBJ.dir == "L":
           OBJ.AIColliders[0].st = (OBJ.x-OBJ.speed/2,OBJ.y+OBJ.speed/2 )
           OBJ.AIColliders[1].st = (OBJ.x-OBJ.speed/2,OBJ.y-OBJ.speed/2 )
           OBJ.AIColliders[0].end = (OBJ.x-2*OBJ.speed-4,OBJ.y+OBJ.speed)
           OBJ.AIColliders[1].end = (OBJ.x-2*OBJ.speed-4,OBJ.y-OBJ.speed )
           
           OBJ.AIColliders[2].st = (OBJ.x,OBJ.y+OBJ.speed/2)
           OBJ.AIColliders[3].st = (OBJ.x,OBJ.y-OBJ.speed/2)
           OBJ.AIColliders[2].end = (OBJ.x,OBJ.y+2*OBJ.speed)
           OBJ.AIColliders[3].end = (OBJ.x,OBJ.y-2*OBJ.speed)

           OBJ.AIColliders[4].st = (OBJ.x-OBJ.speed*2,OBJ.y+OBJ.speed+1)
           OBJ.AIColliders[5].st = (OBJ.x-OBJ.speed*2,OBJ.y-OBJ.speed-1)
           OBJ.AIColliders[4].end = (OBJ.x-5*OBJ.speed,OBJ.y)
           OBJ.AIColliders[5].end = (OBJ.x-5*OBJ.speed,OBJ.y)
           
           OBJ.AIColliders[6].st = (OBJ.x,OBJ.y+2*OBJ.speed)
           OBJ.AIColliders[7].st = (OBJ.x,OBJ.y-2*OBJ.speed)
           OBJ.AIColliders[6].end = (OBJ.x,OBJ.y+3.5*OBJ.speed)
           OBJ.AIColliders[7].end = (OBJ.x,OBJ.y-3.5*OBJ.speed)
           
           OBJ.AIColliders[8].st = (OBJ.x-OBJ.speed,OBJ.y+OBJ.speed/2)
           OBJ.AIColliders[8].end = (OBJ.x-OBJ.speed, OBJ.y-OBJ.speed/2)
           
           OBJ.AIColliders[9].st = (OBJ.x+OBJ.speed,OBJ.y+OBJ.speed/2)
           OBJ.AIColliders[10].st = (OBJ.x+OBJ.speed, OBJ.y-OBJ.speed/2)
           OBJ.AIColliders[9].end = (OBJ.x+OBJ.speed*2,OBJ.y+OBJ.speed)
           OBJ.AIColliders[10].end = (OBJ.x+OBJ.speed*2, OBJ.y-OBJ.speed)
           
           
           A=[0,0,0,0,0,0,0,0,0,0,0]
           for i in range(len(OBJ.AIColliders)):
               for bike in spGroup:
                   if A[i]:
                       pass
                   for line in bike.Lines:
                       if OBJ.AIColliders[i].collideswith(line):
                           if i != 9 and i != 10:
                               A[i] = True
                           elif bike != OBJ:
                               A[i] = True
                           break
           if (A[0] and A[1]) or A[8]:
               #dead ahead line
               if A[2] and A[3]:
                   OBJ.Action()
               elif A[3]:
                   OBJ.dir = "D"
               elif A[2]:
                   OBJ.dir = "U"
               elif A[6] and A[7]:
                   if random.randint(0,3) > 1:
                       OBJ.dir = "U"
                   else:
                       OBJ.dir = "D"
               elif random.randint(0,2) >= 1:
                   OBJ.dir = "D"
               else:
                   OBJ.dir = "U"
           elif A[0]:
               OBJ.dir = "U"
           elif A[1]:
               OBJ.dir = "D"
           elif A[4] or A[5]: #ufar
               if A[2] and A[3]:
                   OBJ.Action()    
               elif A[3]:
                   OBJ.dir = "D"
               elif A[2]:
                   OBJ.dir = "U"
               elif A[6]:
                   OBJ.dir = "U"
               elif A[7]:
                   OBJ.dir = "D"
           elif A[9] and not (A[0] or A[2] or A[6] or A[10]):
               OBJ.dir= "D"
           elif A[10] and not (A[1] or A[3] or A[7] or A[9]):
               OBJ.dir = "U"
           elif A[6] and not A[3] and random.randint(0,35) > 28:
               OBJ.dir = "U"
           elif A[7] and not A[2] and random.randint(0,35) > 28:
               OBJ.dir = "D"
       OBJ.dirChanged = True
   # now if it's passive
   else:
       if num > 5:
           OBJ.dirChanged = True
           return
       if OBJ.dir == "U":
           OBJ.AIColliders[0].st = (OBJ.x-OBJ.speed,OBJ.y-OBJ.speed/2 )
           OBJ.AIColliders[1].st = (OBJ.x+OBJ.speed,OBJ.y-OBJ.speed/2 )
           OBJ.AIColliders[0].end = (OBJ.x-OBJ.speed,OBJ.y-2*OBJ.speed-4 )
           OBJ.AIColliders[1].end = (OBJ.x+OBJ.speed,OBJ.y-2*OBJ.speed-4 )
           
           OBJ.AIColliders[2].st = (OBJ.x-OBJ.speed/2,OBJ.y)
           OBJ.AIColliders[3].st = (OBJ.x+OBJ.speed/2,OBJ.y)
           OBJ.AIColliders[2].end = (OBJ.x-2*OBJ.speed,OBJ.y)
           OBJ.AIColliders[3].end = (OBJ.x+2*OBJ.speed,OBJ.y)

           OBJ.AIColliders[4].st = (OBJ.x-OBJ.speed,OBJ.y-2*OBJ.speed)
           OBJ.AIColliders[5].st = (OBJ.x+OBJ.speed,OBJ.y-2*OBJ.speed)
           OBJ.AIColliders[4].end = (OBJ.x-OBJ.speed,OBJ.y-5*OBJ.speed)
           OBJ.AIColliders[5].end = (OBJ.x+OBJ.speed,OBJ.y-5*OBJ.speed)
           
           OBJ.AIColliders[6].st = (OBJ.x-2*OBJ.speed,OBJ.y)
           OBJ.AIColliders[7].st = (OBJ.x+2*OBJ.speed,OBJ.y)
           OBJ.AIColliders[6].end = (OBJ.x-4*OBJ.speed,OBJ.y)
           OBJ.AIColliders[7].end = (OBJ.x+4*OBJ.speed,OBJ.y)
           
           OBJ.AIColliders[8].st = (OBJ.x-OBJ.speed/2,OBJ.y-OBJ.speed)
           OBJ.AIColliders[8].end = (OBJ.x+OBJ.speed/2, OBJ.y-OBJ.speed)
           A=[0,0,0,0,0,0,0,0,0]
           for i in range(len(OBJ.AIColliders)):
               for bike in spGroup:
                   if A[i]:
                       pass
                   for line in bike.Lines:
                       if OBJ.AIColliders[i].collideswith(line):
                           A[i] = True
                           break
           if (A[0] and A[1]) or A[8]:
               #dead ahead line
               if A[2] and A[3]:
                   OBJ.Action()
               elif A[3]:
                   OBJ.dir = "L"
               elif A[2]:
                   OBJ.dir = "R"
               elif A[6] and A[7]:
                   if random.randint(0,3) > 1:
                       OBJ.dir = "R"
                   else:
                       OBJ.dir = "L"
               elif random.randint(0,2) >= 1:
                   OBJ.dir = "L"
               else:
                   OBJ.dir = "R"
           elif A[0]:
               OBJ.dir = "R"
           elif A[1]:
               OBJ.dir = "L"
           elif A[4] or A[5]: #ufar
               if A[2] and A[3]:
                   OBJ.Action()    
               elif A[3]:
                   OBJ.dir = "L"
               elif A[2]:
                   OBJ.dir = "R"
               elif A[6]:
                   OBJ.dir = "R"
               elif A[7]:
                   OBJ.dir = "L"
                   
       elif OBJ.dir == "D":
           OBJ.AIColliders[0].st = (OBJ.x+OBJ.speed,OBJ.y+OBJ.speed/2 )
           OBJ.AIColliders[1].st = (OBJ.x-OBJ.speed,OBJ.y+OBJ.speed/2 )
           OBJ.AIColliders[0].end = (OBJ.x+OBJ.speed,OBJ.y+2*OBJ.speed-4 )
           OBJ.AIColliders[1].end = (OBJ.x-OBJ.speed,OBJ.y+2*OBJ.speed-4 )
           
           OBJ.AIColliders[2].st = (OBJ.x+OBJ.speed/2,OBJ.y)
           OBJ.AIColliders[3].st = (OBJ.x-OBJ.speed/2,OBJ.y)
           OBJ.AIColliders[2].end = (OBJ.x+4*OBJ.speed,OBJ.y)
           OBJ.AIColliders[3].end = (OBJ.x-4*OBJ.speed,OBJ.y)

           OBJ.AIColliders[4].st = (OBJ.x+OBJ.speed,OBJ.y+2*OBJ.speed)
           OBJ.AIColliders[5].st = (OBJ.x-OBJ.speed,OBJ.y+2*OBJ.speed)
           OBJ.AIColliders[4].end = (OBJ.x+OBJ.speed,OBJ.y+5*OBJ.speed)
           OBJ.AIColliders[5].end = (OBJ.x-OBJ.speed,OBJ.y+5*OBJ.speed)
           
           OBJ.AIColliders[6].st = (OBJ.x+2*OBJ.speed,OBJ.y)
           OBJ.AIColliders[7].st = (OBJ.x-2*OBJ.speed,OBJ.y)
           OBJ.AIColliders[6].end = (OBJ.x+4*OBJ.speed,OBJ.y)
           OBJ.AIColliders[7].end = (OBJ.x-4*OBJ.speed,OBJ.y)
           
           OBJ.AIColliders[8].st = (OBJ.x-OBJ.speed/2,OBJ.y+OBJ.speed)
           OBJ.AIColliders[8].end = (OBJ.x+OBJ.speed/2, OBJ.y+OBJ.speed)
           
           A=[0,0,0,0,0,0,0,0,0]
           for i in range(len(OBJ.AIColliders)):
               for bike in spGroup:
                   if A[i]:
                       pass
                   for line in bike.Lines:
                       if OBJ.AIColliders[i].collideswith(line):
                           A[i] = True
                           break
           if (A[0] and A[1]) or A[8]:
               #dead ahead line
               if A[2] and A[3]:
                   OBJ.Action()
               elif A[3]:
                   OBJ.dir = "R"
               elif A[2]:
                   OBJ.dir = "L"
               elif A[6] and A[7]:
                   if random.randint(0,3) > 1:
                       OBJ.dir = "L"
                   else:
                       OBJ.dir = "R"
               elif random.randint(0,2) >= 1:
                   OBJ.dir = "R"
               else:
                   OBJ.dir = "L"
           elif A[0]:
               OBJ.dir = "L"
           elif A[1]:
               OBJ.dir = "R"
           elif A[4] or A[5]: #ufar
               if A[2] and A[3]:
                   OBJ.Action()    
               elif A[3]:
                   OBJ.dir = "R"
               elif A[2]:
                   OBJ.dir = "L"
               elif A[6]:
                   OBJ.dir = "L"
               elif A[7]:
                   OBJ.dir = "R"

       elif OBJ.dir == "R":
           OBJ.AIColliders[0].st = (OBJ.x+OBJ.speed/2,OBJ.y-OBJ.speed )
           OBJ.AIColliders[1].st = (OBJ.x+OBJ.speed/2,OBJ.y+OBJ.speed )
           OBJ.AIColliders[0].end = (OBJ.x+2*OBJ.speed+4,OBJ.y-OBJ.speed)
           OBJ.AIColliders[1].end = (OBJ.x+2*OBJ.speed+4,OBJ.y+OBJ.speed )
           
           OBJ.AIColliders[2].st = (OBJ.x,OBJ.y-OBJ.speed/2)
           OBJ.AIColliders[3].st = (OBJ.x,OBJ.y+OBJ.speed/2)
           OBJ.AIColliders[2].end = (OBJ.x,OBJ.y-2*OBJ.speed)
           OBJ.AIColliders[3].end = (OBJ.x,OBJ.y+2*OBJ.speed)

           OBJ.AIColliders[4].st = (OBJ.x+OBJ.speed*2,OBJ.y-OBJ.speed)
           OBJ.AIColliders[5].st = (OBJ.x+OBJ.speed*2,OBJ.y+OBJ.speed)
           OBJ.AIColliders[4].end = (OBJ.x+5*OBJ.speed,OBJ.y-OBJ.speed)
           OBJ.AIColliders[5].end = (OBJ.x+5*OBJ.speed,OBJ.y+OBJ.speed)
           
           OBJ.AIColliders[6].st = (OBJ.x,OBJ.y-2*OBJ.speed)
           OBJ.AIColliders[7].st = (OBJ.x,OBJ.y+2*OBJ.speed)
           OBJ.AIColliders[6].end = (OBJ.x,OBJ.y-4*OBJ.speed)
           OBJ.AIColliders[7].end = (OBJ.x,OBJ.y+4*OBJ.speed)
           
           OBJ.AIColliders[8].st = (OBJ.x+OBJ.speed,OBJ.y-OBJ.speed/2)
           OBJ.AIColliders[8].end = (OBJ.x+OBJ.speed, OBJ.y+OBJ.speed/2)
           
           A=[0,0,0,0,0,0,0,0,0]
           for i in range(len(OBJ.AIColliders)):
               for bike in spGroup:
                   if A[i]:
                       pass
                   for line in bike.Lines:
                       if OBJ.AIColliders[i].collideswith(line):
                           A[i] = True
                           break
           if (A[0] and A[1]) or A[8]:
               #dead ahead line
               if A[2] and A[3]:
                   OBJ.Action()
               elif A[3]:
                   OBJ.dir = "U"
               elif A[2]:
                   OBJ.dir = "D"
               elif A[6] and A[7]:
                   if random.randint(0,3) > 1:
                       OBJ.dir = "D"
                   else:
                       OBJ.dir = "U"
               elif random.randint(0,2) >= 1:
                   OBJ.dir = "U"
               else:
                   OBJ.dir = "D"
           elif A[0]:
               OBJ.dir = "D"
           elif A[1]:
               OBJ.dir = "U"
           elif A[4] or A[5]: #ufar
               if A[2] and A[3]:
                   OBJ.Action()    
               elif A[3]:
                   OBJ.dir = "U"
               elif A[2]:
                   OBJ.dir = "D"
               elif A[6]:
                   OBJ.dir = "D"
               elif A[7]:
                   OBJ.dir = "U"

       elif OBJ.dir == "L":
           OBJ.AIColliders[0].st = (OBJ.x-OBJ.speed/2,OBJ.y+OBJ.speed )
           OBJ.AIColliders[1].st = (OBJ.x-OBJ.speed/2,OBJ.y-OBJ.speed )
           OBJ.AIColliders[0].end = (OBJ.x-2*OBJ.speed-4,OBJ.y+OBJ.speed)
           OBJ.AIColliders[1].end = (OBJ.x-2*OBJ.speed-4,OBJ.y-OBJ.speed )
           
           OBJ.AIColliders[2].st = (OBJ.x,OBJ.y+OBJ.speed/2)
           OBJ.AIColliders[3].st = (OBJ.x,OBJ.y-OBJ.speed/2)
           OBJ.AIColliders[2].end = (OBJ.x,OBJ.y+2*OBJ.speed)
           OBJ.AIColliders[3].end = (OBJ.x,OBJ.y-2*OBJ.speed)

           OBJ.AIColliders[4].st = (OBJ.x-OBJ.speed*2,OBJ.y+OBJ.speed)
           OBJ.AIColliders[5].st = (OBJ.x-OBJ.speed*2,OBJ.y-OBJ.speed)
           OBJ.AIColliders[4].end = (OBJ.x-5*OBJ.speed,OBJ.y+OBJ.speed)
           OBJ.AIColliders[5].end = (OBJ.x-5*OBJ.speed,OBJ.y-OBJ.speed)
           
           OBJ.AIColliders[6].st = (OBJ.x,OBJ.y+2*OBJ.speed)
           OBJ.AIColliders[7].st = (OBJ.x,OBJ.y-2*OBJ.speed)
           OBJ.AIColliders[6].end = (OBJ.x,OBJ.y+4*OBJ.speed)
           OBJ.AIColliders[7].end = (OBJ.x,OBJ.y-4*OBJ.speed)
           
           OBJ.AIColliders[8].st = (OBJ.x-OBJ.speed,OBJ.y+OBJ.speed/2)
           OBJ.AIColliders[8].end = (OBJ.x-OBJ.speed, OBJ.y-OBJ.speed/2)
           
           A=[0,0,0,0,0,0,0,0,0]
           for i in range(len(OBJ.AIColliders)):
               for bike in spGroup:
                   if A[i]:
                       pass
                   for line in bike.Lines:
                       if OBJ.AIColliders[i].collideswith(line):
                           A[i] = True
                           break
           if (A[0] and A[1]) or A[8]:
               #dead ahead line
               if A[2] and A[3]:
                   OBJ.Action()
               elif A[3]:
                   OBJ.dir = "D"
               elif A[2]:
                   OBJ.dir = "U"
               elif A[6] and A[7]:
                   if random.randint(0,3) > 1:
                       OBJ.dir = "U"
                   else:
                       OBJ.dir = "D"
               elif random.randint(0,2) >= 1:
                   OBJ.dir = "D"
               else:
                   OBJ.dir = "U"
           elif A[0]:
               OBJ.dir = "U"
           elif A[1]:
               OBJ.dir = "D"
           elif A[4] or A[5]: #ufar
               if A[2] and A[3]:
                   OBJ.Action()    
               elif A[3]:
                   OBJ.dir = "D"
               elif A[2]:
                   OBJ.dir = "U"
               elif A[6]:
                   OBJ.dir = "U"
               elif A[7]:
                   OBJ.dir = "D"
       OBJ.dirChanged = True
