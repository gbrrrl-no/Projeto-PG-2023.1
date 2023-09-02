class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):  # __repr__ is used for debugging
        return f"Point({self.x}, {self.y}, {self.z})"

    def __str__(self):  # __str__ is used for printing
        return f"({self.x}, {self.y}, {self.z})"

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)