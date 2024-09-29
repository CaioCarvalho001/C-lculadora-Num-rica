#include "../include/NewtonRaphson.h"

NewtonRaphson::NewtonRaphson(double e, int n){
    tolerancia = e;
    iteracoesMAX = n;
}

double NewtonRaphson::calcular(double x, Funcao F) const{
    int i = 0;
    double f_de_x;

    do{
        x = x - (F.imagem(x) / F.derivada(x));
        f_de_x = F.imagem(x);

        
        std::cout << x << '\t' << f_de_x << std::endl;

    }while(std::abs(f_de_x) > tolerancia && iteracoesMAX > i++);

    return x;
}

