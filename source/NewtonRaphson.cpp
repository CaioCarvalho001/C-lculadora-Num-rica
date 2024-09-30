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

        printf("%d\t %.5lf\t %.5lf \t%.5lf\n", i, x, f_de_x, std::abs(f_de_x) - tolerancia);

    }while(std::abs(f_de_x) > tolerancia && iteracoesMAX > i++);

    return x;
}

