'''Assignment 6'''
class Shape:
    def what_am_i(self):
        print("I am a shape")
    
class Square(Shape):
    def __init__(self, s1):
        self.s1 = s1
    def calculate_perimeter(self):
        return self.s1 * 4

class Rectangle(Shape):
    def __init__(self, w, l):
        self.width = w
        self.length = l
    def calculate_perimeter(self):
        return 2 * (self.width + self.length)

square = Square(7)
rectangle = Rectangle(4,7)

square.what_am_i()
rectangle.what_am_i()
