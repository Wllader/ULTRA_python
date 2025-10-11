from abc import ABC
from dataclasses import dataclass

class Entity(ABC):
    def __init__(self, name:str, hp:int):
        self.name = name
        self.hp = hp

    # def __repr__(self) -> str:
    #     return f"{self.name.capitalize()}: {max(self.hp, 0)}"

    def deal_damage(self, dmg:int):
        self.hp -= dmg

class AttackingEntity(Entity, ABC):
    def __init__(self, name, hp):
        super().__init__(name, hp)

    def attack(self, dmg:int, target:Entity):
        target.deal_damage(dmg)



class Enemy(AttackingEntity):
    def __init__(self, name, hp, sound:str):
        super().__init__(name, hp)
        self.sound = sound

    def make_sound(self):
        print(self.sound)


class Npc(AttackingEntity):
    def __init__(self, name, hp, quest:str):
        super().__init__(name, hp)
        self.quest = quest

    def get_quest(self):
        print(self.quest)

class Critter(Entity):
    def __init__(self, name, hp, sound:str):
        super().__init__(name, hp)
        self.sound = sound

    def make_sound(self):
        print(self.sound)


if __name__ == "__main__":
    legolas = Npc("Legolas", 100, "Přines mi můj luk!")
    e = Enemy("Goblin", 5, "Grrr!")
    lightbug = Critter("Světluška", 1, "Bzzz")

    print(
        legolas,
        e,
        lightbug,

        sep="\n",
        end="\n\n"
    )

    e.attack(20, legolas)
    legolas.attack(30, e)
    e.attack(5, lightbug)

    print(
        legolas,
        e,
        lightbug,

        sep="\n",
        end="\n\n"
    )

