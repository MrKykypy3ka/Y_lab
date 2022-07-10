from abc import ABC, abstractmethod
from weapon import Laser, Gun, Limbs


class Hero(ABC):
    @property
    def name(self):
        raise NotImplementedError

    @abstractmethod
    def attack(self):
        pass


class SuperHero(Hero):
    @abstractmethod
    def ultimate(self):
        pass


class Superman(SuperHero, Laser, Limbs):
    name = 'Clark Kent'

    def ultimate(self):
        self.incinerate_with_lasers()

    def attack(self):
        self.roundhouse_kick()
        self.ultimate()


class ChuckNorris(Hero, Gun, Limbs):
    name = 'Chuck Norris'

    def attack(self):
        self.roundhouse_kick()
        self.fire_a_gun()

