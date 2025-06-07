

class Animal:
    def __init__(self, name:str):
        self.name = name

    def say_my_name(self):
        print(self.name)


class Cat(Animal):
    def __init__(self, name, sound = "meow"):
        super().__init__(name)
        self.sound = sound

    def make_a_sound(self):
        print(self.sound)


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def tell_my_breed(self):
        print(f"My breed is {self.breed}")


class PoliceDog(Dog):
    def __init__(self, name, breed = "Malinois", unit = "K9"):
        super().__init__(name, breed)
        self.unit = unit


class Brick:
    def __init__(self):
        pass

    def say_my_name(self):
        print(f"Já jsem cihla!")


def process_animals(animals:list[Animal]):
    for animal in animals:
        animal.say_my_name()


if __name__ == "__main__":
    pd = PoliceDog("Rex")
    d = Dog("Candy", "GR")
    c = Cat("Micka")
    b = Brick()

    process_animals([pd, d, c, b])



