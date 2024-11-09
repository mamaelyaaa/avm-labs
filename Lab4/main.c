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

int main() {
    double x[N], y_exp[N];
    readFile(x, y_exp);

    experimentalDotsGraphic();
    printf("Experimental point graph created...\n");

    printf("Optimal polynomial degree: %d\n", findOptimalPolynomialDegree(x, y_exp));

    printf("%lf", chooseLagrangeDots(x, y_exp, 1, 6, 11));
    return 0;
}