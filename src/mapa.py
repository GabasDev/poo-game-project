import pygame

class Mapa:
    def __init__(self):
        # Inicializa a tela com o tamanho especificado
        self.largura_tela = 800
        self.altura_tela = 600
        
        # Carrega a imagem do fundo
        self.imagem_fundo = pygame.image.load('static/imagens/grass.png')
        self.imagem_fundo = pygame.transform.scale(self.imagem_fundo, (self.largura_tela, self.altura_tela))

    def desenhar(self, tela):
        # Desenha a imagem do fundo na tela
        tela.blit(self.imagem_fundo, (0, 0))