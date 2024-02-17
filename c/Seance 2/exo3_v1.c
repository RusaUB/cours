/*
NOM : UBAIDULLOEV
PRENOM : Rustam
GROUPE : 3SC1
SEANCE : 2
EXERCICE : 3
VERSION : 1 : les basiques saisir / affichage d un tableau
DATE : 05/02/2024
*/

#include <stdio.h>
//-------------------------
// Programme  Principal
//-------------------------

int main()
{

  int t1[30], nombre, v, i;
  //------------------------------1--------------------------------

  printf("\n-----------------");
  printf("\n   Exercice 3 ");
  printf("\n-----------------\n");
  do
  {
    printf("\n n : ");
    scanf("%d", &nombre);
  } while (nombre <= 0 || nombre > 30);
  //------------------------------2--------------------------------
  for (i = 0; i < nombre; i++)
  {
    printf(" Saisir la valeurs de t1[%d]: ", i);
    scanf("%d", &t1[i]);
  }
  //------------------------------3--------------------------------

  printf("t1 :");
  for (i = 0; i < nombre; i++)
  {
    printf("%d /", t1[i]);
  }
  printf("\nvous avez %d elements dans t1", nombre);

  return 0;
}
