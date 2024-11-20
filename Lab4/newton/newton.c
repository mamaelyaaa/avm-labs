#include <stdio.h>
#include <stdlib.h>

#define N 12
#define NEWTON_DOTS 4

void chooseNewtonDots(double x[N], double y_exp[N], int x1, int x2, int x3, int x4) {
    FILE *file = fopen("newton/newton_dots.txt", "w");

    int i = 0, idx = 0;

    while (i <= N) {
        if ((i + 1 == x1) || (i + 1 == x2) || (i + 1 == x3) || (i + 1 == x4)) {
            fprintf(file, "%.2lf\t%.2lf\n", x[i], y_exp[i]);
        }
        i++;
    }
}

void readNewtonDots(double Nx[NEWTON_DOTS], double Ny_exp[NEWTON_DOTS]) {
    FILE *file = fopen("newton/newton_dots.txt", "r");

    if (!file) {
        printf("File Error: Cannot find newton/newton_dots.txt");
        exit(1);
    }

    for (int i = 0; i < NEWTON_DOTS; i++){
        fscanf(file, "%lf %lf\n", &Nx[i], &Ny_exp[i]);
        // printf("%lf %lf\n", Nx[i],Ny_exp[i]);
    }
    fclose(file);
}

double newtonFunc(double x, double Nx[NEWTON_DOTS], double Ny_exp[NEWTON_DOTS], double delta_y0[NEWTON_DOTS - 1]) {
    double res = Ny_exp[0];
    int idx = 0;

    while (idx < NEWTON_DOTS)
    {
        double prod = delta_y0[idx];  

        for (int i = 0; i <= idx; i++) {
            if (prod != 0) {
                prod *= (x - Nx[i]);
            }
        }    

        res += prod;
        idx += 1;
    }
    return res;
}

void newtonDiagonalDiff(double x[N], double Nx[NEWTON_DOTS], double Ny_exp[NEWTON_DOTS]) {
    FILE *diagfile = fopen("newton/newton_table.txt", "w");
    FILE *outputfile = fopen("newton/newton_calc.txt", "w");

    double diagonalTable[NEWTON_DOTS][NEWTON_DOTS];
    double delta_y[NEWTON_DOTS];
    double delta_y0[NEWTON_DOTS - 1];

    for (int i = 0; i < NEWTON_DOTS - 1; i++) {
        double diff = (Ny_exp[i + 1] - Ny_exp[i]) / (Nx[i + 1] - Nx[i]);

        if (i == 0) {
            delta_y0[i] = diff;
        }
        
        diagonalTable[i][0] = diff;
        
        delta_y[i] = diff;
    }

    for (int i = 1; i < NEWTON_DOTS; i++) {
        for (int j = 0; j < NEWTON_DOTS - i - 1; j++) {
            double diff = (delta_y[j + 1] - delta_y[j]) / (Nx[i + j + 1] - Nx[j]);
            diagonalTable[j][i] = diff;

            if (j == 0) {
                delta_y0[i] = diff;
            }

            delta_y[j] = diff;
        }
    }

    for (int i = 0; i < NEWTON_DOTS; i++) {
        for (int j = 0; j < NEWTON_DOTS - 1; j++) {
            fprintf(diagfile, "%.2lf\t ", diagonalTable[i][j]);
        }
        fprintf(diagfile, "\n");
    }

    double y_calc[N];

    for (int i = 0; i < N; i++) {
        y_calc[i] = newtonFunc(x[i], Nx, Ny_exp, delta_y0);
        fprintf(outputfile, "%.3lf\t%.3lf\n", x[i], y_calc[i]);
    }
}