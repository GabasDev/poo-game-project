#include <iostream>
#include <vector>
#include "Jogador.cpp"
#include "Pokebola.cpp"
#include "Pokemon.cpp"

int main() {
    Jogador jogador;
    std::vector<Pokemon*> listaPokemons;

    // Simulação de loop de jogo
    for (int i = 0; i < 10; ++i) {
        // Atualiza o jogador e mostra o estado
        jogador.atualizar(i % 2 == 0, i % 2 != 0);
        jogador.mostrarEstado();
    }

    // Simulando um arremesso
    jogador.arremessar();
    jogador.voltarASegurar();

    // Limpeza da memória (exemplo)
    for (auto& pokemon : listaPokemons) {
        delete pokemon; // Destrói os Pokémon
    }

    return 0;
}
