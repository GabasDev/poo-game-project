import pygame
import random
from pygame.locals import *

# Definindo as cores
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Classe Pokémon
class Pokemon(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 780)
        self.rect.y = random.randint(0, 280)

    def mover(self):
        self.rect.x = random.randint(0, 780)
        self.rect.y = random.randint(0, 280)

# Classe Pokébola
class Pokebola(pygame.sprite.Sprite):
    def __init__(self, x, y, dx, dy):
        super().__init__()
        self.image = pygame.Surface([10, 10])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.dx = dx
        self.dy = dy

    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

# Classe Jogador
class Jogador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (400, 570)

    def atualizar(self, teclas):
        if teclas[K_LEFT]:
            self.rect.x -= 5
        if teclas[K_RIGHT]:
            self.rect.x += 5

        # Limita o movimento do jogador dentro da parte inferior da tela
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > 780:
            self.rect.x = 780

# Classe Mapa
class Mapa:
    def __init__(self):
        self.image = pygame.Surface([800, 600])
        self.image.fill((255, 255, 255))

    def desenhar(self, tela):
        tela.blit(self.image, (0, 0))
