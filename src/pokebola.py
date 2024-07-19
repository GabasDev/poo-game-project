import pygame

class Pokebola(pygame.sprite.Sprite):
    def __init__(self, x, y, dx, dy):
        super().__init__()
        imagem_original = pygame.image.load('static/imagens/pokebola.png').convert_alpha()
        
        largura_nova = 20  
        altura_nova = 20   
        
        self.image = pygame.transform.scale(imagem_original, (largura_nova, altura_nova))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.dx = dx
        self.dy = dy

    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy
