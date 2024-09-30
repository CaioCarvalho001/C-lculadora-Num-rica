#include "../include/NewtonRaphson.h"

NewtonRaphson::NewtonRaphson(double e, int n){
    tolerancia = e;
    iteracoesMAX = n;
}

double NewtonRaphson::calcular(double x, Funcao F) const{
    int i = 0;
    double f_de_x;

    do{
        
        f_de_x = F.imagem(x);

        printf("%d\t %.7lf\t %.7lf \t%.7lf\n", i, x, f_de_x, std::abs(f_de_x) - tolerancia);

        x = x - (F.imagem(x) / F.derivada(x));

    }while(std::abs(f_de_x) > tolerancia && iteracoesMAX > i++);

    return x;
}

