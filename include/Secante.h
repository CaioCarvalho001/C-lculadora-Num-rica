#include <ginac/ginac.h>
#include "../include/Funcao.h"


#ifndef SECANTE_H
#define SECANTE_H

class Secante
{
private:
    double tolerancia;
    int iteracoesMAX;
public:
    Secante(double e, int n);
    double calcular(double a, double b, Funcao F) const;
};

#endif