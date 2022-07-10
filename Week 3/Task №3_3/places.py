from abc import ABC, abstractmethod


class Place(ABC):
    @abstractmethod
    def get_antagonist(self):
        pass

    @property
    def name(self):
        raise NotImplementedError


class Kostroma(Place):
    name = 'Kostroma'

    def get_antagonist(self):
        print('Orcs hid in the forest')


class Tokyo(Place):
    name = 'Tokyo'

    def get_antagonist(self):
        print('Godzilla stands near a skyscraper')


class Krypton(Place):
    name = 'Krypton'
    coordinates = [37, 83]

    def get_antagonist(self):
        print('The Kryptonians came for Superman')
