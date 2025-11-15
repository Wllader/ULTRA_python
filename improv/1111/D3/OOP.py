

class Animal:
    def __init__(self, name:str):
        self.name = name

    def say_my_name(self):
        print(self.name)

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def show_off(self):
        print(f"I'm {self.color}")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def tell_my_breed(self):
        print(f"My breed is {self.breed}")

class PoliceDog(Dog):
    def __init__(self, name, breed="Malinois", unit="K9"):
        super().__init__(name, breed)
        self.unit = unit

    def say_my_name(self):
        print(f"Jménem zákona! {self.name}")


class Brick:
    def __init__(self):
        pass

    def say_my_name(self):
        print("Já jsem cihla")


if __name__ == "__main__":
    a = Animal("Žofka")
    a.say_my_name()

    b = Brick()
    b.say_my_name()

    c = Cat("Garfield", "red")
    c.say_my_name()
    c.show_off()

    d = Dog("Candy", "GR")
    d.say_my_name()
    d.tell_my_breed()

    pd = PoliceDog("Rex")
    pd.say_my_name()
    pd.tell_my_breed()

    l:list[Animal] = [a, b, c, d, pd]
    for an in l:
        an.say_my_name()

