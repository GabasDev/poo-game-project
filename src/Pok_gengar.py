from .pokemon import Pokemon
import pygame
import random

class Gengar(Pokemon):
    def __init__(self, lista_pokemons):
        super().__init__(lista_pokemons, "static/imagens/Gengar.png")
        # self.image = pygame.transform.scale(self.image, (50, 50))
        # self.rect = self.image.get_rect()
        self._posicionar()
        self.velocidade = random.randint(1, 4)
        self.nome = "Gengar"
        self.tempo_teleporte = pygame.time.get_ticks()
        self.proximo_teleporte = random.randint(1000, 3000)
        
    def mover(self):
        """Teletransporta o Pokémon após um intervalo de tempo aleatório entre 1 e 3 segundos."""
        tempo = pygame.time.get_ticks()
        if tempo - self.tempo_teleporte > self.proximo_teleporte:
            self.teletransportar() 
            self.tempo_teleporte = tempo 
            self.proximo_teleporte = random.randint(1000, 3000)  

    def teletransportar(self):
        """Teletransporta o Gengar para uma nova posição aleatória."""
        self.rect.x = random.randint(0, 750)
        self.rect.y = random.randint(0, 550)
        print(f"Gengar se teletransportou para ({self.rect.x}, {self.rect.y})")