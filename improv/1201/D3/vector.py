from math import sqrt


class Vector2:
    def __init__(self, x:float, y:float):
        self.x = x
        self.y = y

    @property
    def norm(self) -> float: #getter
        return sqrt(self.x*self.x + self.y*self.y)
    

    @norm.setter
    def norm(self, value:float):
        print(f"Changing norm of {self} from {self.norm} to {value}...")
        unit_v = self / self.norm
        tmp:"Vector2" = unit_v * value
        self.x, self.y = tmp.x, tmp.y



    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"

    def add(self, other:"Vector2") -> "Vector2":
        return Vector2(
            self.x + other.x,
            self.y + other.y
        )
    
    def __add__(self, other:"Vector2") -> "Vector2":
        return self.add(other)

    def dot(self, other:"Vector2") -> float:
        return self.x * other.x + self.y * other.y
    
    def __matmul__(self, other:"Vector2") -> float:
        return self.dot(other)
    
    def mul(self, k:float) -> "Vector2":
        return Vector2(
            k*self.x,
            k*self.y
        )
    
    def __mul__(self, k:float) -> "Vector2":
        return self.mul(k)
    

    def div(self, k:float) -> "Vector2":
        return self.mul(1/k)
    
    def __truediv__(self, k:float) -> "Vector2":
        return self.div(k)
    
    def __mod__(self, s:str) -> str:
        return f"{s}_{self}_{s}"
    

    # __add__       : +
    # __mul__       : *
    # __matmul__    : @
    # __truediv__   : /
    # __floordiv__  : //
    # __pow__       : **
    # __mod__       : %

    


if __name__ == "__main__":
    a = Vector2(3, 4)
    b = Vector2(5, -3)

    print(f"{a=}, {b=}")

    print(f"{a + b=}")
    print(f"{a.add(b)=}")
    print(f"{Vector2.add(a, b)=}")

    print(f"{a * 3=}")
    print(f"{a.mul(3)=}")
    print(f"{Vector2.mul(a, 3)=}")

    print(f"{a @ b=}")
    print(f"{a.dot(b)=}")
    print(f"{Vector2.dot(a, b)=}")

    print(f"{a.norm=}, {b.norm=}")

    a.y = 2


    print(f"{a=}, {b=}")
    print(f"{a.norm=}, {b.norm=}")

    a.norm = 7

    print(f"{a=}, {b=}")
    print(f"{a.norm=}, {b.norm=}")

    print(b % "Ahoj")
