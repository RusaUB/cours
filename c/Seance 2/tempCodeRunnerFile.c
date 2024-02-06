/*
--------------------------------------
Nom      : UBAIDULLOEV
Prenom   : Rustam
Classe   : 3PSC
Groupe   : C1
Seance   : 2
Exercice : 2
Version  : 1
Date     :5/02/2024
--------------------------------------

--------------------------------------
Programme Principal
--------------------------------------
*/
#include <stdio.h>

int main()
{
    int choice;
    int nombre;

    printf("\n ------------------ ");
    printf("\n Exercice 2");
    printf("\n ------------------ \n \n");

    do
    {
        printf("------------------ \n");
        printf("Table de Multiplication de %d \n", nombre);
        printf("------------------ \n");

        for (int i = 1; i <= 10; i++)
        {
            printf("%d * %d = %d \n", nombre, i, nombre * i);
        }

        printf("------------------ \n");
        do
        {
            printf("Saisir un valuer : ");
            scanf("%d", &nombre);

        } while (0 >= nombre || nombre > 10);
        printf("Voulaiz vous recommencer ? \n");
        scanf("%d", choice);
    } while (choice == 0 || choice == 1);

    printf("Merci et Aurevoir");

    return 0;
}