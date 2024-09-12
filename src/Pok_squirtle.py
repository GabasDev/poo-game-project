from .pokemon import Pokemon
import pygame
import random

class Squirtle(Pokemon):
    def _init_(self, lista_pokemons):
        super()._init_(lista_pokemons, "static/imagens/squirtle.png")
        self._posicionar()
        self.velocidade = random.randint(1, 2)

    def mover(self):
        "Movimento vertical"
        self.rect.y += self.velocidade
        if self.rect.bottom > 600 or self.rect.top < 0:
            self.velocidade = -self.velocidade
