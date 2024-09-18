import pygame
import random
import math
from .pokemon import Pokemon

class Bulbasaur(Pokemon):
    def __init__(self, lista_pokemons):
        super().__init__(lista_pokemons, "static/imagens/Bulbassauro.png")

        self._posicionar()
        self.velocidade = random.randint(1, 3)
        "Inicia com um ângulo aleatório"
        self.angulo = random.uniform(0, 2 * math.pi)
        self.nome = "Bulbasaur"  
    def mover(self):
        "Movimento circular"
        centro_x, centro_y = 400, 300
        raio = 100
        "Atualiza o ângulo com base na velocidade"
        self.angulo += 0.01 * self.velocidade  

        self.rect.x = centro_x + raio * math.sin(self.angulo) - self.rect.width / 2
        self.rect.y = centro_y + raio * math.cos(self.angulo) - self.rect.height / 2

        "Garante que o Pokémon permaneça dentro dos limites da tela"
        if self.rect.right < 0:
            self.rect.left = 800
        elif self.rect.left > 800:
            self.rect.right = 0
        if self.rect.bottom < 0:
            self.rect.top = 600
        elif self.rect.top > 600:
            self.rect.bottom = 0
