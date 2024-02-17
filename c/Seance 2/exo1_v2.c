/*
Nom : UBAIDULLOEV
Prenom : Rustam
Classe : 3PSC
Groupe  : C1
Seance : 2
Exercice :1
Version : 2 : do ___ while
Date : 05/02/24
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

    do{
    printf("\n n : ");
    scanf("%d",&nombre);

    }while (nombre <32) ;

    printf("\n Ok Merci %d >= 32  ! ",nombre );

    return 0;
}
