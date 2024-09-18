from .pokebola import Pokebola

class PokebolaComum(Pokebola):
    def __init__(self, x, y, dx, dy, chance, jogo):
        super().__init__(x, y, dx, dy, chance, jogo)
        self.image = pygame.image.load('static/imagens/pokebola.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (30, 30))