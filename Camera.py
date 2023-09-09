from Point import Point
from Vector import Vector

class Camera:
    
    def __init__(self, origin: Point, view: Point, up: Vector, v: Vector, u: Vector, distance, hRes, vRes):
        self.origin = origin
        self.viewPoint = view
        self.upVector = up
        self.wVector = (origin - view).normalize()
        self.vVector = v.normalize()
        self.uVector = u.normalize()
        self.distance = distance
        self.hRes = hRes
        self.vRes = vRes
        