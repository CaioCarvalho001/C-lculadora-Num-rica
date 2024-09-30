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
        
        f_de_x = F.imagem(x);
        
        printf("%d\t %.5lf\t %.5lf\t %.5lf\t %.5lf \t%.5lf\n", i, a, b, x, f_de_x, std::abs(f_de_x) - tolerancia);

        if((f_de_x * F.imagem(a)) > 0){
            a = x;
        } else {
            b = x;
        }

    }while(std::abs(f_de_x) > tolerancia && iteracoesMAX > i++);

    return x;
}


