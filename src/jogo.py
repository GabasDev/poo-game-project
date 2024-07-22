import pygame
from src.jogador import Jogador
from src.mapa import Mapa
from src.pokemon import Pokemon
from src.pokebola import Pokebola
from src.chances import Chance
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
        self.tempoMaximo = 60  # Tempo máximo em segundos
        self.tempo_inicial = pygame.time.get_ticks()  # Tempo inicial
        self.tempo_restante = self.tempoMaximo * 1000  # Tempo restante em milissegundos
        self.chance = Chance()
        self.jogo_ativo = True
        self.adicionar_pokemon(2)
        
        try:
            self.som_captura = pygame.mixer.Sound('static/sons/song.mp3')
        except pygame.error as e:
            print(f"Erro ao carregar o som: {e}")

        self.arremesso_ativo = False
        self.tempo_arremesso_inicio = None

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
                if evento.key == pygame.K_SPACE and not self.arremesso_ativo:
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
        tempo_arremesso = (pygame.time.get_ticks() - self.tempo_arremesso_inicio) / 1000.0
        self.arremesso_ativo = False
        forca = min(tempo_arremesso * 10, 100)

        mouse_x, mouse_y = pygame.mouse.get_pos()
        dx, dy = mouse_x - self.jogador.rect.x, mouse_y - self.jogador.rect.y
        distancia = (dx ** 2 + dy ** 2) ** 0.5
        dx, dy = (dx / distancia) * forca, (dy / distancia) * forca

        self.jogador.arremessar() 
        pokebola = Pokebola(self.jogador.rect.x, self.jogador.rect.y, dx, dy, self.chance)
        self.pokebolas.add(pokebola)
        self.todos_sprites.add(pokebola)
        pygame.time.set_timer(pygame.USEREVENT + 1, 300)

    def atualizar_tempo_restante(self):
        """Atualiza o tempo restante do jogo."""
        tempo_atual = pygame.time.get_ticks()
        self.tempo_restante = max(0, self.tempoMaximo * 1000 - (tempo_atual - self.tempo_inicial))

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
                    if len(self.pokemons) == 1:
                        self.tempoMaximo += 1
                        self.adicionar_pokemon(1)
                        pokebola.kill()
                        print(f"Pokébola posição: ({pokebola.rect.x}, {pokebola.rect.y})")

            self.atualizar_tempo_restante()

            if self.tempo_restante == 0 or self.chance._mostrar_chance() == 0 or self.pontuacao >= self.tempoMaximo:
                self.jogo_ativo = False

    def renderizar_texto(self, texto, cor, sombra_cor, pos_x, pos_y):
        sombra_texto = self.fonte.render(texto, True, sombra_cor)
        self.tela.blit(sombra_texto, (pos_x + 2, pos_y + 2))
        texto_final = self.fonte.render(texto, True, cor)
        self.tela.blit(texto_final, (pos_x, pos_y))

    def mostrar_frame(self):
        self.mapa.desenhar(self.tela)
        self.todos_sprites.draw(self.tela)

        self.renderizar_texto("Pokémon: " + str(self.pontuacao), WHITE, BLACK, 10, 500)
        self.renderizar_texto("Pokebolas: " + str(self.chance._mostrar_chance()), WHITE, BLACK, 10, 540)

        minutos = self.tempo_restante // 60000
        segundos = (self.tempo_restante % 60000) // 1000
        tempo_texto = f"Tempo: {minutos:02}:{segundos:02}"
        self.renderizar_texto(tempo_texto, WHITE, BLACK, 600, 540)

        if not self.jogo_ativo:
            mensagem = "Parabéns! Você capturou todos os Pokémon!" if self.pontuacao >= self.tempoMaximo else "Game Over! Você ficou sem chances."
            self.renderizar_texto(mensagem, WHITE, BLACK, 400 - self.fonte.size(mensagem)[0] // 2, 300 - self.fonte.size(mensagem)[1] // 2)

            mensagem_reiniciar = "Pressione R para tentar novamente ou Q para sair."
            self.renderizar_texto(mensagem_reiniciar, WHITE, BLACK, 400 - self.fonte.size(mensagem_reiniciar)[0] // 2, 350 - self.fonte.size(mensagem_reiniciar)[1] // 2)

        pygame.display.flip()
