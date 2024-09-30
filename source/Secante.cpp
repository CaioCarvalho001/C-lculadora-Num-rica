#include "../include/Secante.h"


Secante::Secante(double e, int n)
{
    tolerancia = e;
    iteracoesMAX = n;
}

double Secante::calcular(double x_1, double x_2, Funcao F) const{
    int i = 0;
    double x, f_de_x;
    do{
        double f_de_x_1 = F.imagem(x_1);
        double f_de_x_2 = F.imagem(x_2);
        
        x = (x_1 * f_de_x_2 - x_2 * f_de_x_1) / (f_de_x_2 - f_de_x_1);
        f_de_x = F.imagem(x);


        printf("%d\t %.7lf\t %.7lf\t %.7lf\t %.7lf\t %.7lf\n", i, x_1, x_2, x, f_de_x, std::abs(f_de_x) - tolerancia);
        x_1 = x_2;
        x_2 = x;

    }while(std::abs(f_de_x) > tolerancia && iteracoesMAX > i++);

    return x;
}
