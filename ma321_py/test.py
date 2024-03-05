import numpy as np 

def dekker(f, a0, b0, tol=1e-6, max_iter=100):
    ak = a0
    bk = b0
    bk_minus_1 = a0
    
    for i in range(max_iter):
        # Calcul de la sécante
        s = bk - (bk - bk_minus_1) / (f(bk) - f(bk_minus_1)) * f(bk)
        
        # Calcul du milieu
        m = (ak + bk) / 2
        
        # Choix du prochain itéré
        if abs(s - bk) < abs(m - bk) and s > min(bk, m) and s < max(bk, m):
            bk_plus_1 = s
        else:
            bk_plus_1 = m
        
        # Choix du nouveau contrepoint
        if f(ak) * f(bk_plus_1) < 0:
            ak_plus_1 = ak
        else:
            ak_plus_1 = bk
        
        # Échange si nécessaire
        if abs(f(ak_plus_1)) < abs(f(bk_plus_1)):
            ak_plus_1, bk_plus_1 = bk_plus_1, ak_plus_1
        
        # Condition de convergence
        if abs(f(ak_plus_1)) < tol:
            return ak_plus_1
        
        # Mise à jour des itérations
        bk_minus_1 = bk
        ak = ak_plus_1
        bk = bk_plus_1
    
    raise ValueError("La méthode de Dekker n'a pas convergé après {} itérations".format(max_iter))

# Exemple d'utilisation avec une fonction f(x) quelconque
def dG(x): 
    return (x + 2)/np.sqrt((-x - 2)**2 + 2) 

# Choix des points initiaux
a0 = -10
b0 = 10

# Résolution de l'équation f(x) = 0
root = dekker(f=dG, a0=a0, b0=b0)
print("La racine de l'équation est approximativement :", root)