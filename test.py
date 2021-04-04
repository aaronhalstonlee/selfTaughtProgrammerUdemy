class Square():
    square_list = []
    
    def __init__(self, s1):
        self.s1 = s1
        self.square_list.append(self.s1)

square1 = Square(5)
square2 = Square(6)
square3 = Square(7)
print(square1.square_list)
