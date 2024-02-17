/*
NOM      : UBAIDULLOEV
Prenom   : Rustam
Classe   : 3PSC
Groupe   : C1
Séance   : 2
Exercice : Devoir Maison
Version  : 1
Date     : 05/02/2024

OBJECTIF : Écrire un programme permettant de stocker le nom (max. 30 caractères), le prénom, ainsi que quatre notes (toutes comprises entre 0 et 20) et calculer la moyenne.
Afficher toutes les coordonnées et la moyenne.

RÉALISATION : Refaire les étapes précédentes en utilisant une boucle do-while.
*/

#include <stdio.h>
#include <string.h>

// Fonction pour calculer la moyenne des notes
float calculerMoyenne(float note1, float note2, float note3, float note4)
{
    return (note1 + note2 + note3 + note4) / 4;
}

int main()
{
    char nom[30];    // nom peut contenir jusqu'à 29 caractères + le caractère de fin de chaîne "\O"
    char prenom[30]; // prénom peut contenir jusqu'à 29 caractères + le caractère de fin de chaîne "\O"
    float note1, note2, note3, note4, moyenne;
    char reponse; 
    int i = 1;

    do
    {
        printf("Entrez le nom (max. 30 caractères) : ");
        scanf("%30s", nom);
        printf("Entrez le prénom (max. 30 caractères) : ");
        scanf("%30s", prenom);
        printf("Entrez la note 1 : ");
        scanf("%f", &note1);
        printf("Entrez la note 2 : ");
        scanf("%f", &note2);
        printf("Entrez la note 3 : ");
        scanf("%f", &note3);
        printf("Entrez la note 4 : ");
        scanf("%f", &note4);

        // Vérification des notes pour qu'elles soient comprises entre 0 et 20
        if (note1 >= 0 && note1 <= 20 && note2 >= 0 && note2 <= 20 && note3 >= 0 && note3 <= 20 && note4 >= 0 && note4 <= 20)
        {
            moyenne = calculerMoyenne(note1, note2, note3, note4);
            // Affichage des coordonnées et de la moyenne
            printf("\nCoordonnées de l'étudiant %d :\n", i);
            printf("Nom : %s\n", nom);
            printf("Prénom : %s\n", prenom);
            printf("Note 1 : %.2f\n", note1);
            printf("Note 2 : %.2f\n", note2);
            printf("Note 3 : %.2f\n", note3);
            printf("Note 4 : %.2f\n", note4);
            printf("Moyenne : %.2f\n\n", moyenne);
            i++; // Incrémentation du compteur d'étudiants
            printf("Voulez-vous réessayer ? (O/N) : ");
            scanf(" %c", &reponse); // Espace avant %c pour consommer le retour à la ligne restant
        }
        else
        {
            printf("Veuillez entrer des notes comprises entre 0 et 20.\n\n");
            reponse = 'O';
        }
    } while (reponse == 'O' || reponse == 'o');

    return 0;
}