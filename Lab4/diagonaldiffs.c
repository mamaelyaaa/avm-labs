#include <stdio.h>
#include <stdlib.h>
#include "diagonaldiffs.h"

#define N 12

int lagrangeDiagonalDiff(double x[N], double y_exp[N]) {
    FILE *file = fopen("lagrange/lagrange_table.txt", "w");

    double diagonalTable[N][N];
    double delta_y[N - 1];
    double dm[N - 1];
    double maxValue, minValue;

    for (int i = 0; i < N - 1; i++) {
        
        double diff = y_exp[i] - y_exp[i + 1];

        if (i == 0) {
            maxValue = diff;
            minValue = diff;
        }

        maxValue = (diff >= maxValue) ? diff : maxValue;
        minValue = (diff <= minValue) ? diff : minValue;

        diagonalTable[i][0] = diff;
        delta_y[i] = diff;
    }
    dm[0] = maxValue - minValue;
    
    for (int i = 1; i < N - 1; i++) {
        double maxValue, minValue;

        for (int j = 0; j < N - i - 1; j++) {
            double diff = delta_y[j] - delta_y[j + 1];
            diagonalTable[j][i] = diff;

            if (j == 0) {
                maxValue = diff;
                minValue = diff;
            }

            maxValue = (diff >= maxValue) ? diff : maxValue;
            minValue = (diff <= minValue) ? diff : minValue;

            delta_y[j] = diff;
        }
        dm[i] = maxValue - minValue;
    }

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N - 1; j++) {
            fprintf(file, "%.2lf\t ", diagonalTable[i][j]);
        }
        fprintf(file, "\n");
    }

    fprintf(file, "\n");
    for (int i = 0; i < N - 1; i++) {
        fprintf(file, "%.2lf\t ", dm[i]);
    }

    int optimalPolynomial = 1;

    for (int i = 0; i < N - 2; i++) {        
        if (dm[i] < dm[optimalPolynomial]) {
            optimalPolynomial = i;
        }
    }
    return optimalPolynomial + 1;
}

// int newtonOptimalPolynomialDegree(double x[N], double y_exp[N]) {
//     double temp_y[N - 1];
//     double deltaY0[N - 1];
//     double newtonFunc = y_exp[0];

//     for (int i = 0; i < N - 1; i++) {
//         double diff = (y_exp[i + 1] - y_exp[i]) / (x[i + 1] - x[i]);
//         if (i == 0) {
//             deltaY0[i] = diff;
//         }
//         temp_y[i] = diff;
//         printf("delta0y: %lf\n", temp_y[i]);
//     }

//     printf("%lf", deltaY0[0]);

//     for (int i = 1; i < N - 1; i++) {
//         for (int j = 0; j < N - i - 1; j++) {
//             double diff = (temp_y[i + 1] - temp_y[i]) / (x[i + 1] - x[i]);

//             if (j == 0) {
//                 deltaY0[i] = diff;
//             }

//             temp_y[j] = diff;
//         }
//     }
// }