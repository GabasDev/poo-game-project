#include <iostream>
#include <vector>

class Pokemon {
public:
    Pokemon(std::vector<Pokemon*>& listaPokemons)
        : listaPokemons(listaPokemons), tempoLimite(5000), tempoInicio(0) {
        posicionar();
    }

    virtual ~Pokemon() {
        // Destrói o Pokémon
    }

    virtual void mover() {
        // Método a ser sobrescrito por subclasses
    }

    void verificarTempo() {
        // Simulação de tempo para o exemplo
        unsigned long tempoAtual = 0; // Aqui você pode implementar a lógica de tempo atual
        if (tempoAtual - tempoInicio > tempoLimite) {
            kill();
        }
    }

protected:
    struct Rect {
        int x, y, w, h; // Posição e dimensões
    } rect;

    std::vector<Pokemon*>& listaPokemons;
    unsigned long tempoInicio;
    const unsigned long tempoLimite;

private:
    void posicionar() {
        // Lógica de posicionamento
        rect.x = rand() % (800 - rect.w);
        rect.y = rand() % (300 - rect.h); // Metade superior da tela
    }

    void kill() {
        std::cout << "Pokémon removido após exceder o tempo limite!" << std::endl;
    }
};
