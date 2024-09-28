#include <iostream>
#include <ginac/ginac.h>
#include <cmath> 
#include "../include/Funcao.h"
#include "../include/Bisseccao.h"

Bisseccao::Bisseccao(double e, int n)
{
    tolerancia = e;
    iteracoesMAX = n;
}

double Bisseccao::media(double a, double b, Funcao F) const{
    return (a + b) / 2;
}

double Bisseccao::calcular(double a, double b, Funcao F) const{
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



