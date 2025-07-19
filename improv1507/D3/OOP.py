
class Animal:
    def __init__(self, name:str):
        self.name = name

    def say_my_name(self):
        print(self.name)

class Cat(Animal):
    def __init__(self, name:str, color:str):
        super().__init__(name)
        self.color = color
        self.sound = "meow"

    def make_a_sound(self):
        print(self.sound)

class Dog(Animal):
    def __init__(self, name:str, breed:str):
        super().__init__(name)
        self.breed = breed
        self.sound = "woof!"

    def make_a_sound(self):
        print(self.sound)

class PoliceDog(Dog):
    def __init__(self, name, breed="Malinois", unit="K9"):
        super().__init__(name, breed)
        self.unit = unit
        self.sound = "Rawrrr"


class Brick:
    def __init__(self):
        pass

    def say_my_name(self):
        print("Já jsem cihla!")


def process_animals(animals:list[Animal]):
    for animal in animals:
        animal.say_my_name()


if __name__ == "__main__":
    pd = PoliceDog("Rex")
    d = Dog("Candy", "GR")
    c = Cat("Micka", "Red")
    b = Brick()

    process_animals([pd, d, c, b])