#include <iostream>
#include <string>
#include <ginac/ginac.h>
#include "../include/Funcao.h"
#include "../include/Bisseccao.h"
#include "../include/FalsaPosicao.h"
#include "../include/NewtonRaphson.h"
#include "../include/Secante.h"


int main(void){
    char op;
    printf("Bem vindo a Calculadora Numérica, escolha uma das opções abaixo.\n");

    do{
        
        printf("a) Método da Bissecção\n");
        printf("b) Método da Falsa Posição\n");
        printf("c) Método de Newton-Raphson\n");
        printf("d) Método da Secante\n");
        printf("Digte qualquer outra tecla para sair: ");

       
        scanf(" %c%*c", &op);
        
        switch (op)
        {
        case 'a':
            {
                double a, b, e;
                int n;
                std::string func;
                
                printf("Insira a função: ");
                std::getline(std::cin, func);
                Funcao F(func);

                printf("\nInsira o intervalo: ");
                scanf("%lf %lf", &a, &b);

                printf("Insira a tolerância: ");
                scanf("%lf", &e);

                printf("Insira o número máximo de interações: ");
                scanf("%d", &n);

                Bisseccao B(e, n);
                B.calcular(a, b, F);

            }
            
            break;

        case 'b':
            {
                double a, b, e;
                int n;
                std::string func;
                
                printf("Insira a função: ");
                std::getline(std::cin, func);
                Funcao F(func);

                printf("\nInsira o intervalo: ");
                scanf("%lf %lf", &a, &b);

                printf("Insira a tolerância: ");
                scanf("%lf", &e);

                printf("Insira o número máximo de interações: ");
                scanf("%d", &n);

                FalsaPosicao FP(e, n);
                FP.calcular(a, b, F);
            }
            break;

        case 'c':
            {
                double x, e;
                int n;
                std::string func;
                
                printf("Insira a função: ");
                std::getline(std::cin, func);
                Funcao F(func);

                printf("\nInsira uma estimativa da raiz: ");
                scanf("%lf", &x);

                printf("Insira a tolerância: ");
                scanf("%lf", &e);

                printf("Insira o número máximo de interações: ");
                scanf("%d", &n);

                NewtonRaphson NR(e, n);
                NR.calcular(x, F);
            }
            break;

        case 'd':
            {
                double x1, x2, e;
                int n;
                std::string func;
                
                printf("Insira a função: ");
                std::getline(std::cin, func);
                Funcao F(func);

                printf("\nInsira dois pontos: ");
                scanf("%lf %lf", &x1, &x2);

                printf("Insira a tolerância: ");
                scanf("%lf", &e);

                printf("Insira o número máximo de interações: ");
                scanf("%d", &n);

                Secante S(e, n);
                S.calcular(x1, x2, F);
            }
            break;
        
        default:
            break;
        }

        puts("\n");

    } while(op == 'a' || op == 'b' || op == 'c' || op == 'd');
    



    return 0;
}