# a = {
#     "x" : 3,
#     "y" : 1
# }

# b = {
#     "x" : 5,
#     "y" : 2
# }


# c = {
#     "x" : a["x"] + b["x"],
#     "y" : a["y"] + b["y"]
# }

# s = a["x"]*b["x"] + a["y"]*b["y"]

# print(
#     a, b, c, s,

#     sep="\n"
# )

from dataclasses import dataclass
import math

@dataclass
class Vector2:
    """Třída reprezentující dvoudimenzionální vektor"""
    x:float
    y:float

    @property
    def lenght(self):
        return math.sqrt(self.x**2 + self.y**2)


    @lenght.setter
    def lenght(self, l):
        unit_v = self * (1/self.lenght)
        tmp = unit_v * l
        self.x, self.y = tmp.x, tmp.y

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"
    
    def __add__(self, other:"Vector2") -> "Vector2":
        return Vector2(
            self.x + other.x,
            self.y + other.y
        )
    
    def __matmul__(self, other:"Vector2") -> float:
        return self.x * other.x + self.y * other.y
    
    def __mul__(self, alpha:float) -> "Vector2":
        return Vector2(self.x * alpha, self.y * alpha)

    # __turediv__ : /
    # __floordiv__ : //
    # __pow__ : **
    # __mod__ : %
         

    



a = Vector2(3, 1)
b = Vector2(2, 3)

a.x = 5
a.lenght = 10



print(
    f"{a}",
    f"{a.lenght=}",
    f"{a + b=}",
    f"{b*5=}",
    f"{a * b=}",

    sep="\n"
)