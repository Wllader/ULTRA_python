from dataclasses import dataclass

@dataclass
class Entity:
    name:str
    hp:int

    def deal_damage(self, dmg:int):
        self.hp -= dmg

@dataclass
class AttackingEntity(Entity):
    def attack(self, dmg:int, other:Entity):
        other.deal_damage(dmg)

@dataclass
class Enemy(AttackingEntity):
    sound:str

    def make_sound(self):
        print(self.sound)

@dataclass
class Npc(AttackingEntity):
    quest:str

    def get_quest(self):
        print(self.quest)


legolas = Npc("Legolas", 100, "Přines mi můj luk!")
e = Enemy("Goblin", 5, "Grrr!")

print(
    legolas,
    e,

    sep="\n"
)

e.attack(12, legolas)
legolas.attack(30, e)

print(
    legolas,
    e,

    sep="\n"
)
