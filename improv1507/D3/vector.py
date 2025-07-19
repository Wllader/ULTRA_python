

# a = {
#     "x" : 5,
#     "y" : 2
# }

# b = {
#     "x" : 3,
#     "y" : 1
# }

# c = {
#     "x" : a["x"] + b["x"],
#     "y" : a["y"] + b["y"]
# }

# s = a["x"]*b["x"] + a["y"]*b["y"]

# print(
#     a,b,c,s,
#     sep="\n"
# )

from math import sqrt
from dataclasses import dataclass

@dataclass
class Vector2:
    x:float
    y:float

    @property
    def len(self):
        return sqrt(self.x**2 + self.y**2)
    
    @len.setter
    def len(self, value):
        unit_v = self * (1/self.len)
        tmp:Vector2 = unit_v * value
        self.x, self.y = tmp.x, tmp.y

    # def __repr__(self) -> str:
    #     return f"({self.x}, {self.y})"
    
    def __add__(self, other:"Vector2") -> "Vector2":
        return self.add(other)
    
    def __mul__(self, k:float) -> "Vector2":
        return self.times(k)
    
    def __matmul__(self, other:"Vector2") -> float:
        return self.dot(other)

    def add(self, other:"Vector2"):
        return Vector2(self.x + other.x, self.y + other.y)
    
    def dot(self, other:"Vector2") -> float:
        return self.x * other.x + self.y * other.y

    def times(self, k:float):
        return Vector2(k * self.x, k * self.y)
    
    # __truediv__ : /
    # __floordiv__ : //
    # __pow__ : **
    # __mod__ : %
    


if __name__ == "__main__":
    v = Vector2(5, 2)
    u = Vector2(3, 1)

    # u.y = 0
    u.len = 13

    print(
        u, v,
        u + v,
        u * 3,
        #~ 3 * u,
        u @ v,
        u.len,

        sep="\n"
    )