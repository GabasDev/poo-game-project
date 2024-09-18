from .pokemon import Pokemon
import pygame
import random

class Charmander(Pokemon):
    def __init__(self, lista_pokemons):
        super().__init__(lista_pokemons, "static/imagens/charmander.png")
        # self.image = pygame.transform.scale(self.image, (50, 50))
        # self.rect = self.image.get_rect()
        self._posicionar()
        self.velocidade = random.randint(1, 4)
        self.nome = "Charmander"  

    def mover(self):
        "Movimento diagonal"
        self.rect.x += self.velocidade
        self.rect.y += self.velocidade
        if self.rect.right > 800 or self.rect.top < 0:
            self.velocidade = -self.velocidade
        elif self.rect.left < 0 or self.rect.bottom > 600:
            self.velocidade = -self.velocidade
