import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar

def F(x):
    return x**4 + 8*x**3 + 24*x**2 + 32*x + 17

# Trouver les minimums
result_brent = minimize_scalar(F, method='brent', tol=1e-10)
result_golden = minimize_scalar(F, method='golden', tol=1e-10)

print("Minimum trouvé avec la méthode brent:", result_brent.x)
print("Minimum trouvé avec la méthode golden:", result_golden.x)

x = np.linspace(-10, 10, 1000)

plt.plot(x, F(x))
plt.scatter(result_brent.x, F(result_brent.x), color='red', label=f'Minimum brent ({result_brent.x:.2f},{F(result_brent.x):.2f})')
plt.scatter(result_golden.x, F(result_golden.x), color='blue', label=f'Minimum golden ({result_golden.x:.2f},{F(result_golden.x):.2f})')
plt.legend()
plt.show()

# Fonction de recherche par la méthode de la section dorée
def golden_section_search(f, a, b, tol=1e-10):
    evolution = []  # stocker l'évolution du point minimum
    intervals = []  # stocker l'évolution de l'intervalle [a, b]
    iteration = 0
    golden_ratio = (1 + np.sqrt(5)) / 2
    c = b - (b - a) / golden_ratio
    d = a + (b - a) / golden_ratio
    while abs(c - d) > tol:
        iteration += 1
        if f(c) < f(d):
            b = d
        else:
            a = c
        c = b - (b - a) / golden_ratio
        d = a + (b - a) / golden_ratio
        evolution.append((b + a) / 2)  # stocker le point minimum actuel
        intervals.append((a, b))  # stocker l'intervalle actuel
    print(iteration, "itérations")  # afficher le nombre d'itérations
    return (b + a) / 2, evolution, intervals

# Calculer la recherche par section dorée pour chaque point minimum
minimum_golden, _, intervals_golden = golden_section_search(F, -10, 10)

# Définir les itérations spécifiques pour le tracé
specific_iterations = [1, 10, 20, 30, 48]  # Spécifier les itérations spécifiques

# Tracer la fonction originale F(x) avec l'évolution de l'intervalle [a, b] pour des itérations spécifiques
x_values = np.linspace(-10, 10, 1000)

# Créer les sous-graphiques
fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# Premier sous-graphique: Vue générale de la recherche autour du minimum de la méthode de la section dorée
ax1 = axes[0,0]
ax1.plot(x_values, F(x_values), label='F(x)')
for i, interval in enumerate(intervals_golden):
    if i + 1 in specific_iterations:
        ax1.plot(interval, [F(interval[0]), F(interval[1])], 'o-', label=f'Itération {i+1}')
ax1.set_xlabel('x')
ax1.set_ylabel('F(x)')
ax1.set_title(f'Recherche par la section dorée autour du minimum ({minimum_golden:.2f})')
ax1.legend()
ax1.grid(True)

# Deuxième sous-graphique: Vue zoomée autour du minimum de la méthode de la section dorée
ax2 = axes[0,1]
ax2.plot(x_values, F(x_values), label='F(x)')
for i, interval in enumerate(intervals_golden):
    if i + 1 in specific_iterations:
        ax2.plot(interval, [F(interval[0]), F(interval[1])], 'o-', label=f'Itération {i+1}')
ax2.set_xlabel('x')
ax2.set_ylabel('F(x)')
ax2.set_title(f'Zoom près du minimum ({minimum_golden:.2f}) à 1e-1')
ax2.legend()
ax2.grid(True)
ax2.set_xlim(minimum_golden - 0.1, minimum_golden + 0.1)  # Zoom près du minimum

# Troisième sous-graphique: Vue encore plus zoomée autour du minimum de la méthode de la section dorée
ax3 = axes[1,0]
ax3.plot(x_values, F(x_values), label='F(x)')
for i, interval in enumerate(intervals_golden):
    if i + 1 in specific_iterations:
        ax3.plot(interval, [F(interval[0]), F(interval[1])], 'o-', label=f'Itération {i+1}')
ax3.set_xlabel('x')
ax3.set_ylabel('F(x)')
ax3.set_title(f'Zoom encore plus près du minimum ({minimum_golden:.2f}) à 1e-3')
ax3.legend()
ax3.grid(True)
ax3.set_xlim(minimum_golden - 1e-3, minimum_golden + 1e-3)  # Zoom encore plus près du minimum

# Quatrième sous-graphique: Vue extrêmement zoomée autour du minimum de la méthode de la section dorée
ax4 = axes[1,1]
ax4.plot(x_values, F(x_values), label='F(x)')
for i, interval in enumerate(intervals_golden):
    if i + 1 in specific_iterations:
        ax4.plot(interval, [F(interval[0]), F(interval[1])], 'o-', label=f'Itération {i+1}')
ax4.set_xlabel('x')
ax4.set_ylabel('F(x)')
ax4.set_title(f'Zoom extrêmement près du minimum ({minimum_golden:.2f}) à 1e-8')
ax4.legend()
ax4.grid(True)
ax4.set_xlim(minimum_golden - 1e-8, minimum_golden + 1e-8)  # Zoom extrêmement près du minimum

plt.tight_layout()
plt.show()
