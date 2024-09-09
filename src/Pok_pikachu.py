from .pokemon import Pokemon
import pygame
import random

class Pikachu(Pokemon):  
    def __init__(self, lista_pokemons):
        super().__init__(lista_pokemons, "static/imagens/pikachu.png")
        # self.image = pygame.transform.scale(self.image, (50, 50))
        # self.rect = self.image.get_rect()
        self._posicionar()
        "Velocidade aleatória horizontal"
        self.velocidade_x = random.randint(1, 3)
        "Velocidade aleatória vertical"
        self.velocidade_y = random.randint(1, 3)
        
    def mover(self):
        ' Movimento horizontal'
        self.rect.x += self.velocidade_x
        if self.rect.right > 800 or self.rect.left < 0:
            self.velocidade_x = -self.velocidade_x
            
        'Movimento vertical'
        self.rect.y += self.velocidade_y
        if self.rect.bottom > 600 or self.rect.top < 0:
            self.velocidade_y = -self.velocidade_y