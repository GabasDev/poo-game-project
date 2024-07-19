import pygame

class Mapa:
    def __init__(self):
        self.image = pygame.Surface([800, 600])
        self.image.fill((255, 255, 255))  # Branco

    def desenhar(self, tela):
        tela.blit(self.image, (0, 0))
