from abc import ABC, abstractmethod


class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass


class Sword(Weapon):
    def attack(self):
        print("Боец наносит удар мечом")


class Bow(Weapon):
    def attack(self):
        print("Боец делает выстрел из лука")


class Tank(Weapon):
    def attack(self):
        print("Боец делает выстрел из танка")


class Fighter():
    def __init__(self, weapon: Weapon):
        self.weapon = weapon

    def changeWeapon(self, weapon: Weapon):
        self.weapon = weapon
        print(f"Боец изменил оружие на {self.weapon.__class__.__name__}")
    def fight(self):
        self.weapon.attack()
        print("Монстр побежден")

class Monster():
    pass


sword1 = Sword()
bow1 = Bow()
tank1 = Tank()
fighter = Fighter(sword1)
fighter.fight()
fighter.changeWeapon(bow1)
fighter.fight()
fighter.changeWeapon(tank1)
fighter.fight()