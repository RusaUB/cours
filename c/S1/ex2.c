/*
--------------------------------------
Nom      : UBAIDULLOEV
Prenom   : Rustam
Classe   : 3PSC
Groupe   : C1
Seance   : 1
Exercice : 2
Version  : 1
Date     :31/01/2024
--------------------------------------
*/
#include <stdio.h>

int main()
{
    float a, b;

    printf("-------------------");
    printf("\n   Exercie 2 ");
    printf("\n------------------- \n");

    // Demander à l'utilisateur de saisir deux nombres
    printf("Entrez le premier nombre (a) : ");
    scanf("%f", &a);

    printf("Entrez le deuxième nombre (b) : ");
    scanf("%f", &b);

    // Calculer et afficher la somme des deux nombres
    printf("La somme de %.2f et %.2f est : %.2f  \n", a, b, a + b);

    // Calculer et afficher le produit des deux nombres
    printf("Le produit de %.2f et %.2f est : %.2f \n", a, b, a * b);

    return 0;
}
