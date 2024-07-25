import pygame

class Jogador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.imagem_segura = pygame.image.load('static/imagens/mao_segura.png').convert_alpha()
        self.imagem_arremessando = pygame.image.load('static/imagens/arremesar.png').convert_alpha()

        self.imagem_segura = pygame.transform.scale(self.imagem_segura, (50, 50)) 
        self.imagem_arremessando = pygame.transform.scale(self.imagem_arremessando, (50, 50))  

        self.image = self.imagem_segura
        self.rect = self.image.get_rect(center=(400, 570))  # Inicializando a posição diretamente
        self.estado = 'segurando'

        self.tempo_inicio = None

    def atualizar(self, teclas):
        """Atualiza a posição do jogador com base nas teclas pressionadas."""
        self._mover(teclas)
        self._limitar_movimento()

    def _mover(self, teclas):
        """Move o jogador baseado nas teclas pressionadas."""
        if teclas[pygame.K_LEFT]:
            self.rect.x -= 5
        if teclas[pygame.K_RIGHT]:
            self.rect.x += 5

    def _limitar_movimento(self):
        """Garante que o jogador permaneça dentro dos limites da tela."""
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > 800 - self.rect.width:
            self.rect.x = 800 - self.rect.width

    def arremessar(self):
        """Muda a imagem para 'arremessando'."""
        self.estado = 'arremessando'
        self.image = self.imagem_arremessando

    def voltar_a_segurar(self):
        """Muda a imagem para 'segurando'."""
        self.estado = 'segurando'
        self.image = self.imagem_segura

    def _calcular_forca(self, tempo_pressao):
        """Calcula a força do arremesso baseado no tempo de pressão."""
        return min(tempo_pressao * 10, 100)  # Força máxima de 100
