#include <iostream>
#include <ginac/ginac.h>
#include "../include/Funcao.h"

#ifndef FALSAPOSICAO_H
#define FALSAPOSICAO_H

class FalsaPosicao
{
private:
    double tolerancia;
    int iteracoesMAX;
public:
    FalsaPosicao(double e, int n);
    double calcular(double a, double b, Funcao F) const;
    double media(double a, double b, Funcao F) const;

};

#endif