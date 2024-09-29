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
        x = (x_1 * F.imagem(x_2) - x_2 * F.imagem(x_1)) / (F.imagem(x_2) - F.imagem(x_1));

        x_1 = x_2;
        x_2 = x;
        f_de_x = F.imagem(x);

        
        std::cout << x << '\t' << f_de_x << std::endl;


    }while(std::abs(f_de_x) > tolerancia && iteracoesMAX > i++);

    return x;
}
