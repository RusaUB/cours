/*
--------------------------------------
Nom      : UBAIDULLOEV
Prenom   : Rustam
Classe   : 3PSC
Groupe   : C1
Seance   : 2
Exercice : 1
Version  : 2
Date     :5/02/2024
--------------------------------------

--------------------------------------
Programme Principal
--------------------------------------
*/
#include <stdio.h>

int main()
{
    int nombre;
    printf("\n ------------------ ");
    printf("\n Exercice 1");
    printf("\n ------------------ \n \n");

    do
    {
    printf("n : ");
    scanf("%d", &nombre);
        /* code */
    } while (nombre < 33);
    
    printf("Merci %d >= 32 \n", nombre);
    return 0;
}