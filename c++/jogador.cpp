#include <iostream>

class Jogador {
public:
    Jogador() {
        estado = "segurando";
        rect.x = 400;
        rect.y = 570;
        rect.w = 50; // largura
        rect.h = 50; // altura
    }

    void atualizar(bool esquerda, bool direita) {
        mover(esquerda, direita);
        limitarMovimento();
    }

    void arremessar() {
        estado = "arremessando";
        std::cout << "Arremessando!" << std::endl;
    }

    void voltarASegurar() {
        estado = "segurando";
        std::cout << "Voltando a segurar!" << std::endl;
    }

    void mostrarEstado() const {
        std::cout << "Estado: " << estado << " | Posição: (" << rect.x << ", " << rect.y << ")" << std::endl;
    }

private:
    struct Rect {
        int x, y, w, h; // Posição e dimensões
    } rect;

    std::string estado;

    void mover(bool esquerda, bool direita) {
        if (esquerda) {
            rect.x -= 5;
        }
        if (direita) {
            rect.x += 5;
        }
    }

    void limitarMovimento() {
        if (rect.x < 0) rect.x = 0;
        if (rect.x > 800 - rect.w) rect.x = 800 - rect.w; // Limite da tela
    }
};
