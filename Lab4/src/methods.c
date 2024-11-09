#include <stdio.h>
#include <stdlib.h>
#include "methods.h"

#define N 12
#define LAGRANGE_DOTS 3
#define NEWTON_DOTS 4


double chooseLagrangeDots(double x[N], double y_exp[N], int x1, int x2, int x3) {
    double dots[LAGRANGE_DOTS][2] = {0};

    int i = 0, idx = 0;

    while (i < N) {
        if ((i + 1 == x1) || (i + 1 == x2) || (i + 1 == x3)) {
            dots[idx][0] = x[i];
            dots[idx][1] = y_exp[i];
            idx++;
        }
        i++;
    }

    for (int i = 0; i < LAGRANGE_DOTS; i++) {
        printf("%d) ", i + 1);
        for (int j = 0; j < 2; j++) {
            printf("%lf ", dots[i][j]);
        }
        printf("\n");
    }

    return 0;
}

// double chooseLagrangeDots(double array[N][2], int x1, int x2, int x3) {
//     double dots[LAGRANGE_DOTS][2] = {0};

//     int i = 0, idx = 0;

//     while (i < N) {
//         if ((i + 1 == x1) || (i + 1 == x2) || (i + 1 == x3)) {
//             for (int j = 0; j < 2; j++) {
//                 dots[idx][j] = array[i][j];
//             }
//             idx++;
//         }
//         i++;
//     }

//     for (int i = 0; i < LAGRANGE_DOTS; i++) {
//         printf("%d) ", i + 1);
//         for (int j = 0; j < 2; j++) {
//             printf("%lf ", dots[i][j]);
//         }
//         printf("\n");
//     }

//     return 0;
// }

double chooseNewtonDots(double array[N][2], int x1, int x2, int x3, int x4) {
    double dots[NEWTON_DOTS][2] = {0};

    int i = 0, idx = 0;

    while (i < N) {
        if ((i + 1 == x1) || (i + 1 == x2) || (i + 1 == x3) || (i + 1 == x4)) {
            for (int j = 0; j < 2; j++) {
                dots[idx][j] = array[i][j];
            }
            idx++;
        }
        i++;
    }

    for (int i = 0; i < NEWTON_DOTS; i++) {
        printf("%d) ", i + 1);
        for (int j = 0; j < 2; j++) {
            printf("%lf ", dots[i][j]);
        }
        printf("\n");
    }

    return 0;
}

// double chooseNewtonDots(double array[N][2], int x1, int x2, int x3, int x4) {
//     double dots[NEWTON_DOTS][2] = {0};

//     int i = 0, idx = 0;

//     while (i < N) {
//         if ((i + 1 == x1) || (i + 1 == x2) || (i + 1 == x3) || (i + 1 == x4)) {
//             for (int j = 0; j < 2; j++) {
//                 dots[idx][j] = array[i][j];
//             }
//             idx++;
//         }
//         i++;
//     }

//     for (int i = 0; i < NEWTON_DOTS; i++) {
//         printf("%d) ", i + 1);
//         for (int j = 0; j < 2; j++) {
//             printf("%lf ", dots[i][j]);
//         }
//         printf("\n");
//     }

//     return 0;
// }