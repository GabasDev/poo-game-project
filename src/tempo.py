import pygame

class Tempo:
    def __init__(self, tempoMaximo):
        self.tempoMaximo = tempoMaximo
        self.tempo_inicial = pygame.time.get_ticks()
        self.tempo_restante = self.tempoMaximo * 1000

    def atualizar_tempo_restante(self):
        "Atualiza o tempo restante do jogo."
        tempo_atual = pygame.time.get_ticks()
        self.tempo_restante = max(0, self.tempoMaximo * 1000 - (tempo_atual - self.tempo_inicial))

    def get_tempo_restante(self):
        return self.tempo_restante

    def formatar_tempo(self):
        minutos = self.tempo_restante // 60000
        segundos = (self.tempo_restante % 60000) // 1000
        return f"Tempo: {minutos:02}:{segundos:02}"