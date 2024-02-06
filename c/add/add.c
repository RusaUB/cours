#include <stdio.h>

int main()
{
    char d = 10;
    char *gpt; // тип адрессации такой же как и у переменной к которой мы ссылаемся

    gpt = &d; // берем аддресс ячейки в которой хнаринться d, gpt содержит адресс где находится d

    printf("gpt = %p, *gpt = %d, d = %d \n", gpt, *gpt, d);

    *gpt = 100; // так же меняет значения переменной d

    printf("gpt = %p, *gpt = %d, d = %d \n", gpt, *gpt, d);

    return 0;
}