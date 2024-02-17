/*---------------------
NOM      : UBAIDULLOEV
Prenom   : Rustam
Classe   : 3PSC
Groupe   : C1
Séance   : 2
Exercice : 2
Version  : 1
Date     : 05/02/2024
*/

#include <stdio.h>

//---------------------
// Programme principal
//---------------------

main()
{
  int n, i, r;
  printf("\n-----------------");
  printf("\n   Exercice 2 ");
  printf("\n-----------------\n");
  do
  {
    do
    {
      printf("n:");
      scanf("%d", &n);

    } while (n <= 0 || n > 10);

    printf("\t\t\t\t------------------------------------\n");
    printf("\t\t\t\t Table de Multiplication de %d \n", n);
    printf("\t\t\t\t------------------------------------\n");
    for (i = 1; i <= 10; i++)
    {
      printf("\n\t\t\t\t\t%d*%d = %d", i, n, i * n);
    }
    printf("\n\t\t\t\t------------------------------------\n");
    do
    {
      printf("\n Voulez vous recommencer (1 : oui / 0 : non ) ");
      scanf("%d", &r);
    } while (r != 0 && r != 1);
  } while (r == 1);
  printf("\n Merci et au revoir !!!  ");
}
