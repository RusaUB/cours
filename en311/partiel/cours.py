"""
#################################
Question:
A quelle température faut-il prendre les propriétés physiques et thermique de l air et pourquoi ?
Réponse:
Il faut prendre la température de air à une température moyenne car air n est pas à la même température, il est plus froid proche du mur 10°c et plus chaud loin du mur dans la chambre 20°C. 
T_m = (T_ext + T_int) / 2

#################################
Equation bilan du flux:
Flux absorbé = flux émis ou somme algébrique des flux égale à zéro (quand objet absorbe rien)

Absence de soleil:

Le coefficient de convection à la surface du toit de la voiture est h = 6,0 W/m2 °C.
La température de l environnement est notée tenv= -18°C. 
La température de l air autour du toit de la voiture tair = 5°C. 
La température du toit de la voiture est ttoit. 
L émissivité du toit de la voiture est ε = 0,84. 

#Flux transféré par convection : hS (T_toit - T_aire)
#Flux rayonné entre le toit et l environnement : ε*sigma*S*(T_toit^4 - T_env^4)
#Flux absorbé = flux émis ou somme algébrique des flux égale à zéro. 
# h*S*(T_toit - T_aire) + 𝜺*sigma*S*(T_toit^4 - T_env^4 ) = 0 
#################################

Résistance thermiques de CONDUCTION de l argon :
R(argon) = e/conductivite*S

Résistance thermiques de CONVECTION de l argon :
R(argon) = 1/hS

#################################

Entre la surface de l absorbeur et la vitre, il y a du vide : 

Question  : Que peut-on dire du flux reçu par l absorbeur et du flux émis par l absorbeur ?
Reponse : L absorbeur étant un corps noir, à l équilibre le flux reçu par l absorbeur est égal au flux émis par l’absorbeur.  

Question :  Déterminer la température à l équilibre et la calculer. 
Reponse : M = sigma*T^4 or M = flux solaire arrivant sur le capteur phi = 1000W/m^2

Le bilan thermique de la vitre est donné par :  
alpha_3*phi*3 + alpha_3*sigma*T^4 = 2ε_3*sigma*T_v^4
𝜶𝟑phi_𝟑    Flux incident absorbé par la vitre dans la zone spectrale 3. 
𝜶𝟑𝝈𝑻^4  Flux émis par le corps noir et absorbé par la vitre.  
𝟐𝜺𝟑𝝈𝑻𝑽^𝟒 Flux émis par la vitre sur les deux faces. 

Le bilan thermique de l’absorbeur est donné par :
sigma*T^4 = tau_2*phi_2 + tau_3*phi3 + rho_3*sigma*T^4 + alpha_3*sigma*T_v^4
𝝈𝑻𝟒  Rayonnement émis par l’absorbeur (corps noir).      
tau_𝟐phi_𝟐+tau_𝟑phi_𝟑 Flux absorbé par l’absorbeur en provenance du flux transmis par la vitre 
𝝆𝟑𝝈𝑻𝟒 Rayonnement émis par l’absorbeur et réfléchi par la vitre et absorbé par l’absorbeur. 



"""