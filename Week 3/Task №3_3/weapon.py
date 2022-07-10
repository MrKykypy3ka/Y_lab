from abc import ABC


class Weapon(ABC):
    pass


class Gun(Weapon):
    def fire_a_gun(self):
        print('PIU PIU')


class Laser(Weapon):
    def incinerate_with_lasers(self):
         print('Wzzzuuuup!')


class Limbs(Weapon):
    def roundhouse_kick(self):
        print('Bump')