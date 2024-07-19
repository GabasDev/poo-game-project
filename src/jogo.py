import pygame
from src.jogador import Jogador
from src.mapa import Mapa
from src.pokemon import Pokemon
from src.pokebola import Pokebola
import random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Jogo:
    def __init__(self):
        self.tela = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Capturador de Pokémon")
        self.mapa = Mapa()
        self.jogador = Jogador()
        self.pokemons = pygame.sprite.Group()
        self.pokebolas = pygame.sprite.Group()
        self.todos_sprites = pygame.sprite.Group()
        self.todos_sprites.add(self.jogador)
        self.pontuacao = 0
        self.fonte = pygame.font.SysFont('Arial', 25)
        self.max_pokemons = 20
        self.chances = 3
        self.jogo_ativo = True
        self.pokemons_visiveis = []  
        self.adicionar_pokemon(1)

    def adicionar_pokemon(self, quantidade):
        if len(self.pokemons) < self.max_pokemons:
            for _ in range(quantidade):
                if len(self.pokemons) < self.max_pokemons:
                    novo_pokemon = Pokemon()
                    self.pokemons.add(novo_pokemon)
                    self.todos_sprites.add(novo_pokemon)
                    self.pokemons_visiveis.append(novo_pokemon)

    def processar_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return True
            if self.jogo_ativo and evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                dx = mouse_x - self.jogador.rect.x
                dy = mouse_y - self.jogador.rect.y
                distancia = (dx ** 2 + dy ** 2) ** 0.5
                dx /= distancia
                dy /= distancia
                dx *= 10
                dy *= 10

                pokebola = Pokebola(self.jogador.rect.x, self.jogador.rect.y, dx, dy)
                self.pokebolas.add(pokebola)
                self.todos_sprites.add(pokebola)
                
            if not self.jogo_ativo and evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_r:  
                    self.__init__()
                elif evento.key == pygame.K_q: 
                    return True
        return False

    def executar_logica(self):
        if self.jogo_ativo:
            teclas = pygame.key.get_pressed()
            self.jogador.atualizar(teclas)

            self.pokebolas.update()

            for pokebola in self.pokebolas:
                pokemons_atingidos = pygame.sprite.spritecollide(pokebola, self.pokemons, True)
                if pokemons_atingidos:
                    self.pontuacao += 1
                    if len(self.pokemons) == 0:
                        self.adicionar_pokemon(2)
                    pokebola.kill()
                else:
                    if pokebola.rect.x > 800 or pokebola.rect.x < 0 or pokebola.rect.y > 600 or pokebola.rect.y < 0:
                        self.chances -= 1
                        pokebola.kill()

            if self.chances == 0:
                self.jogo_ativo = False

            if self.pontuacao >= self.max_pokemons:
                self.jogo_ativo = False

    def mostrar_frame(self, tela):
        self.mapa.desenhar(tela)
        self.todos_sprites.draw(tela)
        texto_pontuacao = self.fonte.render("Pontuação: " + str(self.pontuacao), True, BLACK)
        texto_chances = self.fonte.render("Chances: " + str(self.chances), True, BLACK)
        tela.blit(texto_pontuacao, [10, 10])
        tela.blit(texto_chances, [10, 40])

        if not self.jogo_ativo:
            if self.pontuacao >= self.max_pokemons:
                mensagem = "Parabéns! Você capturou todos os Pokémon!"
            else:
                mensagem = "Game Over! Você ficou sem chances."
            texto_final = self.fonte.render(mensagem, True, BLACK)
            tela.blit(texto_final, [400 - texto_final.get_width() // 2, 300 - texto_final.get_height() // 2])

            mensagem_reiniciar = self.fonte.render("Pressione R para tentar novamente ou Q para sair.", True, BLACK)
            tela.blit(mensagem_reiniciar, [400 - mensagem_reiniciar.get_width() // 2, 350 - mensagem_reiniciar.get_height() // 2])

        pygame.display.flip()
