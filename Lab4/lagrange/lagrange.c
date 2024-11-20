#include <stdio.h>
#include <stdlib.h>

#define N 12
#define LAGRANGE_DOTS 3

void lagrangeDiagonalDiff(double x[N], double y_exp[N]) {
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
}

void chooseLagrangeDots(double x[N], double y_exp[N], int x1, int x2, int x3) {
    FILE *file = fopen("lagrange/lagrange_dots.txt", "w");

    int i = 0, idx = 0;

    while (i <= N) {
        if ((i + 1 == x1) || (i + 1 == x2) || (i + 1 == x3)) {
            fprintf(file, "%.2lf\t%.2lf\n", x[i], y_exp[i]);
        }
        i++;
    }
}

void readLagrangeDots(double Lx[LAGRANGE_DOTS], double Ly_exp[LAGRANGE_DOTS]) {
    FILE *file = fopen("lagrange/lagrange_dots.txt", "r");

    if (!file) {
        printf("File Error: Cannot find lagrange/lagrange_dots.txt");
        exit(1);
    }

    for (int i = 0; i < LAGRANGE_DOTS; i++){
        fscanf(file, "%lf %lf\n", &Lx[i], &Ly_exp[i]);
    }
    fclose(file);
}

double lagrangeFunc(double x, double _x[LAGRANGE_DOTS], double _y_exp[LAGRANGE_DOTS]) {
    double res = 0.0;

    for (int i = 0; i < LAGRANGE_DOTS; i++) {
        double prod = 1.0;

        for (int j = 0; j < LAGRANGE_DOTS; j++) {
            if (i != j) {
                prod *= (x - _x[j]) / (_x[i] - _x[j]);
            }
        }
        res += _y_exp[i] * prod;
    }
    return res;
}

void lagrangeMethod(double x[N], double _x[LAGRANGE_DOTS], double _y_exp[LAGRANGE_DOTS]) {
    FILE *file = fopen("lagrange/lagrange_calc.txt", "w");
    double y_calc[N];

    for (int i = 0; i < N; i++) {
        y_calc[i] = lagrangeFunc(x[i], _x, _y_exp);
        fprintf(file, "%.3lf\t%.3lf\n", x[i], y_calc[i]);
    }
}
