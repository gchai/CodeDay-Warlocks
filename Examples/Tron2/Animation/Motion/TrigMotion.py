#	Trig motion module
#	this module is intended to provide 'motion' objects which have 
#		- GetNextVect() return the next vector [dx,dy] that is logical for the type of motion. 
#		- GetPrevVects(num) returns the last num vector(s) [dx,dy] returned by GetNextVect()
#		- GetSpeed() returns the average speed
#		- GetMotionType() returns 'p' 'l' 's' 'c' for parabolic, linear, sin, cos
#		- IsOscillating() returns true if motion type is using oscillation
#		- SetOscillation(bounds = [minspeed, maxspeed], type= 0) set to no'0' or perpendicular'1' or parallel'2' oscillation.  
#		- __init__(self, type = 'l', speed = 12)
#		
#
#
#
class TrigMotion():
		def __init__(self, MotType = 'l', speed = 12)
		def GetNextVect(self):
				#finish this
		def GetPrevVects(self, num = 1):
				
