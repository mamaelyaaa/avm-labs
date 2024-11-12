#include <stdio.h>
#include <stdlib.h>
#include "methods.h"

#define N 12
#define LAGRANGE_DOTS 3
#define NEWTON_DOTS 4


double lagrangeFunc(double x, double dots[LAGRANGE_DOTS][2]) {
    double res = 0.0;

    for (int i = 0; i < LAGRANGE_DOTS; i++) {
        double prod = 1.0;

        for (int j = 0; j < LAGRANGE_DOTS; j++) {
            if (i != j) {
                prod *= (x - dots[j][0]) / (dots[i][0] - dots[j][0]);
            }
        }
        res += dots[i][1] * prod;
    }
    return res;
}
    
void chooseLagrangeDots(double x[N], double y_exp[N], int x1, int x2, int x3) {
    FILE *output = fopen("src/lagrange_y_calc.txt", "w");

    double dots[LAGRANGE_DOTS][2] = {0};

    int i = 0, idx = 0;

    while (i <= N) {
        if ((i + 1 == x1) || (i + 1 == x2) || (i + 1 == x3)) {
            dots[idx][0] = x[i];
            dots[idx][1] = y_exp[i];
            idx++;
        }
        i++;
    }

    double y_calc[N];

    for (int i = 0; i < N; i++) {
        y_calc[i] = lagrangeFunc(x[i], dots);
        fprintf(output, "%.3lf\n", y_calc[i]);
    }
}