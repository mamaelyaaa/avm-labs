#include <stdio.h>
#include <stdlib.h>
#include "graphic.h"

#define N 12

void experimentalDotsGraphic() {
    FILE *gnuplot = popen("gnuplot", "w");

    if (!gnuplot) {
        perror("popen");
        exit(EXIT_FAILURE);
    }
    
    fprintf(gnuplot, "set title 'Экспериментальные точки'\n");
    fprintf(gnuplot, "set xlabel 'X'\n");
    fprintf(gnuplot, "set ylabel 'Y' rotate by 0\n");
    fprintf(gnuplot, "set grid\n");
    fprintf(gnuplot, "unset key\n");
    
    fprintf(gnuplot, "set yrange [-28:0]\n");

    // Сохраняем график в pics/expdots.png
    fprintf(gnuplot, "set terminal png\n");
    fprintf(gnuplot, "set output './graphics/pics/expdots.png'\n");

    fprintf(gnuplot, "plot 'cords.txt' u 1:2 w p pointtype 7\n");
    pclose(gnuplot);
}

void lagrangeGraphic(double x[N], double y_exp[N], double y_calc[N]) {
    FILE *gnuplot = popen("gnuplot", "w");

    if (!gnuplot) {
        perror("popen");
        exit(EXIT_FAILURE);
    }

    fprintf(gnuplot, "set title 'График полученной зависимости (Метод Лагранжа)'\n");
    fprintf(gnuplot, "set xlabel 'X'\n");
    fprintf(gnuplot, "set ylabel 'Y' rotate by 0\n");
    fprintf(gnuplot, "set grid\n");
    fprintf(gnuplot, "set key at graph 1, 0.2\n");
     
    // fprintf(gnuplot, "unset key\n");

    fprintf(gnuplot, "set yrange [-28:0]\n");

    // Сохраняем график в pics/expdots.png
    fprintf(gnuplot, "set terminal png\n");
    fprintf(gnuplot, "set output './graphics/pics/lagrange.png'\n");

    fprintf(gnuplot, "plot '-' u 1:2 w l lw 2 t 'F(x)', '-' u 1:2 w p pt 7 ps 1.5 t 'Исходные точки', '' w p pt 5 pointsize 2 lt rgb 'red' t 'Выбранные точки для полинома 2 степени'\n");

    // Строим график функции по Y расчетным

    for (int i = 0; i < N; i++) {
        fprintf(gnuplot, "%f %f\n", x[i], y_calc[i]);
    }

    fprintf(gnuplot, "e\n");

    // Проставляем исходные точки

    for (int i = 0; i < N; i++) {
        fprintf(gnuplot, "%f %f\n", x[i], y_exp[i]);
    }

    fprintf(gnuplot, "e\n");

    // Выделяем исходные точки для расчета

    for (int i = 0; i < N; i+=5) {
        fprintf(gnuplot, "%lf %lf\n", x[i], y_calc[i]);
    }

    fprintf(gnuplot, "e\n");
    pclose(gnuplot);
}

void newtonGraphic(double x[N], double y_exp[N], double y_calc[N]);