from Point import Point
from Vector import Vector

class Plane:

    def __init__(self, point: Point, normal: Vector):
        self.point = point
        self.normalVector = normal.normalize()

    def normal(self) -> Vector:
        return self.normalVector