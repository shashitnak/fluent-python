import math


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __mul__(self, scalar):
        return Vector(scalar*self.x, scalar*self.y)

    def __repr__(self):
        return f"Vector({self.x!r}, {self.y!r})"

    def __bool__(self):
        return bool(abs(self))


v1 = Vector(2, 4)
v2 = Vector(2, 1)
print(v1 + v2)

v = Vector(3, 4)
print(abs(v))
print(v*3)
print(abs(v)*3)
print(bool(v))
print(bool(Vector(0, 0)))
