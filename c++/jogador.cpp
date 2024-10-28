#include <SDL.h>
#include <SDL_image.h>
#include <iostream>

class Jogador {
public:
    Jogador() {
        // Inicializa o jogador (carregar imagem, etc.)
        imagemSegura = IMG_Load("static/imagens/mao_segura.png");
        imagemArremessando = IMG_Load("static/imagens/arremesar.png");
        estado = "segurando";
        // Configuração inicial da posição
        rect.x = 400;
        rect.y = 570;
        rect.w = 50; // largura da imagem
        rect.h = 50; // altura da imagem
    }

    void atualizar(const Uint8* teclas) {
        mover(teclas);
        limitarMovimento();
    }

    void arremessar() {
        estado = "arremessando";
        // Aqui você deveria mudar a imagem para "arremessando"
        std::cout << "Arremessando!" << std::endl;
    }

    void voltarASegurar() {
        estado = "segurando";
        // Aqui você deveria mudar a imagem para "segurando"
        std::cout << "Voltando a segurar!" << std::endl;
    }

    void mover(const Uint8* teclas) {
        if (teclas[SDL_SCANCODE_LEFT]) {
            rect.x -= 5;
        }
        if (teclas[SDL_SCANCODE_RIGHT]) {
            rect.x += 5;
        }
    }

    void limitarMovimento() {
        if (rect.x < 0) rect.x = 0;
        if (rect.x > 800 - rect.w) rect.x = 800 - rect.w;
    }

private:
    SDL_Rect rect;
    SDL_Surface* imagemSegura;
    SDL_Surface* imagemArremessando;
    std::string estado;
};
