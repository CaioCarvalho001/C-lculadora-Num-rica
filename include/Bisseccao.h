#include <ginac/ginac.h>
#include "../include/Funcao.h"

#ifndef BISSECCAO_H
#define BISSECCAO_H

class Bisseccao
{
private:
    double tolerancia;
    int iteracoesMAX;
public:
    Bisseccao(double e, int n);
    double calcular(double a, double b, Funcao F) const;
    double media(double a, double b, Funcao F) const;
    
};

#endif