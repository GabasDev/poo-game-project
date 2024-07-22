class Chance:
    def __init__(self):
        self.chance = 3

    def perdeuChance(self):
        self.chance -= 1
        
    def mostrarChance(self):
        return self.chance
