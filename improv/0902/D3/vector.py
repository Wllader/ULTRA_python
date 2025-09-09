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
    def len(self):
        return sqrt(self.x**2 + self.y**2)
    

    @len.setter
    def len(self, value:float):
        unit_v = self * (1/self.len)
        tmp:Vector2 = unit_v * value
        self.x, self.y = tmp.x, tmp.y


    #Dunder methods
    # def __repr__(self):
    #     return f"({self.x}, {self.y})"


    def __add__(self, other:"Vector2") -> "Vector2":
        return self.add(other)


    def __mul__(self, k:float) -> "Vector2":
        return self.times(k)


    def __matmul__(self, other:"Vector2") -> float:
        return self.dot(other)
    
    #? __truediv__ : /
    #? __floordiv__ : //
    #? __pow__ : **
    #? __mod__ : %
    #? __sub__ : -


    def __mod__(self, other:"Vector2"):
        return f"{self.x} !!! {other.x}"


    #Methods
    def add(self, other:"Vector2"):
        return Vector2(
            self.x + other.x,
            self.y + other.y
        )
    
    def dot(self, other:"Vector2"):
        return self.x * other.x + self.y * other.y
    

    def times(self, alpha:float):
        return Vector2(alpha * self.x, alpha * self.y)
    
    def norm(self):
        return sqrt(self.x**2 + self.y**2)
    


if __name__ == "__main__":
    a = Vector2(5, 2)
    b = Vector2(3, -1)

    # print(
    #     f"{a.add(b)=}",
    #     f"{b.add(a)=}",
    #     f"{a.dot(b)=}",
    #     f"{b.dot(a)=}",
    #     f"{a.times(5)=}",
    #     f"{b.times(5)=}",
    #     f"{a.norm()=}",
    #     f"{b.norm()=}",

    #     f"{a+b=}",
    #     f"{a*3=}",
    #     f"{a@b=}",

    #     f"{a%b=}",
    #     f"{a.len}",

    #     sep="\n\n"
    # )

    print(
        f"{a=}",
        f"{a.len=}",

        sep="\n"
    )

    a.len = 5

    print(
        f"{a=}",
        f"{a.len=}",

        sep="\n"
    )