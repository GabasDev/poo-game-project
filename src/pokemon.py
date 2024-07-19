import pygame
import random

class Pokemon(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill((255, 0, 0))  # Vermelho
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 800 - 20)
        self.rect.y = random.randint(0, 600 // 2 - 20)

    def mover(self):
        self.rect.x = random.randint(0, 800 - 20)
        self.rect.y = random.randint(0, 600 // 2 - 20)