from abc import ABC, abstractmethod


class MassMedia(ABC):
    name: str

    @abstractmethod
    def create_news(self, heroes,  place, info):
        pass


class Tv(MassMedia):
    def __init__(self, name):
        self.name = name

    def create_news(self, heroes, place):
        print(f'Breaking news from the {self.name}.')
        print(f'{heroes.name} saved the {place.name}!')
