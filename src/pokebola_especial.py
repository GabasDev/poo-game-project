import pygame
from .pokebola import Pokebola

class PokebolaEspecial(Pokebola):
    def __init__(self, x, y, dx, dy, chance, jogo):
        super().__init__(x, y, dx, dy, chance, jogo)
        self.image = pygame.image.load('static/imagens/pokebola_especial.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (30, 30))

    def capturar_pokemon(self, pokemon):
        """Método para capturar um Pokémon e atualizar a pontuação com o dobro"""
        if hasattr(pokemon, 'nome'):
            if pokemon.nome == "Ditto":
                self.jogo.pontuacao += pokemon.pontuacao * 2  
                self.jogo.tempo.decrementar(1)
            elif pokemon.nome == "Alakazam":
                self.jogo.pontuacao += pokemon.pontuacao * 2
                self.jogo.tempo.incrementar(5)
            else:
                self.jogo.pontuacao += pokemon.pontuacao*2
                self.jogo.tempo.incrementar(2)
                print(f"{self.jogo.pontuacao}") 

        if hasattr(self.jogo, 'som_captura'):
            self.jogo.som_captura.play() 

        self.kill()
        self.jogo.pokebola_em_movimento = False
