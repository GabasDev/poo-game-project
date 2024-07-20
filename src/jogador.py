import pygame

class Jogador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.imagem_segura = pygame.image.load('static/imagens/mao_segura.png').convert_alpha()
        self.imagem_arremessando = pygame.image.load('static/imagens/arremesar.png').convert_alpha()
        
        self.imagem_segura = pygame.transform.scale(self.imagem_segura, (50, 50)) 
        self.imagem_arremessando = pygame.transform.scale(self.imagem_arremessando, (50, 50))  
        
        self.image = self.imagem_segura
        self.rect = self.image.get_rect()
        self.rect.center = (400, 570)  
        self.estado = 'segurando'  

    def atualizar(self, teclas):
        if teclas[pygame.K_LEFT]:
            self.rect.x -= 5
        if teclas[pygame.K_RIGHT]:
            self.rect.x += 5

        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > 800 - self.rect.width:
            self.rect.x = 800 - self.rect.width

    def arremessar(self):
        self.estado = 'arremessando'
        self.image = self.imagem_arremessando

    def voltar_a_segurar(self):
        self.estado = 'segurando'
        self.image = self.imagem_segura
