#include <iostream>

class Pokebola {
public:
    Pokebola(int x, int y, int dx, int dy)
        : dx(dx), dy(dy), tempoLimite(1000), tempoInicio(0) {
        rect.x = x;
        rect.y = y;
        rect.w = 30; // largura da Pokébola
        rect.h = 30; // altura da Pokébola
    }

    void update() {
        atualizarPosicao();
        if (verificarSaidaTela() || verificarTempoLimite()) {
            lidarComFimDeJogo();
        }
    }

private:
    struct Rect {
        int x, y, w, h; // Posição e dimensões
    } rect;

    int dx, dy;
    unsigned long tempoInicio;
    const unsigned long tempoLimite;

    void atualizarPosicao() {
        rect.x += dx;
        rect.y += dy;
    }

    bool verificarSaidaTela() {
        return (rect.x > 800 || rect.x < 0 || rect.y > 600 || rect.y < 0);
    }

    bool verificarTempoLimite() {
        // Simulação de tempo para o exemplo
        unsigned long tempoAtual = 0; // Aqui você pode implementar a lógica de tempo atual
        return (tempoAtual - tempoInicio > tempoLimite);
    }

    void lidarComFimDeJogo() {
        std::cout << "Fim de jogo! Pokébola saiu da tela ou excedeu o tempo." << std::endl;
    }
};
