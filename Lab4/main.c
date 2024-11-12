#include <stdio.h>
#include <stdlib.h>
#include "src/graphic.h"
#include "src/polynomial.h"
#include "src/methods.h"

#define N 12

void readFile(double x[N], double y_exp[N]) {
    FILE *file = fopen("cords.txt", "r");

    if (!file) {
        printf("File Error");
        exit(1);
    }

    for (int i = 0; i < N; i++){
        fscanf(file, "%lf %lf\n", &x[i], &y_exp[i]);
    }

    fclose(file);
}

void readLagrange(double y_calc[N]) {
    FILE *file = fopen("src/lagrange_y_calc.txt", "r");

    if (!file) {
        printf("File Error");
        exit(1);
    }
    
    for (int i = 0; i < N; i++){
        fscanf(file, "%lf\n", &y_calc[i]);
    }
    fclose(file);
}

int main(void) {
    double x[N]; 
    double y_exp[N];
    double y_calc[N];

    readFile(x, y_exp);

    experimentalDotsGraphic();
    printf("Experimental point graph created...\n");

    printf("Optimal polynomial degree: %d\n", lagrangeOptimalPolynomialDegree(x, y_exp));

    readLagrange(y_calc);
    chooseLagrangeDots(x, y_exp, 1, 6, 11);
    printf("Finding the obtained values for Lagrange method...\n");

    lagrangeGraphic(x, y_exp, y_calc);
    return 0;
}