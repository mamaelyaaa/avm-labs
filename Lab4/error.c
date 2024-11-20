#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "error.h"

#define N 12
#define LAGRANGE_DOTS 3
#define NEWTON_DOTS 4

void findErrors(double y_exp[N], double Ly_calc[N], double Ny_calc[N]) {
    FILE *file = fopen("error.txt", "w");

    double lagrangeError[N];
    double newtonError[N];
    double lagrangeRes = 0;
    double newtonRes = 0;

    fprintf(file, "Lagrange\tNewton\n");
    for (int i = 0; i < N; i++) {
        lagrangeError[i] = pow(y_exp[i] - Ly_calc[i], 2);
        newtonError[i] = pow(y_exp[i] - Ny_calc[i], 2);
        lagrangeRes += lagrangeError[i];
        newtonRes += newtonError[i];
        fprintf(file, "%lf\t%lf\n", lagrangeError[i], newtonError[i]);
    }

    fprintf(file, "\nAll Dots\nLagrange Error: %lf\n", pow(lagrangeRes / (N + 1), 0.5));
    fprintf(file, "Newton Error: %lf\n", pow(newtonRes / (N + 1), 0.5));

    fprintf(file, "\nDots (which not used)\nLagrange Error: %lf\n", pow(lagrangeRes / (N - LAGRANGE_DOTS + 1), 0.5));
    fprintf(file, "Newton Error: %lf\n", pow(newtonRes / (N - NEWTON_DOTS + 1), 0.5));
}
