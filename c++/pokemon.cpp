#include <SDL.h>
#include <SDL_image.h>
#include <vector>
#include <iostream>
#include <utility>

class Pokemon {
public:
    Pokemon(std::vector<Pokemon*>& listaPokemons, const std::string& caminhoImagem) 
        : listaPokemons(listaPokemons) {
        imagem = IMG_Load(caminhoImagem.c_str());
        if (imagem == nullptr) {
            std::cerr << "Erro ao carregar imagem: " << caminhoImagem << std::endl;
        }
        posicionar();
    }

    virtual ~Pokemon() {
        SDL_FreeSurface(imagem);
    }

    virtual void mover() {
        // Método a ser sobrescrito por subclasses
    }

    void verificarTempo() {
        if (SDL_GetTicks() - tempoInicio > tempoLimite) {
            kill();
        }
    }

protected:
    SDL_Surface* imagem;
    SDL_Rect rect;
    std::vector<Pokemon*>& listaPokemons;
    Uint32 tempoInicio = SDL_GetTicks();
    const Uint32 tempoLimite = 5000; // 5 segundos

private:
    void posicionar() {
        rect.x = posicaoAleatoria().first;
        rect.y = posicaoAleatoria().second;

        while (verificarColisao()) {
            rect.x = posicaoAleatoria().first;
            rect.y = posicaoAleatoria().second;
        }
    }

    std::pair<int, int> posicaoAleatoria() {
        int x = rand() % (800 - rect.w);
        int y = rand() % (300 - rect.h); // Metade superior da tela
        return std::make_pair(x, y);
    }

    bool verificarColisao() {
        for (const auto& pokemon : listaPokemons) {
            if (pokemon != this && SDL_HasIntersection(&rect, &pokemon->rect)) {
                return true;
            }
        }
        return false;
    }

    void kill() {
        std::cout << "Pokémon removido após exceder o tempo limite!" << std::endl;
        // Lógica para remover Pokémon
    }
};
