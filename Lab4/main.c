#include <stdio.h>
#include <stdlib.h>
#include "graphics/graphic.h"
#include "lagrange/lagrange.h"
#include "newton/newton.h"

#define N 12
#define LAGRANGE_DOTS 3
#define NEWTON_DOTS 4

void readFile(double x[N], double y[N], char filepath[]) {
    FILE *file = fopen(filepath, "r");

    if (!file) {
        printf("File Error: Cannot find %s", filepath);
        exit(1);
    }

    for (int i = 0; i < N; i++){
        fscanf(file, "%lf %lf\n", &x[i], &y[i]);
        // printf("%lf %lf\n", x[i], y[i]);
    }
    fclose(file);
}

int main(void) {
    double x[N]; 
    double y_exp[N];

    double y_calc_Newton[N];

    readFile(x, y_exp, "cords.txt");

    experimentalDotsGraphic();
    printf("Experimental point graph created...\n");

    lagrangeDiagonalDiff(x, y_exp);
    printf("Create Diagonal Difference table for Lagrange...\n");

    double Lx[LAGRANGE_DOTS], Ly_exp[LAGRANGE_DOTS];
    readLagrangeDots(Lx, Ly_exp);
    chooseLagrangeDots(x, y_exp, 1, 6, 11);
    printf("Choosing Lagrange dots...\n");

    double Ly_calc[N];
    readFile(x, Ly_calc, "lagrange/lagrange_calc.txt");
    lagrangeMethod(x, Lx, Ly_exp);
    lagrangeGraphic(x, y_exp, Ly_calc);
    printf("Lagrange graphic created...\n");

    double Nx[NEWTON_DOTS], Ny_exp[NEWTON_DOTS];
    readNewtonDots(Nx, Ny_exp);
    chooseNewtonDots(x, y_exp, 1, 4, 6, 11);
    printf("Choosing Newton dots...\n");

    double Ny_calc[N];
    readFile(x, Ny_calc, "newton/newton_calc.txt");
    newtonDiagonalDiff(x, Nx, Ny_exp);

    newtonGraphic(x, y_exp, Ly_calc);
    printf("Newton graphic created...\n");
    return 0;
}