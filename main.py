import pygame
from src.jogo import Jogo

def principal():
    pygame.init()
    pygame.mixer.init()  

    # Carregar e tocar a música de fundo
    try:
        pygame.mixer.music.load('static/sons/musica_fundo.mp3')
        pygame.mixer.music.play(-1)  # -1 para tocar em loop
    except pygame.error as e:
        print(f"Erro ao carregar a música de fundo: {e}")

    clock = pygame.time.Clock()
    jogo = Jogo()

    terminado = False
    while not terminado:
        terminado = jogo.processar_eventos()
        jogo.executar_logica()
        jogo.mostrar_frame()  # Corrigido para não passar argumentos
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    principal()
