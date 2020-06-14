from math import sqrt
###################     CLASS RECTANGLE      ####################
class Rectangle :
    def __init__(self,length, bredth):
        self.length = length
        self.bredth = bredth

    def Area(self):
        A = self.length * self.bredth
        return A

    def Perimater(self):
        P = (self.length + self.bredth) * 2
        return P
####################################################################
################         CLASS  TRIANGLE         ###################
class Triangle :
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def Perimeter(self):
        P = self.a + self.b + self.c
        return P

    def Area(self):
        s = self.Perimeter() / 2
        A = sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        return A
###################################################################
##############          CLASS RHOMBUS          ####################
class Rhombus :
    def __init__(self,x,y,a_side,):
        self.x = x
        self.y = y
        self.a_side = a_side

    def Area(self):
        A =( self.x * self.y )/2
        return A

    def Perimeter(self):
        P = 4 * self.a_side
        return P

###############################################################
##############         CLASS CIRCLE          ##################
class Circle :
    def __init__(self,radius):
        self.radius = radius

    def Area(self):
        A = 3.14 * (self.radius ** 2)
        return A

    def Diameter(self):
        D = 2 * self.radius
        return D

    def Circumference(self):
        C  = 2 * 3.14 * self.radius
        return C
