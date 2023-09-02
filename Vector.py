from __future__ import annotations
import math

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    # __repr__ is used for debugging
    def __repr__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"
    
    # __str__ is used for printing
    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"
    
    def scalarProduct(self, other: Vector) -> Vector:
        return Vector(self.x * other.x, self.y * other.y, self.z * other.z)
    
    def crossProduct(self, other: Vector) -> Vector:
        return Vector(self.y * other.z - self.z * other.y,
                      self.z * other.x - self.x * other.z,
                      self.x * other.y - self.y * other.x)
    
    @property
    def magnitude(self) -> float:
        return math.sqrt(self.dot_product(self))

    def normalize(self) -> float:
        return self / self.magnitude
    
    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __mul__(self, constant: float) -> Vector:
        return Vector(self.x * constant, self.y * constant, self.z * constant) 