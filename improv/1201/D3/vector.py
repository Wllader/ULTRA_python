from math import sqrt


class Vector2:
    def __init__(self, x:float, y:float):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"

    def add(self) -> "Vector2": ... #sub?
    def dot(self) -> float: ...
    def mul(self) -> "Vector2": ... #div?
    def norm(self) -> float: ...


if __name__ == "__main__":
    a = Vector2(3, 4)
    b = Vector2(5, -3)

    print(f"{a=}, {b=}")

    print(f"{a.add(b)=}")
    print(f"{Vector2.add(a, b)=}")

    print(f"{a.mul(3)=}")
    print(f"{Vector2.mul(a, 3)=}")

    print(f"{a.dot(b)=}")
    print(f"{Vector2.dot(a, b)=}")

    print(f"{a.norm()=}, {b.norm()=}")