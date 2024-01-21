T_a = float(input("Température de l'air (T_a) en °C : "))
T_s = float(input("Température de la surface (T_s) en °C : "))
viscosite = float(input("Viscosité (en m^2/s) : "))
masse_vol = float(input("Masse volumique (en kg/m^3) : "))
conductivite = float(input("Conductivité thermique (en W/(m°C)) : "))
capacite_calorifique = float(input("Capacité calorifique (en J/(kg°C)) : "))
hauteur_de_mur = float(input("Hauteur du mur (en m) (grand L) : "))
longeur_du_mur = float(input("Longueur du mur (en m) : "))

coefficient_de_dilatation = 1/(273+(T_a+T_s))

print('\n')

Pr = (viscosite*capacite_calorifique)/conductivite
print("Nombre de Prandtl (Pr) : ",round(Pr,3))

Gr = (9.81*coefficient_de_dilatation*abs(T_a - T_s)*hauteur_de_mur**3*masse_vol**2)/viscosite**2
formatted_Gr = "{:.2e}".format(Gr)
print("Nombre de Grashoff (Gr) : ", formatted_Gr)

Ra = Pr*Gr
print(f'Nombre de Rayleigh (Ra) : {Ra:.2e}')

Nu = (0.825 + (0.387*Ra**(1/6))/(1+(0.492/Pr)**(9/16))**(8/27))**2
print("Nombre de Nusselt (Nu) : ",round(Nu,3))

h = (Nu*conductivite)/hauteur_de_mur 
print("Coefficient d’échange par convection h : ",round(h,3), '(W/m^2 C°)')

"""
Déterminer le flux de chaleur perdu par l’air si la longueur du mur est l = 5m.
"""

surface = hauteur_de_mur * longeur_du_mur
phi = h*surface*(T_a - T_s)

print('Flux perdu par l’air ',round(phi,2), '(W)')