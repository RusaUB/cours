#include <stdio.h>
#include <stdbool.h>

int main()
{
    // pass
    float a,b;
    a = 2.2f;
    b = 3.3f;
    float max_ab = a>b ? a : b;
    printf("%.1f",max_ab); 
    return 0;
}