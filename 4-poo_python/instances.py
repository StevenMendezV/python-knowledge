class Coordinate:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, another_coordinate):
        x_diff = (self.x - another_coordinate.x)**2
        y_diff = (self.y - another_coordinate.y)**2

        return (x_diff + y_diff)**0.5

if __name__ == "__main__":
    coor_1 = Coordinate(3, 30)
    coor_2 = Coordinate(4, 8)

    print(coor_1.distance(coor_2))
    print(isinstance(coor_2, Coordinate))
