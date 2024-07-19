import pygame

class Jogador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill((0, 255, 0))  # Verde
        self.rect = self.image.get_rect()
        self.rect.center = (400, 570)  # Centralizado na parte inferior

    def atualizar(self, teclas):
        if teclas[pygame.K_LEFT]:
            self.rect.x -= 5
        if teclas[pygame.K_RIGHT]:
            self.rect.x += 5

        # Limita o movimento do jogador dentro da parte inferior da tela
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > 800 - self.rect.width:
            self.rect.x = 800 - self.rect.width
