#include <stdio.h>
#include <math.h>
#include "ma_bilio.h"

/*
Nom : MESSANI
Prenom : Yani
Classe : 3PSC
Groupe  : 1
Seance : 2
Exercice : 3
Version : 4 : somme _ Produit _ moyenne _ max et pos_maxi _ mini et pos_mini z + repetition
        : Fonctions et procedures
Date : 05/02/2024
*/

/*
int maximum(int t1[30],int nombre)
{

}
*/
//-------------------------
// Programme  Principal
//-------------------------
int main()
{

    int t1[30], nombre, v, i, S, P, r;
    int maxi, pos_max, mini, pos_mini;
    float M;
    //------------------------------1--------------------------------
    titre(3);

    do
    {

        nombre = saisir_nombre();

        //------------------------------2--------------------------------
        saisir_tableau(t1, nombre);
        //------------------------------3--------------------------------
        afficher_tableau(t1, nombre);
        // ----------------------- somme -------------------------
        S = somme_tableau(t1, nombre); // appel
        printf("\nLa somme des elements de t1 : %d", S);
        // ----------------------- produit -------------------------

        P = produit_tableau(t1, nombre);
        printf("\nLe produit des elements de t1 : %d", P);
        // ----------------------- produit -------------------------

        M = moyenne(t1, nombre);
        printf("\nLa moyenne des  elements de t1 : %.2f", M);

        maxi = t1[0];
        pos_max = 0;
        for (i = 1; i < nombre; i++)
        {
            if (t1[i] > maxi)
            {
                maxi = t1[i];
                pos_max = i;
            }
        }
        printf("\nle maximum est %d et est a la place %d", maxi, pos_max);

        mini = t1[0];
        pos_mini = 0;
        for (i = 1; i < nombre; i++)
        {
            if (t1[i] < mini)
            {
                mini = t1[i];
                pos_mini = i;
            }
        }
        printf("\nle minimum est %d et est a la place %d", mini, pos_mini);

        do
        {
            printf("\n Voulez vous recommencer (1 : oui / 0 : non ) :  ");
            scanf("%d", &r);
        } while (r != 0 && r != 1);

    } while (r == 1);
    return 0;
}
