#define N 12
#define NEWTON_DOTS 4

void chooseNewtonDots(double x[N], double y_exp[N], int x1, int x2, int x3, int x4);
void readNewtonDots(double Nx[NEWTON_DOTS], double Ny_exp[NEWTON_DOTS]);
void newtonDiagonalDiff(double x[N], double Nx[NEWTON_DOTS], double Ny_exp[NEWTON_DOTS]);