class Shape:
    def __init__(self,type):
        self.__type = type
    def get_area(self):
        pass
    def get_perimeter(self):
        pass

import math
class Circle(Shape):
    def __init__(self,radius):
        Shape.__init__(self,'circle')
        self.radius = radius
    def get_area(self):
        return math.pi*self.radius**2
    def get_perimeter(self):
        return 2*math.pi*self.radius
c = Circle(10)
print(c.get_area())
print(c.get_perimeter())


class Square(Shape):
    def __init__(self,side):
        Shape.__init__(self,'square')
        self.side = side
    def get_area(self):
        return self.side * self.side
    def get_perimeter(self):
        return 4*self.side
s = Square(3)
print(s.get_area())
print(s.get_perimeter())
