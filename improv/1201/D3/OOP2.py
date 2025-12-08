from abc import ABC
from typing import Protocol
from dataclasses import dataclass, field


class LoudComponent(Protocol):
    def make_sound(self): ...

class AttackingComponent(Protocol):
    def attack(self, dmg:int, target:"Entity"):
        target.take_damage(dmg)

@dataclass
class Entity(ABC):
    name:str
    hp:int

    # def __init__(self, name:str, hp:int):
    #     super().__init__()
    #     self.name = name
    #     self.hp = hp

    def __repr__(self) -> str:
        return f"{self.name.capitalize()}: {max(self.hp, 0)}"

    def take_damage(self, dmg:int):
        self.hp -= dmg

# class AttackingEntity(Entity, ABC):
#     def __init__(self, name, hp):
#         super().__init__(name, hp)

#     def attack(self, dmg:int, target:Entity):
#         target.take_damage(dmg)

# class LoudEntity(Entity, ABC):
#     def __init__(self, name, hp, sound):
#         super().__init__(name, hp)
#         self.sound = sound

#     def make_sound(self):
#         print(self.sound)


@dataclass(repr=False)
class Enemy(Entity, AttackingComponent, LoudComponent):
    sound:str

    # def __init__(self, name, hp, sound:str):
    #     super().__init__(name, hp)
    #     self.sound = sound

    def make_sound(self):
        print(self.sound)


@dataclass
class Npc(Entity, AttackingComponent):
    quest:str = field(repr=False)

    # def __init__(self, name, hp, quest:str):
    #     super().__init__(name, hp)
    #     self.quest = quest

    def get_quest(self):
        print(self.quest)


@dataclass
class Critter(Entity, LoudComponent):
    sound:str

    # def __init__(self, name, hp, sound:str):
    #     super().__init__(name, hp)
    #     self.sound = sound

    def make_sound(self):
        print(self.sound)

    

if __name__ == "__main__":
    ent = Entity("Test", -5)
    legolas = Npc("Legolas", 100, "Přines mi můj luk!")
    e = Enemy("Goblin", 5, "Grrr")
    lightbug = Critter("Světluška", 1, "Bzzz")

    print(
        legolas, e, lightbug, ent,
        sep="\n",
        end="\n\n"
    )

    e.attack(20, legolas)
    legolas.attack(30, e)
    e.attack(5, lightbug)

    print(
        legolas, e, lightbug,
        sep="\n",
        end="\n\n"
    )
