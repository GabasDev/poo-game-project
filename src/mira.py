import pygame

class Mira:
    def __init__(self, imagem_path):
        self.mira = pygame.image.load(imagem_path)
        self.mira = pygame.transform.scale(self.mira, (32, 32))
        self.mira_rect = self.mira.get_rect()
        pygame.mouse.set_visible(False)

    def desenhar(self, tela):
        mouse_pos = pygame.mouse.get_pos()
        self.mira_rect.center = mouse_pos
        tela.blit(self.mira, self.mira_rect)