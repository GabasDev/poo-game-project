from .pokemon import Pokemon
import pygame
import random

class Charmander(Pokemon):
    def _init_(self, lista_pokemons):
        super()._init_(lista_pokemons, "static/imagens/charmander.png")
        self._posicionar()
        self.velocidade = random.randint(1, 4)

    def mover(self):
        "Movimento diagonal"
        self.rect.x += self.velocidade
        self.rect.y += self.velocidade
        if self.rect.right > 800 or self.rect.top < 0:
            self.velocidade = -self.velocidade
        elif self.rect.left < 0 or self.rect.bottom > 600:
            self.velocidade = -self.velocidade
