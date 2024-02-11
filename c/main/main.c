#include <stdio.h>
#include <math.h>

double sq4_x(double x)
{
    double res = (x < 0) ? NAN : pow(x, 0.25);
    return res;
}

int main()
{
    printf("%f", sq4_x(12));
    return 0;
}
