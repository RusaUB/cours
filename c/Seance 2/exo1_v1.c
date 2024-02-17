/*
Nom : UBAIDULLOEV
Prenom : Rustam
Classe : 3PSC
Groupe  : C1
Seance : 2
Exercice :  1
Version : 1
Date : 05/02/2024
*/

#include <stdio.h>
//-------------------------
// Programme  Principal
//-------------------------

int main() {
    int nombre;
    printf("\n-----------------");
    printf("\n   Exercice 1 ");
    printf("\n-----------------\n");
    printf("\n n : ");
    scanf("%d",&nombre);

    while (nombre <32) {
        printf("\n n : ");
        scanf("%d",&nombre);
    }

    printf("\n Ok Merci %d >= 32  ! ",nombre );

    return 0;
}
