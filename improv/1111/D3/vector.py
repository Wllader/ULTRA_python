

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

class Vector2:
    def __init__(self, x:float, y:float):
        self.x = x
        self.y = y

    def add(): pass
    def dot(): pass
    def mul(): pass
    def norm(): pass


if __name__ == "__main__":
    a = Vector2(3, 2)
    b = Vector2(5, -3)

    print(f"{a.add(b)=}")
    print(f"{a.mul(3)=}")
    print(f"{a.dot(b)=}")
    print(f"{a.norm()=}")