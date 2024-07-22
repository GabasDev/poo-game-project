import pygame
import random

class Pokemon(pygame.sprite.Sprite):
    def __init__(self, lista_pokemons):
        super().__init__()
        self.lista_pokemons = lista_pokemons
        pokemons = {
            "pikachu": './static/imagens/pikachu.png',
            "charmander": './static/imagens/charmander.png',
            "squirtle": './static/imagens/squirtle.png',
            "bulbasaur": './static/imagens/Bulbassauro.png'
        }
        random_pokemon = self._random_img_pokemon(pokemons)
        img_size = pygame.image.load(random_pokemon).convert_alpha()

        self.image = pygame.transform.scale(img_size, (50, 50))
        self.rect = self.image.get_rect()
        self._posicionar()

    def _posicionar(self):
        """Posiciona o Pokémon em uma posição aleatória, garantindo que não haja colisão com outros Pokémons."""
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

    def _random_img_pokemon(self, dicionario_pokemon):
        """Escolhe uma imagem de Pokémon aleatória a partir do dicionário fornecido."""
        return random.choice(list(dicionario_pokemon.values()))
