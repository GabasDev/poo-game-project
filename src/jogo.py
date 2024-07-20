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
        pygame.init()
        pygame.mixer.init() 
        
        self.tela = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Capturador de Pokémon")
        self.mapa = Mapa()
        self.jogador = Jogador()
        self.pokemons = pygame.sprite.Group()
        self.pokebolas = pygame.sprite.Group()
        self.todos_sprites = pygame.sprite.Group()
        self.todos_sprites.add(self.jogador)
        self.pontuacao = 0
        self.fonte = pygame.font.SysFont('Arial', 30, bold=True)  
        self.max_pokemons = 20
        self.chances = 3
        self.jogo_ativo = True
        self.pokemons_visiveis = []  
        self.adicionar_pokemon(1)
        
        try:
            self.som_captura = pygame.mixer.Sound('static/sons/song.mp3')
        except pygame.error as e:
            print(f"Erro ao carregar o som: {e}")

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

                self.jogador.arremessar() 
                
                pokebola = Pokebola(self.jogador.rect.x, self.jogador.rect.y, dx, dy)
                self.pokebolas.add(pokebola)
                self.todos_sprites.add(pokebola)
                
                pygame.time.set_timer(pygame.USEREVENT + 1, 300)  

            if evento.type == pygame.USEREVENT + 1:
                self.jogador.voltar_a_segurar() 
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
                    if hasattr(self, 'som_captura'):
                        self.som_captura.play()  
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

    def renderizar_texto(self, texto, cor, sombra_cor, pos_x, pos_y):
        sombra_texto = self.fonte.render(texto, True, sombra_cor)
        self.tela.blit(sombra_texto, (pos_x + 2, pos_y + 2))
        texto_final = self.fonte.render(texto, True, cor)
        self.tela.blit(texto_final, (pos_x, pos_y))

    def mostrar_frame(self, tela):
        self.mapa.desenhar(tela)
        self.todos_sprites.draw(tela)

        self.renderizar_texto("Pontuação: " + str(self.pontuacao), WHITE, BLACK, 10, 10)
        
        self.renderizar_texto("Chances: " + str(self.chances), WHITE, BLACK, 10, 40)

        if not self.jogo_ativo:
            if self.pontuacao >= self.max_pokemons:
                mensagem = "Parabéns! Você capturou todos os Pokémon!"
            else:
                mensagem = "Game Over! Você ficou sem chances."

            self.renderizar_texto(mensagem, WHITE, BLACK, 400 - self.fonte.size(mensagem)[0] // 2, 300 - self.fonte.size(mensagem)[1] // 2)

            mensagem_reiniciar = "Pressione R para tentar novamente ou Q para sair."
            self.renderizar_texto(mensagem_reiniciar, WHITE, BLACK, 400 - self.fonte.size(mensagem_reiniciar)[0] // 2, 350 - self.fonte.size(mensagem_reiniciar)[1] // 2)

        pygame.display.flip()
