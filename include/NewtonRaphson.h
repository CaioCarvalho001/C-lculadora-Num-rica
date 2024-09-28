#include <ginac/ginac.h>
#include "../include/Funcao.h"

#ifndef NEWTONRAPHSON_H
#define NEWTONRAPHSON_H

class NewtonRaphson
{
private:
    double tolerancia;
    int iteracoesMAX;
public:
    NewtonRaphson(double e, int n);
    double calcular(double x, Funcao F) const;
};

#endif