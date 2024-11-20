#define N 12
#define LAGRANGE_DOTS 3

void lagrangeDiagonalDiff(double x[N], double y_exp[N]);
void chooseLagrangeDots(double x[N], double y_exp[N], int x1, int x2, int x3);
void readLagrangeDots(double x[LAGRANGE_DOTS], double y_exp[LAGRANGE_DOTS]);
void lagrangeMethod(double x[N], double _x[LAGRANGE_DOTS], double _y_exp[LAGRANGE_DOTS]);