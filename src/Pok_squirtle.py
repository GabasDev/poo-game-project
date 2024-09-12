from .pokemon import Pokemon
import pygame
import random

class Squirtle(Pokemon):
    def __init__(self, lista_pokemons):
        super().__init__(lista_pokemons, "static/imagens/squirtle.png")
        # self.image = pygame.transform.scale(self.image, (50, 50))
        # self.rect = self.image.get_rect()
        self._posicionar()
        self.velocidade = random.randint(1, 2)

    def mover(self):
        "Movimento vertical"
        self.rect.y += self.velocidade
        if self.rect.bottom > 600 or self.rect.top < 0:
            self.velocidade = -self.velocidade
