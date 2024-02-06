#include <stdio.h>

int main()
{
    char d = 10;
    /*
    Опреция инциальзации а не присвивания поэтому можно записать в этой форме:
        char *gpt  = &d;
    Хотя как при присвивании нужно было записывать в такой форме gpt  = &d; то есть без "*"
     */
    char *gpt  = &d; 

    printf("gpt = %p, *gpt = %d, d = %d \n", gpt, *gpt, d);

    *gpt = 100; // так же меняет значения переменной d

    printf("gpt = %p, *gpt = %d, d = %d \n", gpt, *gpt, d);

    return 0;
}