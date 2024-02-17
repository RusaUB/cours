/*
NOM      : UBAIDULLOEV
Prenom   : Rustam
Classe   : 3PSC
Groupe   : C1
Séance   : 2
Exercice : 4
Version  : 1
Date     : 05/02/2024
*/

#include <string.h>
#include <stdio.h>

//-------------------------
// Programme  Principal
//-------------------------
int main() {
     char nom[30],prenom[30], id [61];

      printf(" Nom : ");
      gets(nom);

      printf("\n Prenom : ");
      gets(prenom);
      //scanf("%s",&nom);

      strcpy(id,prenom);
      strcat(id," ");
      strcat(id,nom);

      /* char  t3[6];
     strcpy(t3,"salut");*/
     printf("\nnom : %s et sa taille est %d ", nom , strlen(nom));
     printf("\nprenom : %s et sa taille est %d ", prenom , strlen(prenom));
     printf("\nBonjour %s comment ca va ? %d", id, strlen(id));
     if ( strcmp(id,"Mehdi BEN THAIER")==0)
        printf("\n Bienvenu a ton espace perso !!!");
     else
        printf("\n Mais c est pas toi !!! go out ciao !!!!! ");
    return 0;
}
