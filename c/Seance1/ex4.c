/*
--------------------------------------
Nom      : UBAIDULLOEV
Prenom   : Rustam
Classe   : 3PSC
Groupe   : C1
Seance   : 1
Exercice : 4
Version  : 1
Date     :31/01/2024
--------------------------------------
*/

#include <stdio.h>
#include <math.h>

int main()
{
    float a, b, c, delta, x1, x2;

    printf("-------------------");
    printf("\n   Exercice 4 ");
    printf("\n------------------- \n");

    // Demander à l'utilisateur de saisir les coefficients
    printf("Coefficient a : ");
    scanf("%f", &a);

    printf("Coefficient b : ");
    scanf("%f", &b);

    printf("Coefficient c : ");
    scanf("%f", &c);

    // Calcul du discriminant
    delta = (b * b) - (4.0 * a * c);

    printf("Discriminant : %.2f \n", delta);

    // Tester le discriminant et afficher les résultats
    if (delta > 0)
    {
        x1 = (-b + pow(delta, 0.5)) / (2.0 * a);
        x2 = (-b - pow(delta, 0.5)) / (2.0 * a);
        printf("Deux racines réelles distinctes : x1 = %.2f, x2 = %.2f \n", x1, x2);
    }
    if (delta == 0)
    {
        x1 = -b / (2.0 * a);
        printf("Une racine réelle double : x1 = %.2f \n", x1);
    }
    if (delta < 0)
    {
        // Si le discriminant est négatif, afficher les racines complexes
        x1 = -b / (2 * a);
        x2 = sqrt(-delta) / (2 * a);
        printf("Racines complexes : z1 = %.2f + %.2fi, z2 = %.2f - %.2fi \n", x1, x2, x1, x2);
    }

    return 0;
}
