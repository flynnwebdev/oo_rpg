class PirateCoin:
    def __init__(self, doubloons=0, pieces_of_eight=0, reales=0):
        self.doubloons = doubloons
        self.pieces_of_eight = pieces_of_eight
        self.reales = reales

    # Returns total value in reales
    def value(self):
        return self.doubloons * 32 + self.pieces_of_eight * 8 + self.reales


class Character:
    def __init__(self, name, race):
        self.name = name
        self.race = race
        self.purse = PirateCoin()


class Combat:
    def __init__(self, hp=50, attack=10):
        self.hp = hp
        self.attack = attack

    def __repr__(self):
        return f'{self.hp}HP {self.attack}ATT'

    def battle(self, other_combatant):
        pass


class Warrior(Character):
    def __init__(self, name, race):
        super().__init__(name, race)
        self.combat = Combat(hp=80, attack=20)


class Mage(Character):
    def __init__(self, name, race):
        super().__init__(name, race)
        self.combat = Combat(hp=40, attack=30)


class Totem():
    def __init__(self, hp, attack):
        self.combat = Combat(hp, attack)


class Vendor(Character):
    def __init__(self, name, race):
        super().__init__(name, race)
        self.goods = []
        self.gold = 1000


conan = Warrior("Conan", "Human")
galadriel = Mage("Galadriel", "Elf")
grok = Vendor("Grok", "Orc")
fire_totem = Totem(10, 20)

print(conan.__dict__)
print(galadriel.__dict__)
print(grok.__dict__)
print(fire_totem.__dict__)
