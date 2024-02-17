/*
NOM      : UBAIDULLOEV
Prenom   : Rustam
Classe   : 3PSC
Groupe   : C1
Séance   : 2
Exercice : 3
Version  : 3 somme _ Produit _ moyenne _ max et pos_maxi _ mini et pos_mini z + repetition
Date     : 05/02/2024
*/

#include <stdio.h>
#include<math.h>
//-------------------------
// Programme  Principal
//-------------------------
int main() {

    int t1[30],nombre,v,i,S,P,r;
    float M;
  //------------------------------1--------------------------------

    printf("\n-----------------");
    printf("\n   Exercice 3 ");
    printf("\n-----------------\n");
do {
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

    int maxi,pos_max,mini,pos_mini;

    maxi = t1[0];
    pos_max = 0;
    for(i=1;i<nombre;i++){
        if(t1[i]>maxi){
            maxi = t1[i];
            pos_max = i;
        }
    }
    printf("\nle maximum est %d et est a la place %d",maxi,pos_max);

    mini = t1[0];
    pos_mini = 0;
    for(i=1;i<nombre;i++){
        if(t1[i]<mini){
            mini = t1[i];
            pos_mini = i;
        }
    }
    printf("\nle minimum est %d et est a la place %d",mini,pos_mini);

    do{
    printf("\n Voulez vous recommencer (1 : oui / 0 : non ) :  ");
    scanf("%d",&r);
    }while(r!=0 && r !=1);

}while(r==1);
    return 0;
}
