/*
--------------------------------------
Nom      : UBAIDULLOEV
Prenom   : Rustam
Classe   : 3PSC
Groupe   : C1
Seance   : 1
Exercice : 3
Version  : 1
Date     :31/01/2024
--------------------------------------
*/
#include <stdio.h>

int main()
{
    int n;

    printf("-------------------");
    printf("\n   Exercie 3 ");
    printf("\n-------------------");

    // Demander à l'utilisateur de saisir un nombre
    printf("\n Entrez un nombre entier n : ");
    scanf("%d", &n);

    // Vérifier si le nombre est pair ou impair
    if (n % 2 == 0)
    {
        printf("%d est un nombre pair. \n", n);
    }
    else
    {
        printf("%d est un nombre impair. \n", n);
    };

    return 0;
}