#include <iostream>
#include <string>
#include <ginac/ginac.h>
#include "../include/Funcao.h"
#include "../include/Bisseccao.h"
#include "../include/FalsaPosicao.h"
#include "../include/NewtonRaphson.h"
#include "../include/Secante.h"


int main(int argc, char *argv[]){
    if (argc > 1) {

        int op = atoi(argv[1]);
        std::string func = argv[2];
        Funcao F(func);

        double e = std::stod(argv[3]);
        int n = atoi(argv[4]);
        
        
        switch (op)
        {
        case 1: //Bisseccao
            {
                double a = std::stod(argv[5]);
                double b = std::stod(argv[6]);

                Bisseccao B(e, n);

                B.calcular(a, b, F);
                
            }
            break;
        case 2: //FalsaPosicao
            {
                double a = std::stod(argv[5]);
                double b = std::stod(argv[6]);

                FalsaPosicao FP (e, n);
                FP.calcular(a, b, F);
            }
            break;
        case 3: //Newton-Raphson
            {
                double x = std::stod(argv[5]);
                
                NewtonRaphson NR (e, n);
                NR.calcular(x, F);
            }
            break;
        case 4:
            {
                double x_1 = std::stod(argv[5]);
                double x_2 = std::stod(argv[6]);

                Secante S (e, n);
                S.calcular(x_1, x_2, F);
            }
            break;
        
        default:
            printf("\nERRO C++ script\n");
            break;
        }
    } else 
        printf("\nERRO C++ script\n");
    
    return 0;
}