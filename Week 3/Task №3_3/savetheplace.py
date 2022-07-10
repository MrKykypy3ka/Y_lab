from massmedia import MassMedia
from heroes import SuperHero
from places import Place


class SavePlace:
    def __init__(self, hero: SuperHero, place: Place, mass_media: MassMedia):
        self.place = place
        self.hero = hero
        self.mass_media = mass_media
        self.find()
        hero.attack()
        self.create_news()

    def find(self):
        return self.place.get_antagonist()

    def create_news(self):
        self.mass_media.create_news(self.hero, self.place)

