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
            return min(tempo_arremesso * 10, 100)
        return 0

    def desenhar(self, tela):
        largura_maxima = 200
        largura = 0
        forca = self.calcular_forca()
        largura = (forca / 20) * largura_maxima
        altura = 20
        if largura_maxima > largura:
            pygame.draw.rect(tela, (255, 255, 255), (300, 500, largura_maxima, altura), 2)
            pygame.draw.rect(tela, (255, 255, 255), (300, 500, largura, altura))
            
        else:
            pygame.draw.rect(tela, (255, 255, 255), (300, 500, largura_maxima, altura), 2)
            pygame.draw.rect(tela, (255, 255, 255), (300, 500, largura_maxima, altura))
        
        
        
        
        
        
        