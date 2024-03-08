#include <stdio.h>
#include <math.h>
#include <stdlib.h>

/*
Nom : Messani
Prenom : Yani
Classe : 3PSC
Groupe  : 1
Seance : 3
Exercice : 4
Version : 1 :
Date : 01/03/2024
*/
//--------------------------------------------
// affichage d un titre
void titre(int i, int j)
{
    printf("-------------------------------\n");
    printf("         CHATARD Corentin       \n");
    printf("              3PSC1            \n");
    printf("-------------------------------\n");
    printf("-------------------------------\n");
    printf("        Exercice %d seance %d   \n", i, j);
    printf("-------------------------------\n");
}
//----------------------------------------------
//--------------------------------------------
int saisir_nombre()
{
    int nombre;

    do
    {
        printf("\n n : ");
        scanf("%d", &nombre);
    } while (nombre <= 0);
    return (nombre);
}
//----------------------------
void saisir_tableau(int *t1, int nombre)
{
    int i;
    for (i = 0; i < nombre; i++)
    {
        printf(" Saisir la valeurs de t1[%d]: ", i);
        scanf("%d", (t1 + i));
    }
}
//---------------------------------------
void afficher_tableau(int *t1, int nombre)
{
    int i;
    printf("t1 :");
    for (i = 0; i < nombre; i++)
    {
        printf("%d /", *(t1 + i));
    }
    printf("\nvous avez %d elements dans t1", nombre);
}
//-------------------------
// Fonction Somme
//-------------------------
int somme_tableau(int *t1, int nombre)
{

    int S, i;
    S = 0; // йlйment neutre de la somme est 0
    for (i = 0; i < nombre; i++)
    {
        S = S + (*(t1 + i));
    }
    return (S);
}
//-------------------------
// Fonction Produit
//-------------------------
int produit_tableau(int *t1, int nombre)
{
    int P, i;
    P = 1; // йlйment neutre du produit est 1
    for (i = 0; i < nombre; i++)
    {
        P = P * (*(t1 + i));
    }
    return (P);
}
//-------------------------
// Fonction Moyenne
//-------------------------
float moyenne(int *t1, int nombre)
{
    int S;
    float M;
    S = somme_tableau(t1, nombre); // appel
    M = (float)S / (float)nombre;
    return (M);
}
//-------------------------
void maximum(int *t1, int nombre, int *maxi, int *posmaxi)
{
    int i;
    *maxi = *t1;
    *posmaxi = 0;
    for (i = 1; i < nombre; i++)
    {
        if (*(t1 + i) > *maxi)
        {
            *maxi = (*(t1 + i));
            *posmaxi = i;
        }
    }
}
//-------------------------

void minimum(int *t1, int nombre, int *mini, int *posmini)
{
    int i;
    *mini = *t1;
    *posmini = 0;
    for (i = 1; i < nombre; i++)
    {
        if ((*(t1 + i)) < *mini)
        {
            *mini = (*(t1 + i));
            *posmini = i;
        }
    }
}

//----------------------------------------
void exo4()
{
    int *t1, nombre, v, i, S, P, r;
    int maxi, pos_maxi, mini, pos_mini;
    float M;
    //------------------------------1--------------------------------
    titre(4, 3);

    do
    {

        nombre = saisir_nombre();
        t1 = (int *)malloc(nombre * sizeof(int));
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

        maximum(t1, nombre, &maxi, &pos_maxi);
        printf("\nle maximum est %d et est a la place %d", maxi, pos_maxi);

        minimum(t1, nombre, &mini, &pos_mini);

        printf("\nle minimum est %d et est a la place %d", mini, pos_mini);

        do
        {
            printf("\n Voulez vous recommencer (1 : oui / 0 : non ) :  ");
            scanf("%d", &r);
        } while (r != 0 && r != 1);

    } while (r == 1);
    free(t1);
}
