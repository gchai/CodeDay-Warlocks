#nested function definition test

def Func1():
   def Func2():
      Fx = 3
      name = "Func2"
      print name + " "+str(Fx)
      return Func1
   Fx = 100
   name = "Func1"
   print name + " "+str(Fx)
   Func2()
   return Func2


print "\ntesting function 1"
x = Func1()

print "\ntesting function 2 outside of func1."
y = x()
z = y()
print type(x())
print type(" ")
print type(9)
if x == z:
   print "x = y."
else:
   print "x does not refer to the same place as y."
