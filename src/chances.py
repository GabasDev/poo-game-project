class Chance:
    def __init__(self):
        self.chance = 3

    def _perdeu_chance(self):
        self.chance -= 1
        
    def _mostrar_chance(self):
        return self.chance
