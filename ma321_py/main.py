from utils import *
from fonctions import *

if __name__ == '__main__':

    functions = [{'F': F, 'G': G, 'H': H}, {'F': dF, 'G': dG, 'H': dH}, {'F': d2F, 'G': d2G, 'H': d2H}]
    x0_values = {'F': 0, 'G': -2.5, 'H': 1}
    a, b = -10, 10

    #--------------Question 1---------------
    print("---------------Question 1---------------\n")
    df_from_minimize_methods(list(functions[0].values()), export_excel=False)  # export_excel = True to export the DataFrame to an Excel file
    print("\n")

    #--------------Question 2---------------
    print("---------------Question 2---------------\n")
    # create_excel_golden_section_search(functions[0], a, b) #pour creer le fichier Excel
    for f_name, f in functions[0].items():
        x_section_doree, _, _, _, _ = golden_section_search(f, a, b)
        print(f"Le point minimum de la fonction {f_name}(x) par le méthode de section doree  : {x_section_doree}")
        # visualize_golden_section_search(f,a,b) #visualiser l'evolution de l'interval par section dorée
    print("\n")

    #--------------Question 3---------------
    print("---------------Question 3---------------\n")
    #compare_newton_with_quasi_newton(functions[0], functions[1], functions[2], x0_values) # comparer le minimum par la methode de newton et par la methode de quasi-newton
    for f_name, (df, d2f) in zip(['F', 'G', 'H'], zip(functions[1].values(), functions[2].values())):
        x_newton, _, _ = method_newton(df, d2f, x0_values[f_name])
        x_quiasi, _, _ = method_quasi_newton(df, x0_values[f_name])
        print(f"Minimum par le méthode de Newton pour la function {f_name}(x): {x_newton}")
        print(f"Minimum per le méthode de quasi-Newton pour la function {f_name}(x): {x_quiasi}")
        #plot_newton_method(functions[0][f_name], df, d2f, x0_values[f_name]) #pour tracer l'evolution de minimum par la methode de newton
    print("\n")


    #--------------Question 4---------------
    print("---------------Question 4---------------\n")
    for f_name, (df, d2f) in zip(['F', 'G', 'H'], zip(functions[1].values(), functions[2].values())):
        x_dekker = dekker(df,a,b)
        print(f"Le point minimum de la fonction {f_name}(x) par la methode de Dekker : {x_dekker}")
    print("\n")

    #--------------Question 5---------------
    # print("---------------Question 5---------------\n")
    # data_points_F = [(-40,  F(-40) ), (50,  F(50)), (15,  F(15))]
    # data_points_G = [(-40,  G(-40) ), (50,  G(50)), (15,  G(15))]
    # data_points_H = [(-40,  H(-40) ), (50,  H(50)), (15,  H(15))]

    # data_points = [data_points_F, data_points_G, data_points_H]

    # for vals,fonc in zip(data_points, [F,G,H]):
    #     interp_func = quadratic_interpolation(vals)
    #     plot_functions(f=fonc,data_points=vals, interp_func=interp_func)
    # print("\n")