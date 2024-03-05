from scipy.optimize import minimize_scalar
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
from scipy.optimize import fsolve
from fonctions import (
    F,G,H
)

def df_from_minimize_methods(functions: list, export_excel: bool = False) -> None:

    """
    Fonction pour creer un DataFrame avec les valeurs des fonctions minimisée par les differentes methodes d'optimisation

    Args:
        functions (list): Liste des fonctions a minimiser
        export_excel (bool, optional): Exporter le DataFrame dans un fichier Excel. Defaults to False.
    """

    # Définition des méthodes d'optimisation
    methods = ['bounded', 'brent', 'golden']
    # Initialisation d'un dictionnaire pour stocker les résultats
    results = {
        'Method': methods,
    }
    
    # Ajout des colonnes pour chaque fonction
    for func in functions:
        results[func.__name__] = []

    # Boucle sur les méthodes
    for method in methods:
        # Boucle sur les fonctions
        for func in functions:
            if method == 'bounded':
                result = minimize_scalar(func, bounds=(-10, 10), method=method)
            else:
                result = minimize_scalar(func, method=method, tol=1e-10)
            
            # Ajout du résultat au dictionnaire
            results[func.__name__].append(result.x)

    df = pd.DataFrame(results)
    df.set_index('Method', inplace=True)  

    print("DataFrame:", df)

    if export_excel:
        df.to_excel('methodes_optimisation_scipy.xlsx')
        print("DataFrame exporté vers 'methodes_optimisation_scipy.xlsx' avec succès!")


def golden_section_search(f: callable, a: float, b : float, tol=1e-10) -> tuple:
    """
    Fonction pour trouver le point minimum d'une fonction par la méthode de la section doree

    Args:
        f (callable): fonction a minimiser
        a (float): borne inf
        b (float): borne sup
        tol (float, optional): tolerance. Defaults to 1e-10.
    """
    evolution = []  # stocker l'évolution du point minimum
    intervals = []  # stocker l'évolution de l'intervalle [a, b]
    iteration = 0
    start_time = time.time()  # Mesurer le temps de début
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
    end_time = time.time()  # Mesurer le temps de fin
    cpu_time = end_time - start_time  # Calculer le temps CPU
    return (b + a) / 2, evolution, intervals, iteration, cpu_time

def create_excel_golden_section_search(functions: dict, a: float, b: float, tol=1e-10) -> None:
    """
    Fonction pour creer un fichier Excel avec les resultats de la recherche par la méthode de la section doree

    Args:
        functions (dict): dictionnaire des fonctions a minimiser
        a (float): borne inf
        b (float): borne sup
        tol (float, optional): tolerance. Defaults to 1e-10.
    """
    results = {}
    for name, f in functions.items():
        result, _, _, iteration, cpu_time = golden_section_search(f, a, b, tol)
        results[name] = {'Point Minimum': result, 'Nombre d\'itération': iteration, 'Temps CPU': cpu_time}
    df = pd.DataFrame(results).transpose()
    df.to_excel('golden_section_search_results.xlsx')
    print("Le fichier Excel des résultats a été créé avec succès.")

def visualize_golden_section_search(f: callable, a: float, b:float) -> None:
    """
    Fonction pour visualiser l'evolution de l'intervalle [a, b] par la méthode de la section doree

    Args:
        f (callable): fonction a minimiser
        a (float): borne inf
        b (float): borne sup
    """
    # Calculer la recherche par section dorée pour chaque point minimum
    section_dooree, evolution, intervals_golden, iteration, cpu_time= golden_section_search(f, a, b)

    # Définir les itérations spécifiques pour le tracé
    specific_iterations = [1, 10, 20, 30, iteration]  # Spécifier les itérations spécifiques

    # Tracer la fonction originale f(x) avec l'évolution de l'intervalle [a, b] pour des itérations spécifiques
    x_values = np.linspace(a, b, 1000)

    # Créer les sous-graphiques
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))

    # Premier sous-graphique: Vue générale de la recherche autour du minimum de la méthode de la section dorée
    ax1 = axes[0,0]
    ax1.plot(x_values, f(x_values), label=f'{f.__name__}(x)')
    for i, interval in enumerate(intervals_golden):
        if i + 1 in specific_iterations:
            ax1.plot(interval, [f(interval[0]), f(interval[1])], 'o-', label=f'Itération {i+1}')
    ax1.set_xlabel('x')
    ax1.set_ylabel(f'{f.__name__}(x)')
    ax1.set_title(f'Recherche par la section dorée autour du minimum pour {f.__name__}(x)')
    ax1.legend()
    ax1.grid(True)

    # Deuxième sous-graphique: Vue zoomée autour du minimum de la méthode de la section dorée
    ax2 = axes[0,1]
    ax2.plot(x_values, f(x_values), label=f'{f.__name__}(x)')
    for i, interval in enumerate(intervals_golden):
        if i + 1 in specific_iterations:
            ax2.plot(interval, [f(interval[0]), f(interval[1])], 'o-', label=f'Itération {i+1}')
    ax2.set_xlabel('x')
    ax1.set_ylabel(f'{f.__name__}(x)')
    ax2.set_title(f'Zoom près du minimum à 1e-1')
    ax2.legend()
    ax2.grid(True)
    ax2.set_xlim(section_dooree - 0.1, section_dooree + 0.1)  # Zoom près du minimum
    ax2.set_ylim(f(section_dooree) - 0.1, f(section_dooree) + 0.1)

    # Troisième sous-graphique: Vue encore plus zoomée autour du minimum de la méthode de la section dorée
    ax3 = axes[1,0]
    ax3.plot(x_values, f(x_values), label=f'{f.__name__}(x)')
    for i, interval in enumerate(intervals_golden):
        if i + 1 in specific_iterations:
            ax3.plot(interval, [f(interval[0]), f(interval[1])], 'o-', label=f'Itération {i+1}')
    ax3.set_xlabel('x')
    ax1.set_ylabel(f'{f.__name__}(x)')
    ax3.set_title(f'Zoom encore plus près du minimum à 1e-3')
    ax3.legend()
    ax3.grid(True)
    ax3.set_xlim(section_dooree - 1e-3, section_dooree + 1e-3)  # Zoom encore plus près du minimum
    ax3.set_ylim(f(section_dooree) - 1e-3, f(section_dooree) + 1e-3)

    # Quatrième sous-graphique: Vue extrêmement zoomée autour du minimum de la méthode de la section dorée
    ax4 = axes[1,1]
    ax4.plot(x_values, f(x_values), label=f'{f.__name__}(x)')
    for i, interval in enumerate(intervals_golden):
        if i + 1 in specific_iterations:
            ax4.plot(interval, [f(interval[0]), f(interval[1])], 'o-', label=f'Itération {i+1}')
    ax4.set_xlabel('x')
    ax1.set_ylabel(f'{f.__name__}(x)')
    ax4.set_title(f'Zoom extrêmement près du minimum à 1e-8')
    ax4.legend()
    ax4.grid(True)
    ax4.set_xlim(section_dooree - 1e-8, section_dooree + 1e-8)  # Zoom extrêmement près du minimum
    ax4.set_ylim(f(section_dooree) - 1e-8, f(section_dooree) + 1e-8)

    plt.tight_layout()
    plt.show()

def method_newton(dF: callable, d2F: callable, x0: float, epsilon=1e-6, max_iter=100):
    """
    Fonction pour trouver le point minimum d'une fonction par la méthode de la section doree

    Args:
        f (callable): fonction a minimiser
        a (float): borne inf
        b (float): borne sup
        tol (float, optional): tolerance. Defaults to 1e-10.
    """
    x = x0
    iter_count = 0
    while abs(dF(x)) > epsilon and iter_count < max_iter:
        x -= dF(x) / d2F(x)
        iter_count += 1
    if iter_count == max_iter:
        print("La méthode de Newton n'a pas convergé.")
    print("Itteration Newton", iter_count)
    return x

def method_newton(dF: callable, d2F: callable, x0: float, epsilon=1e-6, max_iter=100) -> tuple:
    """
    Fonction pour trouver le point minimum d'une fonction par la méthode de Newton.

    Args:
        dF (callable): Dérivée première de la fonction.
        d2F (callable): Dérivée seconde de la fonction.
        x0 (float): Point initial.
        epsilon (float, optional): Tolérance pour la convergence. Defaults to 1e-6.
        max_iter (int, optional): Nombre maximum d'itérations. Defaults to 100.

    Returns:
        tuple: Un tuple contenant le point minimum trouvé, le nombre d'itérations effectuées et le temps CPU utilisé.
    """
    start_time = time.time()
    x = x0
    iter_count = 0
    while abs(dF(x)) > epsilon and iter_count < max_iter:
        x -= dF(x) / d2F(x)
        iter_count += 1
    end_time = time.time()
    cpu_time = end_time - start_time
    if iter_count == max_iter:
        print("La méthode de Newton n'a pas convergé.")
    return x, iter_count, cpu_time


def plot_newton_method(F: callable,dF: callable,d2F: callable, x0: float) -> None:
    """
    Fonction pour tracer la fonction et le point minimum par la méthode de la section doree
    Args :
        F (callable): fonction a minimiser
        dF (callable): derivee de la fonction
        d2F (callable): derivee seconde de la fonction
        x0 (float): point initial
    """
    # Perform Newton's method
    x_k, _, _ = method_newton(dF, d2F, x0)

    # Plot the function
    x_values = np.linspace(x0+1, x_k - 0.5, 100)
    plt.plot(x_values, F(x_values))
    plt.scatter(x0, F(x0), color='red')
    plt.scatter(x_k, F(x_k), color='red')

    # Annotate the minimum point
    plt.annotate('x_k initial', xy=(x0, F(x0)), xytext=(-3, 30), textcoords='offset points', arrowprops=dict(arrowstyle='->', color='red'))
    plt.annotate('x_k final (minimum global)', xy=(x_k, F(x_k)), xytext=(-3, 30), textcoords='offset points', arrowprops=dict(arrowstyle='->', color='red'))

    plt.xlabel('x')
    plt.ylabel(f'{F.__name__}(x)')
    plt.ylim(F(x_k)-0.5, F(x0)+0.5)
    plt.title(f'Méthode de Newton pour la fonction {F.__name__}(x)')
    plt.grid(True)
    plt.show()

def method_quasi_newton(dF: callable, x0: float, epsilon=1e-6, max_iter=100) -> tuple:
    """
    Fonction pour trouver le point minimum d'une fonction par la méthode de la section doree

    Args:
        f (callable): fonction a minimiser
        a (float): borne inf
        b (float): borne sup
        tol (float, optional): tolerance. Defaults to 1e-10.
    """
    start_time = time.time()
    x = x0
    x_prev = x0 - epsilon 
    iter_count = 0
    while abs(dF(x)) > epsilon and iter_count < max_iter:
        dF_approx = (dF(x) - dF(x_prev)) / (x - x_prev) 
        x -= dF(x) / dF_approx 
        x, x_prev = x - dF(x) / dF_approx, x  
        iter_count += 1
    end_time = time.time()
    cpu_time = end_time - start_time
    if iter_count == max_iter:
        print("La méthode quasi-Newton n'a pas convergé.")
    return x, iter_count, cpu_time  # Returning both the result, the iteration count, and the CPU time

def compare_newton_with_quasi_newton(functions: dict, derivatives: dict, second_derivatives, x0_values, epsilon=1e-6, max_iter=100, export_excel=False):
    results = {}
    for name in functions:
        x_newton, iter_newton, cpu_time_newton = method_newton(derivatives[name], second_derivatives[name], x0_values[name], epsilon, max_iter)
        x_quasi, iter_quasi, cpu_time_quasi = method_quasi_newton(derivatives[name], x0_values[name], epsilon, max_iter)
        results[name] = {'x_newton': x_newton, 'iter_newton': iter_newton, 'cpu_time_newton': cpu_time_newton,
                         'x_quasi_newton': x_quasi, 'iter_quasi_newton': iter_quasi, 'cpu_time_quasi_newton': cpu_time_quasi}
    df = pd.DataFrame(results)
    if export_excel:
        df.to_excel('compare_newton_with_quasi_newton.xlsx')
    print(df)


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

def quadratic_interpolation(points):
    n = len(points)
    if n != 3:
        raise ValueError("Quadratic interpolation requires exactly 3 data points")

    A = np.array([[point**2, point, 1] for point, _ in points])
    b = np.array([y for _, y in points])

    u = np.linalg.solve(A, b)

    def f(t):
        return u[0]*t**2 + u[1]*t + u[2]

    return f

def find_roots(interp_func, initial_guess=0):
    root = fsolve(interp_func, initial_guess)
    return root

def plot_functions(f,data_points, interp_func):
    x_values = np.linspace(-40, 50, 1000)
    y_original_values = [f(x) for x in x_values]
    y_interp_values = [interp_func(x) for x in x_values]

    plt.plot(x_values, y_original_values, label='Original Function')
    plt.plot(x_values, y_interp_values, label='Interpolation')

    roots = find_roots(interp_func, initial_guess=-0.1)
    print("Roots of Interpolation:", roots)
    plt.plot(roots, np.zeros_like(roots), 'ro', label='Roots of Interpolation')

    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Quadratic Interpolation vs. Original Function')
    plt.grid(True)
    plt.legend()
    plt.show()