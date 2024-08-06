import pygame

class MedidorDeForca:
    def __init__(self):
        self.arremesso_ativo = False
        self.tempo_arremesso_inicio = None

    def iniciar_arremesso(self):
        self.arremesso_ativo = True
        self.tempo_arremesso_inicio = pygame.time.get_ticks()

    def finalizar_arremesso(self):
        self.arremesso_ativo = False

    def calcular_forca(self):
        if self.arremesso_ativo:
            tempo_arremesso = (pygame.time.get_ticks() - self.tempo_arremesso_inicio) / 1000.0
            return min(tempo_arremesso * 20, 100)
        return 0

    def desenhar(self, tela):
        forca = self.calcular_forca()
        largura_maxima = 200
        altura = 20
        largura = (forca / 100) * largura_maxima
        pygame.draw.rect(tela, (255, 255, 255), (300, 500, largura_maxima, altura), 2)
        pygame.draw.rect(tela, (255, 255, 255), (300, 500, largura, altura))