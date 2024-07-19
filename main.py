import pygame
from src.jogo import Jogo

def principal():
    pygame.init()
    LARGURA_TELA = 800
    ALTURA_TELA = 600
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption("Captura de Pokémon")
    clock = pygame.time.Clock()
    jogo = Jogo()

    terminado = False
    while not terminado:
        terminado = jogo.processar_eventos()
        jogo.executar_logica()
        jogo.mostrar_frame(tela)
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    principal()
