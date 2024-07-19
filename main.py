import pygame
from src.jogo import Jogo

def principal():
    pygame.init()
    pygame.mixer.init()  

    pygame.mixer.music.load('static/sons/musica_fundo.mp3')
    pygame.mixer.music.play(-1) 
    clock = pygame.time.Clock()
    jogo = Jogo()

    terminado = False
    while not terminado:
        terminado = jogo.processar_eventos()
        jogo.executar_logica()
        jogo.mostrar_frame(jogo.tela)
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    principal()
