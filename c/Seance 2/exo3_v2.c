/*
NOM : UBAIDULLOEV
PRENOM : Rustam
GROUPE : 3SC1
SEANCE : 2
EXERCICE : 3
VERSION : 2 les basiques saisir / affichage d un tableau
DATE : 05/02/2024
*/

#include <stdio.h>
#include<math.h>
//-------------------------
// Programme  Principal
//-------------------------
int main() {

    int t1[30],nombre,v,i,S,P;
    float M;
  //------------------------------1--------------------------------

    printf("\n-----------------");
    printf("\n   Exercice 3 ");
    printf("\n-----------------\n");
    do{printf("\n n : ");
        scanf("%d",&nombre);
    }while (nombre <= 0 || nombre > 30);
  //------------------------------2--------------------------------
    for(i=0;i<nombre;i++){
            printf(" Saisir la valeurs de t1[%d]: ",i);
            scanf("%d",&t1[i]);

        }
  //------------------------------3--------------------------------

    printf("t1 :");
    for(i=0;i<nombre;i++){
            printf("%d /",t1[i]);
    }
    printf("\nvous avez %d elements dans t1",nombre);
 // ----------------------- somme -------------------------

    S = 0; // �l�ment neutre de la somme est 0
    for(i=0;i<nombre;i++){
        S = S + t1[i];
    }
    printf("\nLa somme des elements de t1 : %d",S);
 // ----------------------- produit -------------------------

    P = 1; // �l�ment neutre du produit est 1
    for(i=0;i<nombre;i++){
        P = P * t1[i];
    }
    printf("\nLe produit des elements de t1 : %d",P);
 // ----------------------- produit -------------------------

    M= (float)S/(float)nombre;
    printf("\nLa moyenne des  elements de t1 : %.2f",M);

    return 0;
}
