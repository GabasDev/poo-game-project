import pygame
from src.jogador import Jogador
from src.mapa import Mapa
from src.pokemon import Pokemon
from src.pokebola import Pokebola
from src.chances import Chance
from src.tempo import Tempo
from src.mira import Mira
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
        self.tempo = Tempo(60)
        self.mira = Mira('static/imagens/mira.png')
        self.chance = Chance()
        self.jogo_ativo = True
        self.adicionar_pokemon(2)
       
        try:
            self.som_captura = pygame.mixer.Sound('static/sons/song.mp3')
        except pygame.error as e:
            print(f"Erro ao carregar o som: {e}")

        self.arremesso_ativo = False
        self.tempo_arremesso_inicio = None
        self.pokebola_em_movimento = False  
        self.delay_arremesso = 2000  
        self.ultimo_arremesso = pygame.time.get_ticks()  

        "Carregar a imagem da mira e redimensionar"
        self.crosshair = pygame.image.load('static/imagens/mira.png')
        self.crosshair = pygame.transform.scale(self.crosshair, (32, 32))
        self.crosshair_rect = self.crosshair.get_rect()

        "Ocultar o cursor padrão"
        pygame.mouse.set_visible(False)

    def adicionar_pokemon(self, quantidade):
        for _ in range(quantidade):
            novo_pokemon = Pokemon(self.pokemons)
            self.pokemons.add(novo_pokemon)
            self.todos_sprites.add(novo_pokemon)

    def processar_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return True

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE and not self.arremesso_ativo and not self.pokebola_em_movimento:
                    self.arremesso_ativo = True
                    self.tempo_arremesso_inicio = pygame.time.get_ticks()  

            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_SPACE and self.arremesso_ativo:
                    self._arremessar()
                   
            if evento.type == pygame.USEREVENT + 1:
                self.jogador.voltar_a_segurar()
               
            if not self.jogo_ativo:
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_r:
                        self.__init__()
                    elif evento.key == pygame.K_q:
                        return True
        return False

    def _arremessar(self):
        if self.pokebola_em_movimento:  
            return
       
        tempo_arremesso = (pygame.time.get_ticks() - self.tempo_arremesso_inicio) / 1000.0
        self.arremesso_ativo = False
        forca = min(tempo_arremesso * 10, 100)

        mouse_x, mouse_y = pygame.mouse.get_pos()
        dx, dy = mouse_x - self.jogador.rect.x, mouse_y - self.jogador.rect.y
        distancia = (dx ** 2 + dy ** 2) ** 0.5
        dx, dy = (dx / distancia) * forca, (dy / distancia) * forca

        self.jogador.arremessar()
        pokebola = Pokebola(self.jogador.rect.x, self.jogador.rect.y, dx, dy, self.chance, self)
        self.pokebolas.add(pokebola)
        self.todos_sprites.add(pokebola)
        pygame.time.set_timer(pygame.USEREVENT + 1, 300)

        self.pokebola_em_movimento = True
        "Atualiza o tempo do último arremesso"
        self.ultimo_arremesso = pygame.time.get_ticks()  

    def executar_logica(self):
        if self.jogo_ativo:
            teclas = pygame.key.get_pressed()
            self.jogador.atualizar(teclas)
            self.pokebolas.update()

            for pokebola in self.pokebolas:
                if pygame.sprite.spritecollide(pokebola, self.pokemons, True):
                    self.pontuacao += 1
                    if hasattr(self, 'som_captura'):
                        self.som_captura.play()  
                    self.adicionar_pokemon(1)
                    pokebola.kill()
                    "Permitir o lançamento de outra pokébola após a colisao"
                    self.pokebola_em_movimento = False  
                    print(f"Pokébola posição: ({pokebola.rect.x}, {pokebola.rect.y})")

            self.tempo.atualizar_tempo_restante()

            if self.tempo.get_tempo_restante() == 0 or self.chance._mostrar_chance() == 0 or self.pontuacao >= self.tempo.tempoMaximo:
                self.jogo_ativo = False

    def renderizar_texto(self, texto, cor, sombra_cor, pos_x, pos_y):
        sombra_texto = self.fonte.render(texto, True, sombra_cor)
        self.tela.blit(sombra_texto, (pos_x + 2, pos_y + 2))
        texto_final = self.fonte.render(texto, True, cor)
        self.tela.blit(texto_final, (pos_x, pos_y))

    def mostrar_frame(self):
        self.tela.fill(BLACK)  
        self.mapa.desenhar(self.tela)
        self.todos_sprites.draw(self.tela)

        self.renderizar_texto("Pokémon: " + str(self.pontuacao), WHITE, BLACK, 10, 500)
        self.renderizar_texto("Pokebolas: " + str(self.chance._mostrar_chance()), WHITE, BLACK, 10, 540)

        tempo_texto = self.tempo.formatar_tempo()
        self.renderizar_texto(tempo_texto, WHITE, BLACK, 600, 540)

        if not self.jogo_ativo:
            mensagem = "Parabéns! Você capturou todos os Pokémon!" if self.pontuacao >= self.tempo.tempoMaximo else "Game Over! Você ficou sem chances."
            self.renderizar_texto(mensagem, WHITE, BLACK, 400 - self.fonte.size(mensagem)[0] // 2, 300 - self.fonte.size(mensagem)[1] // 2)

            mensagem_reiniciar = "Pressione R para tentar novamente ou Q para sair."
            self.renderizar_texto(mensagem_reiniciar, WHITE, BLACK, 400 - self.fonte.size(mensagem_reiniciar)[0] // 2, 350 - self.fonte.size(mensagem_reiniciar)[1] // 2)

        "Desenhar o medidor de força"
        if self.arremesso_ativo:
            tempo_arremesso = (pygame.time.get_ticks() - self.tempo_arremesso_inicio) / 1000.0
            forca = min(tempo_arremesso * 50, 100)
            self.desenhar_medidor_de_forca(forca)

        "Desenhar a mira"
        self.mira.desenhar(self.tela)
        
        pygame.display.flip()

    def desenhar_medidor_de_forca(self, forca):
        largura_maxima = 200
        altura = 20
        largura = (forca / 100) * largura_maxima
        pygame.draw.rect(self.tela, WHITE, (300, 500, largura_maxima, altura), 2)
        pygame.draw.rect(self.tela, WHITE, (300, 500, largura, altura))

