#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct
{
    int j; // jour de naissance
    int m; // mois de naissance
    int a; // annee de naissance
} date;

typedef struct
{
    char prenom[20];
    char nom[20];
    date ddn; // La date de naissance de type date.
    float note1, note2, note3, moyenne;
} etudiant;

void menu();
void saisir_etudiants(etudiant **liste_etudiants, int *nombre_etudiants);
void afficher_etudiants(etudiant *liste_etudiants, int nombre_etudiants);
void rechercher_etudiants(etudiant *liste_etudiants, int nombre_etudiants);
void supprimer_etudiant(etudiant **liste_etudiants, int *nombre_etudiants);

int main()
{
    menu();
    return 0;
}

void menu()
{
    etudiant *liste_etudiants = NULL;
    int nombre_etudiants = 0;
    int expression;

    do
    {
        printf("\n----------Menu----------\n");
        printf("1 - Saisir étudiants\n");
        printf("2 - Afficher étudiants\n");
        printf("3 - Rechercher étudiants\n");
        printf("4 - Supprimer étudiant\n");
        printf("5 - Fin\n");
        printf("Choisir une option : ");
        scanf("%d", &expression);

        switch (expression)
        {
        case 1:
            saisir_etudiants(&liste_etudiants, &nombre_etudiants);
            break;
        case 2:
            afficher_etudiants(liste_etudiants, nombre_etudiants);
            break;
        case 3:
            rechercher_etudiants(liste_etudiants, nombre_etudiants);
            break;
        case 4:
            supprimer_etudiant(&liste_etudiants, &nombre_etudiants);
            break;
        case 5:
            printf("Merci et à bientôt.\n");
            break;
        default:
            printf("Choisissez entre 1 et 5.\n");
            break;
        }
    } while (expression != 5);

    free(liste_etudiants); // Free allocated memory before exiting
}

void saisir_etudiants(etudiant **liste_etudiants, int *nombre_etudiants)
{
    int jour, mois, annee;
    int max_jours;

    (*nombre_etudiants)++;
    *liste_etudiants = (etudiant *)realloc(*liste_etudiants, (*nombre_etudiants) * sizeof(etudiant));
    etudiant *nouvel_etudiant = *liste_etudiants + (*nombre_etudiants) - 1;

    printf("Prénom de l'étudiant : ");
    scanf("%s", nouvel_etudiant->prenom);
    printf("Nom de l'étudiant : ");
    scanf("%s", nouvel_etudiant->nom);

    // Validate day
    do
    {
        printf("Jour de naissance : ");
        scanf("%d", &jour);
        if (jour < 1 || jour > 31)
        {
            printf("Le jour doit être compris entre 1 et 31.\n");
        }
    } while (jour < 1 || jour > 31);

    // Validate month
    do
    {
        printf("Mois de naissance : ");
        scanf("%d", &mois);
        if (mois < 1 || mois > 12)
        {
            printf("Le mois doit être compris entre 1 et 12.\n");
        }
    } while (mois < 1 || mois > 12);

    // Validate year and handle leap year
    do
    {
        printf("Année de naissance : ");
        scanf("%d", &annee);
        if (annee < 1900 || annee > 2024)
        {
            printf("L'année doit être comprise entre 1900 et 2024.\n");
        }
    } while (annee < 1900 || annee > 2024);

    // Check for leap year and validate day
    if ((annee % 4 == 0 && annee % 100 != 0) || annee % 400 == 0)
    {
        if (mois == 2)
        {
            max_jours = 29;
        }
        else if (mois == 4 || mois == 6 || mois == 9 || mois == 11)
        {
            max_jours = 30;
        }
        else
        {
            max_jours = 31;
        }
    }
    else
    {
        if (mois == 2)
        {
            max_jours = 28;
        }
        else if (mois == 4 || mois == 6 || mois == 9 || mois == 11)
        {
            max_jours = 30;
        }
        else
        {
            max_jours = 31;
        }
    }

    while (jour < 1 || jour > max_jours)
    {
        printf("Le jour de naissance est invalide pour ce mois.\n");
        printf("Jour de naissance : ");
        scanf("%d", &jour);
    }

    nouvel_etudiant->ddn.j = jour;
    nouvel_etudiant->ddn.m = mois;
    nouvel_etudiant->ddn.a = annee;

    printf("Note 1 : ");
    scanf("%f", &nouvel_etudiant->note1);
    printf("Note 2 : ");
    scanf("%f", &nouvel_etudiant->note2);
    printf("Note 3 : ");
    scanf("%f", &nouvel_etudiant->note3);
    nouvel_etudiant->moyenne = (nouvel_etudiant->note1 + nouvel_etudiant->note2 + nouvel_etudiant->note3) / 3;
}

void afficher_etudiants(etudiant *liste_etudiants, int nombre_etudiants)
{
    printf("\nListe des étudiants :\n");
    for (int i = 0; i < nombre_etudiants; i++)
    {
        printf("Etudiant %d :\n", i + 1);
        printf("Prénom : %s\n", liste_etudiants[i].prenom);
        printf("Nom : %s\n", liste_etudiants[i].nom);
        printf("Date de naissance : %d/%d/%d\n", liste_etudiants[i].ddn.j, liste_etudiants[i].ddn.m, liste_etudiants[i].ddn.a);
        printf("Moyenne : %.2f\n", liste_etudiants[i].moyenne);
    }
}

void rechercher_etudiants(etudiant *liste_etudiants, int nombre_etudiants)
{
    char recherche[20];
    int found = 0;
    printf("Entrez le nom, le prénom ou l'année de naissance de l'étudiant à rechercher : ");
    scanf("%s", recherche);
    printf("\nRésultats de la recherche :\n");
    for (int i = 0; i < nombre_etudiants; i++)
    {
        if (strcmp(recherche, liste_etudiants[i].nom) == 0 || strcmp(recherche, liste_etudiants[i].prenom) == 0 || atoi(recherche) == liste_etudiants[i].ddn.a)
        {
            printf("Etudiant %d :\n", i + 1);
            printf("Prénom : %s\n", liste_etudiants[i].prenom);
            printf("Nom : %s\n", liste_etudiants[i].nom);
            printf("Date de naissance : %d/%d/%d\n", liste_etudiants[i].ddn.j, liste_etudiants[i].ddn.m, liste_etudiants[i].ddn.a);
            printf("Moyenne : %.2f\n", liste_etudiants[i].moyenne);
            found = 1;
        }
    }
    if (!found)
    {
        printf("Aucun étudiant trouvé avec ces critères.\n");
    }
}

void supprimer_etudiant(etudiant **liste_etudiants, int *nombre_etudiants)
{
    char nom_suppr[20];
    int found = 0;
    printf("Entrez le nom de l'étudiant à supprimer : ");
    scanf("%s", nom_suppr);
    for (int i = 0; i < *nombre_etudiants; i++)
    {
        if (strcmp(nom_suppr, (*liste_etudiants)[i].nom) == 0)
        {
            for (int j = i; j < *nombre_etudiants - 1; j++)
            {
                (*liste_etudiants)[j] = (*liste_etudiants)[j + 1];
            }
            (*nombre_etudiants)--;
            *liste_etudiants = (etudiant *)realloc(*liste_etudiants, (*nombre_etudiants) * sizeof(etudiant));
            found = 1;
            printf("Etudiant supprimé avec succès.\n");
            break;
        }
    }
    if (!found)
    {
        printf("Aucun étudiant trouvé avec ce nom.\n");
    }
}
