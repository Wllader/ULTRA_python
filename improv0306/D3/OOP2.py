from dataclasses import dataclass


@dataclass
class Entity:
    name:str
    hp:int

    def deal_damage(self, dmg:int):
        self.hp -= dmg


@dataclass
class AtackingEntity(Entity):
    def attack(self, dmg:int, other:Entity):
        other.deal_damage(dmg)



@dataclass
class Enemy(AtackingEntity):
    sound:str

    def make_sound(self):
        print(self.sound)


@dataclass
class Npc(AtackingEntity):
    quest:str

    def get_quest(self):
        print(self.quest)

@dataclass
class Critter(Entity):
    sound:str

    def make_sound(self):
        print(self.sound)

if __name__ == "__main__":
    legolas = Npc("Legolas", 100, "Přines mi můj luk!")
    e = Enemy("Goblin", 5, "Grrr!")
    ligthbug = Critter("Světluška", 1, "Bzzz")


    print(
        legolas,
        e,
        ligthbug,

        sep="\n"
    )

    e.attack(15, legolas)
    legolas.attack(30, e)
    e.attack(5, ligthbug)

    print("----")

    print(
        legolas,
        e,
        ligthbug,

        sep="\n"
    )