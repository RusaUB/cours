
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

/*
Nom : CHATARD
Prenom : Corentin
Classe : 3PSC
Groupe  : 1
Seance : 3
Exercice : 2
Version : 1
Date : 01/03/2024
*/

//----------------------------------------------
//              PROGRAMME PRINCIPAL
//----------------------------------------------
typedef struct
{
   char nom[30], prenom[30];
   float n1, n2, n3, m;
} etudiant;
//----------------------------------------------
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

etudiant saisir_1_etudiant(int i)
{

   etudiant * e;
   printf("\n-------------------------------\n");
   printf("\n           Etudiant  %d          \n", i);
   printf("\n-------------------------------\n");
   printf("\nNom : ");
   scanf("%s", &e ->nom);

   printf("\nPrenom  : ");
   scanf("%s", &e -> prenom);

   printf("\nNote 1 : ");
   scanf("%f", &e -> n1);

   printf("\nNote 2 : ");
   scanf("%f", &e -> n2);

   printf("\nNote 3 : ");
   scanf("%f", &e -> n3);

   e->m = (e->n1 + e->n2 + e->n3) / 3.0;

   return (*e);
}
void afficher_1_etudiant(etudiant * e, int i)
{
   printf("\n-------------------------------\n");
   printf("\n           Etudiant  %d         \n", i);
   printf("\n-------------------------------\n");
   printf("\nNom     : %s ", e->nom);
   printf("\nPrenom  : %s", e->prenom);
   printf("\nNote 1  : %.2f", e->n1);
   printf("\nNote 2  : %.2f", e->n2);
   printf("\nNote 3  : %.2f ", e->n3);
   printf("\n-------------------------------\n");
   printf("\nMoyenne : %.2f", e->m);
   printf("\n-------------------------------\n");
}

//------------------------------------------
int saisir_nombre_etudiant()
{
   int n;

   do
   {
      printf("\nNombres Etudiant :");
      scanf("%d", &n);

   } while (n <= 0);

   return (n);
}
//-----------------------------------------
void saisir_n_etudiant(etudiant * e, int n)
{
   int i;
   for (i = 0; i < n; i++)
   {
      e+i = saisir_1_etudiant(i + 1);
   }
}
//-----------------------------------------
void afficher_n_etudiant(etudiant * e, int n)
{
   int i;
   for (i = 0; i < n; i++)
   {
      afficher_1_etudiant(e+i, i + 1);
   }
}
//-----------------------------------------
// Programme principal
//-----------------------------------------

main()
{

   etudiant * e, n_max_e;
   int n;

   n = saisir_nombre_etudiant();
   e = (etudiant *)malloc(n * sizeof(etudiant));

   titre(2, 3);

   saisir_n_etudiant(e, n);
   afficher_n_etudiant(e, n);
}
