

# a = {
#     "x" : 3,
#     "y" : 1
# }

# b = {
#     "x" : 5,
#     "y" : -3
# }

# c = {
#     "x" : a["x"] + b["x"],
#     "y" : a["y"] + b["y"]
# }


from math import sqrt
from dataclasses import dataclass

@dataclass
class Vector2:
    x:float
    y:float

    # def __init__(self, x:float, y:float):
    #     self.x = x
    #     self.y = y

    @property
    def norm(self):
        return sqrt(self.x**2 + self.y**2)
    
    @norm.setter
    def norm(self, value):
        unit_v = self / self.norm
        tmp:"Vector2" = unit_v * value
        self.x, self.y = tmp.x, tmp.y
    
    # def __repr__(self) -> str:
    #     return f"({self.x}, {self.y})"

    def add(self, other:"Vector2") -> "Vector2":
        return Vector2(self.x + other.x, self.y + other.y)
    
    def __add__(self, other:"Vector2") -> "Vector2":
        return self.add(other)

    def dot(self, other:"Vector2") -> float:
        return self.x * other.x + self.y * other.y
    
    def __matmul__(self, other:"Vector2") -> float:
        return self.dot(other)
    
    def mul(self, alpha:float) -> "Vector2":
        return Vector2(alpha*self.x, alpha*self.y)
    
    def __mul__(self, alpha:float) -> "Vector2":
        return self.mul(alpha)
    
    def __truediv__(self, alpha:float) -> "Vector2":
        return self.mul(1/alpha)
    
    
    # __floordiv__  : //
    # __pow__       : **
    # __mod__       : %




if __name__ == "__main__":
    a = Vector2(3, 4)
    b = Vector2(5, -3)

    print(f"{a=}, {b=}")
    print(f"{a.add(b)=}")
    print(f"{a + b=}")
    print(f"{a.mul(3)=}")
    print(f"{a * 3=}")

    print(f"{a.dot(b)=}")
    print(f"{a @ b=}")
    print(f"{a.norm=}")

    a.x = 5
    print(f"{a=}")
    print(f"{a.norm=}")

    a.norm = 12
    print(f"{a.norm=}")
    print(f"{a=}")
