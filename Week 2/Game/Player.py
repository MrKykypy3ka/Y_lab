class Player:
    def __init__(self, genus, figure):
        self.genus = genus
        self.figure = figure

    def __eq__(self, other):
        return True if self.genus == other else False

    def __call__(self):
        return self.figure
