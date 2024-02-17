/*
NOM      : UBAIDULLOEV
Prenom   : Rustam
Classe   : 3PSC
Groupe   : C1
Séance   : 2
Exercice : 3
Version  : 5 Fonctions et procedures
Date     : 05/02/2024
*/

#include <stdio.h>
#include <math.h>
void titre(int n)
{
    printf("\n-----------------");
    printf("\n   Exercice %d ", n);
    printf("\n-----------------\n");
}
//--------------------------------------------
int saisir_nombre()
{
    int nombre;

    do
    {
        printf("\n n : ");
        scanf("%d", &nombre);
    } while (nombre <= 0 || nombre > 30);
    return (nombre);
}
//----------------------------
void saisir_tableau(int t1[30], int nombre)
{
    int i;
    for (i = 0; i < nombre; i++)
    {
        printf(" Saisir la valeurs de t1[%d]: ", i);
        scanf("%d", &t1[i]);
    }
}
//---------------------------------------
void afficher_tableau(int t1[30], int nombre)
{
    int i;
    printf("t1 :");
    for (i = 0; i < nombre; i++)
    {
        printf("%d /", t1[i]);
    }
    printf("\nvous avez %d elements dans t1", nombre);
}
//-------------------------
// Fonction Somme
//-------------------------
int somme_tableau(int t1[30], int nombre)
{

    int S, i;
    S = 0; // �l�ment neutre de la somme est 0
    for (i = 0; i < nombre; i++)
    {
        S = S + t1[i];
    }
    return (S);
}
//-------------------------
// Fonction Produit
//-------------------------
int produit_tableau(int t1[30], int nombre)
{
    int P, i;
    P = 1; // �l�ment neutre du produit est 1
    for (i = 0; i < nombre; i++)
    {
        P = P * t1[i];
    }
    return (P);
}
//-------------------------
// Fonction Moyenne
//-------------------------
float moyenne(int t1[30], int nombre)
{
    int S;
    float M;
    S = somme_tableau(t1, nombre); // appel
    M = (float)S / (float)nombre;
    return (M);
}

//-------------------------
// Fonction pour retourner pos_mini
//-------------------------
int get_pos_mini(int t1[30], int nombre)
{
    int mini, pos_mini;
    mini = t1[0];
    pos_mini = 0;
    for (int i = 1; i < nombre; i++)
    {
        if (t1[i] < mini)
        {
            mini = t1[i];
            pos_mini = i;
        }
    }
    return (pos_mini);
}

//-------------------------
// Fonction pour retourner pos_maxi
//-------------------------
int get_pos_maxi(int t1[30], int nombre)
{
    int maxi, pos_max;
    maxi = t1[0];
    pos_max = 0;
    for (int i = 1; i < nombre; i++)
    {
        if (t1[i] > maxi)
        {
            maxi = t1[i];
            pos_max = i;
        }
    }
    return (pos_max);
}

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

        pos_max = get_pos_maxi(t1, nombre);
        maxi = t1[pos_max];
        printf("\nle maximum est %d et est a la place %d", maxi, pos_max);

        pos_mini = get_pos_mini(t1, nombre);
        mini = t1[pos_mini];
        printf("\nle minimum est %d et est a la place %d", mini, pos_mini);

        do
        {
            printf("\n Voulez vous recommencer (1 : oui / 0 : non ) :  ");
            scanf("%d", &r);
        } while (r != 0 && r != 1);

    } while (r == 1);
    return 0;
}
