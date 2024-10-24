import pygame
import random

class Pokemon(pygame.sprite.Sprite):
    def __init__(self, lista_pokemons, caminho_image):
        super().__init__()
        self.lista_pokemons = lista_pokemons
        self.image = pygame.image.load(caminho_image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.tempo_inicio = pygame.time.get_ticks()  # Armazena o tempo de criação do Pokémon
        self.tempo_limite = 5000  # Limite de tempo em milissegundos (5 segundos)

        self._posicionar()

    def _posicionar(self):
        """Posiciona o Pokémon em uma posição aleatória, garantindo que não haja colisão com outros Pokémons."""
        if self.rect is not None:
            self.rect.topleft = self._posicao_aleatoria()
            while self._verificar_colisao():
                self.rect.topleft = self._posicao_aleatoria()

    def _posicao_aleatoria(self):
        """Gera uma posição aleatória para o Pokémon dentro da tela."""
        x = random.randint(0, 800 - self.rect.width)
        y = random.randint(0, 600 // 2 - self.rect.height)
        return x, y

    def _verificar_colisao(self):
        """Verifica se o Pokémon está colidindo com outros Pokémons."""
        return any(pokemon != self and self.rect.colliderect(pokemon.rect) for pokemon in self.lista_pokemons)

    def mover(self):
        """Método para ser sobrescrito pelas subclasses, definindo o movimento do Pokémon."""
        pass

    def verificar_tempo(self):
        """Verifica se o Pokémon ultrapassou o tempo limite e deve ser removido."""
        if pygame.time.get_ticks() - self.tempo_inicio > self.tempo_limite:
            self.kill()
