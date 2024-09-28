#include "../include/FalsaPosicao.h"

FalsaPosicao::FalsaPosicao(double e, int n)
{
    tolerancia = e;
    iteracoesMAX = n;
}

double FalsaPosicao::media(double a, double b, Funcao F) const{
    double f_de_a = F.imagem(a);
    double f_de_b = F.imagem(b);
    
    return ((a * f_de_b) - (b * f_de_a)) / (f_de_b - f_de_a);
}

double FalsaPosicao::calcular(double a, double b, Funcao F) const{
    int i = 0;
    double x;
    double f_de_x;
    
    do{
        x = media(a, b, F);
        
        //x = (a + b) / 2;
        f_de_x = F.imagem(x);
        
        printf("x_ = %.4lf\t| f(x_) = %.4lf\t|\n", x, f_de_x);

        if((f_de_x * F.imagem(a)) > 0){
            a = x;
        } else {
            b = x;
        }

    }while(std::abs(f_de_x) > tolerancia && iteracoesMAX > i++);

    return x;
}


