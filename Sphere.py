from Point import Point
from Vector import Vector

class Sphere:

    def __init__(self, center: Point, radius):
        self.center = center
        self.radius = radius 

    def normal(self, surfacePoint) -> Vector:
        return (surfacePoint - self.center).normalize()