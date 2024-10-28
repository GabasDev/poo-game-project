#include <SDL.h>
#include <SDL_image.h>
#include <iostream>

class Pokebola {
public:
    Pokebola(int x, int y, int dx, int dy) {
        rect.x = x;
        rect.y = y;
        rect.w = 30; // largura da Pokébola
        rect.h = 30; // altura da Pokébola
        this->dx = dx;
        this->dy = dy;
        imagem = IMG_Load("static/imagens/pokebola.png");
        tempoInicio = SDL_GetTicks();
        tempoLimite = 1000; // 1 segundo
    }

    void update() {
        atualizarPosicao();
        if (verificarSaidaTela() || verificarTempoLimite()) {
            lidarComFimDeJogo();
        }
    }

private:
    SDL_Rect rect;
    SDL_Surface* imagem;
    int dx, dy;
    Uint32 tempoInicio;
    const Uint32 tempoLimite;

    void atualizarPosicao() {
        rect.x += dx;
        rect.y += dy;
    }

    bool verificarSaidaTela() {
        return (rect.x > 800 || rect.x < 0 || rect.y > 600 || rect.y < 0);
    }

    bool verificarTempoLimite() {
        return (SDL_GetTicks() - tempoInicio > tempoLimite);
    }

    void lidarComFimDeJogo() {
        std::cout << "Fim de jogo! Pokébola saiu da tela ou excedeu o tempo." << std::endl;
        // Aqui você deve lidar com a lógica de fim de jogo
    }
};
