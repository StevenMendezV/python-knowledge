class Rectangle:

    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return self.base * self.height

class Square(Rectangle):

    def __init__(self, side):
        super().__init__(side, side)


if __name__ == "__main__":
    rectangle = Rectangle(3, 4)
    print(rectangle.area())

    square = Square(5)
    print(square.area())

