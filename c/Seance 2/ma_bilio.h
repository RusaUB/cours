
#define max 30
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
    S = 0; // йlйment neutre de la somme est 0
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
    P = 1; // йlйment neutre du produit est 1
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