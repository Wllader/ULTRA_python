
# a = {
#     "x" : 3,
#     "y" : 1
# }

# b = {
#     "x" : 5,
#     "y" : 2
# }

# # =====

# # Součet:

# c = {
#     "x" : a["x"] + b["x"],
#     "y" : a["y"] + b["y"]
# }

# print(c)

# s = a["x"]*b["x"] + a["y"]*b["y"]

# print(s)

from typing import Self
from dataclasses import dataclass, asdict

@dataclass
class Vector2:
    """Tahle třída reprezentuje dvoudimenzionální vektor."""
    x:float
    y:float

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"
    
    def __add__(self, other:Self) -> Self:
        return Vector2(
            self.x + other.x,
            self.y + other.y
        )
    
    def __matmul__(self, other:Self) -> float:
        return self.x*other.x + self.y*other.y
    
    def __mul__(self, k:float) -> Self:
        return Vector2(
            k * self.x, #? Pronásobení x-ové složky floatovým číslem
            k * self.y
        )
    
    # __truediv__ - /
    # __floordiv__ - //
    # __pow__ - **
    # __mod__ - %

    def times(self, k:float) -> "Vector2":
        """Tahle funkce provede násobení vektoru s floatovým číslem"""
        return Vector2(
            k * self.x, #? Pronásobení x-ové složky floatovým číslem
            k * self.y
        )

a = Vector2(3, 1)
b = Vector2(5, 2)


c = a + b
s = a @ b
f = a * 7

print(c)
print(s)
print(f)

print(asdict(a))