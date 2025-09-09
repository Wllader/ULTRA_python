

class Animal:
    def __init__(self, name:str):
        self.name = name

    def say_my_name(self):
        print(self.name)

    @staticmethod
    def say_many_names(l:list["Animal"]):
        for a in l:
            a.say_my_name()

    @staticmethod
    def CreateTest() -> "Animal":
        return Animal("Test")


class Fish(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color


class AnimalWithSound(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.sound = None

    def make_a_sound(self):
        print(self.sound)

    @staticmethod
    def make_multiple_sounds(l:list["AnimalWithSound"]):
        for a in l:
            a.make_a_sound()


class Cat(AnimalWithSound):
    def __init__(self, name:str, color:str):
        super().__init__(name)
        self.color = color
        self.sound = "meow"


class Dog(AnimalWithSound):
    def __init__(self, name, breed:str):
        super().__init__(name)
        self.sound = "woof!"


class PoliceDog(Dog):
    def __init__(self, name, breed:str="Malinois", unit="K9"):
        super().__init__(name, breed)
        self.unit = unit
        self.sound = "rawwrrr!"


class Brick:
    def say_my_name(self):
        print("Já jsem cihla!")


if __name__ == "__main__":
    a = Animal("Aleš")
    b = Cat("Micka", "Red")
    c = Brick()
    d = Dog("Candy", "GR")
    e = PoliceDog("Rex")

    AnimalWithSound.make_multiple_sounds([b, d, e])

