#include <stdio.h>
#include <stdlib.h>
#include "graphic.h"

void experimentalDotsGraphic() {
    FILE *gnuplot = popen("gnuplot", "w");

    if (!gnuplot) {
        perror("popen");
        exit(EXIT_FAILURE);
    }
    
    fprintf(gnuplot, "set title 'Экспериментальные точки'\n");
    fprintf(gnuplot, "set xlabel 'Ось X'\n");
    fprintf(gnuplot, "set ylabel 'Ось Y' rotate by 0\n");
    fprintf(gnuplot, "set grid\n");
    fprintf(gnuplot, "unset key\n");
    
    fprintf(gnuplot, "set yrange [-28:0]\n");

    // Сохраняем график в pics/expdots.png
    fprintf(gnuplot, "set terminal png\n");
    fprintf(gnuplot, "set output './pics/expdots.png'\n");

    fprintf(gnuplot, "plot 'cords.txt' using 1:2 with points pointtype 7\n");
    pclose(gnuplot);
}

