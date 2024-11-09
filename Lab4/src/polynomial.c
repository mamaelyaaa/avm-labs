#include <stdio.h>
#include <stdlib.h>
#include "polynomial.h"

#define N 12

int findOptimalPolynomialDegree(double x[N], double y_exp[N]) {
    FILE *output = fopen("src/dm.txt", "w");

    double dm[N - 2];
    double new_y[N - 1];

    for (int i = 0; i < N - 1; i++) {
        double diff = y_exp[i] - y_exp[i + 1];
        new_y[i] = diff;
    }

    for (int i = 1; i < N - 1; i++) {
        double maxValue, minValue;

        for (int j = 0; j < N - i - 1; j++) {
            double diff = new_y[j] - new_y[j + 1];

            if (j == 0) {
                maxValue = diff;
                minValue = diff;
            }
            
            maxValue = (diff >= maxValue) ? diff : maxValue;
            minValue = (diff <= minValue) ? diff : minValue;

            new_y[j] = diff;
        }
        dm[i] = maxValue - minValue;
    }

    fprintf(output, "dm: \n");
    for (int i = 1; i < N - 2; i++) {        
        fprintf(output, "%d\t%.3lf\n", i, dm[i]);
    }
    fclose(output);

    int optimalPolynomial = 1;

    for (int i = 1; i < N - 2; i++) {        
        if (dm[i] < dm[optimalPolynomial]) {
            optimalPolynomial = i;
        }
    }
    return optimalPolynomial;
}

// int findOptimalPolynomialDegree(double x[N], double y_exp[]double array[N][2]) {
//     FILE *output = fopen("src/dm.txt", "w");

//     double y_exp[N];

//     for (int i = 0; i < N; i++) {
//         y_exp[i] = array[i][1];
//     }

//     double dm[N - 2];
//     double new_y[N - 1];

//     for (int i = 0; i < N - 1; i++) {
//         double diff = y_exp[i] - y_exp[i + 1];
//         new_y[i] = diff;
//     }

//     for (int i = 1; i < N - 1; i++) {
//         double maxValue, minValue;

//         for (int j = 0; j < N - i - 1; j++) {
//             double diff = new_y[j] - new_y[j + 1];

//             if (j == 0) {
//                 maxValue = diff;
//                 minValue = diff;
//             }
            
//             maxValue = (diff >= maxValue) ? diff : maxValue;
//             minValue = (diff <= minValue) ? diff : minValue;

//             new_y[j] = diff;
//         }
//         dm[i] = maxValue - minValue;
//     }

//     fprintf(output, "dm: \n");
//     for (int i = 1; i < N - 2; i++) {        
//         fprintf(output, "%d\t%.3lf\n", i, dm[i]);
//     }
//     fclose(output);

//     int optimalPolynomial = 1;

//     for (int i = 1; i < N - 2; i++) {        
//         if (dm[i] < dm[optimalPolynomial]) {
//             optimalPolynomial = i;
//         }
//     }
//     return optimalPolynomial;
// }