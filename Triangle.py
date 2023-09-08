from Point import Point
from Vector import Vector

class Triangle:

    def __init__(self, a: Point, b: Point, c: Point):
        self.a: a
        self.b: b
        self.c: c

        abVector = b - a
        bcVector = c - b

        self.normalVector = abVector.crossProduct(bcVector).normalize()

    def normal(self) -> Vector:
        return self.normalVector