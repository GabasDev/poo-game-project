from .pokemon import Pokemon
import pygame
import random

class Squirtle(Pokemon):
    def __init__(self, lista_pokemons):
        super().__init__(lista_pokemons, "static/imagens/squirtle.png")
        self._posicionar()
        self.velocidade = random.randint(1, 2)
        self.nome = "Pikachu"

    def mover(self):
        "Movimento vertical"
        self.rect.y += self.velocidade
        if self.rect.bottom > 600 or self.rect.top < 0:
            self.velocidade = -self.velocidade
