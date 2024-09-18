import pygame

class Pokebola(pygame.sprite.Sprite):
    def __init__(self, x, y, dx, dy, chance, jogo):
        super().__init__()
        self.image = pygame.image.load('static/imagens/pokebola.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect(center=(x, y))
        self.dx = dx
        self.dy = dy
        self.chance = chance
        self.jogo = jogo
        self.tempo_inicio = pygame.time.get_ticks()
        self.tempo_limite = 1000

    def capturar_pokemon(self, pokemon):
        self.jogo.pontuacao += 0
        
    def update(self):
        "Atualiza a posição e verifica condições de término."
        self._atualizar_posicao()
        if self._verificar_saida_tela() or self._verificar_tempo_limite():
            self._lidar_com_fim_de_jogo()

    def _atualizar_posicao(self):
        "Atualiza a posição com base na velocidade."
        self.rect.x += self.dx
        self.rect.y += self.dy

    def _verificar_saida_tela(self):
        "Verifica se saiu da tela."
        return (self.rect.x > 800 or self.rect.x < 0 or
                self.rect.y > 600 or self.rect.y < 0)

    def _verificar_tempo_limite(self):
        "Verifica se o tempo limite foi alcançado."
        return pygame.time.get_ticks() - self.tempo_inicio > self.tempo_limite

    def _lidar_com_fim_de_jogo(self):
        "Perde a chance e remove a Pokébola do grupo."
        self.chance._perdeu_chance()
        self.kill()
        self.jogo.pokebola_em_movimento = False