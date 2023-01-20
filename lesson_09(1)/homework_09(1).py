class Point:
    x = None
    y = None

    def __init__(self, x, y):
        self.x, self.y = x, y


class Circle(Point):
    x = None
    y = None
    radius = None

    def __init__(self, x, y, radius):
        self.x, self.y, self.radius = x, y, radius

    def perimetr(self):
        print(f"{self.radius * 2 * 3.14} is perimetr")

    def area(self):
        print(f"{self.radius ** 2 * 3.14} is area of circle")


if __name__ == "__main__":
    circle = Circle(1, 2, 5)
    circle.perimetr()
    circle.area()

import math


class Triangle():
    x1 = None
    x2 = None
    x3 = None
    y1 = None
    y2 = None
    y3 = None

    def __init__(self, x1, x2, x3, y1, y2, y3):
        self.x1, self.x2, self.x3, self.y1, self.y2, self.y3 = x1, x2, x3, y1, y2, y3

        a = math.sqrt(({self.x2} - {self.x3}) ** 2 + ({self.y3} - {self.y2}) ** 2)

    def area(self):
        print(
            f"{0.5 * ({self.x1} * ({self.y2} - {self.y3}) + {self.x2} * ({self.y3} - {self.y1}) + {self.x3} * ({self.y1} - {self.y2}))} is area of triangle")

    def perimetr(self):
        print(f"{a}")


if __name__ == "__main__":
    triangle = Triangle(3, 11, 10, 2, 4, 10)
    print(triangle)
    triangle.area()
