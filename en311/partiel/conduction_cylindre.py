"""

Une conduite cylindrique d’une centrale énergétique en acier de conductivité 𝝀a de rayon interne ri et de rayon externe re de longueur L canalise de la vapeur surchauffée. 

On appellera hi le coefficient de convection interne et Si la surface d’échange correspondante. 

On isole cette conduite au moyen d’un isolant de forme cylindrique de conductivité 𝝀i d’épaisseur e. 

On appellera he le coefficient de convection externe et Se la surface d’échange correspondante.  

"""

import math

L = 1
ri = 6e-3  # (m)
re = 7e-3  # (m)

e_values_mm = [i for i in range(5)]

hi = 200  # (W/m^2 C°)
Si = 2 * math.pi * L * ri

he = 10
conductivity_steel = 15  # (W/m C°)
conductivity_isolation = 0.1


resistance_internal_convection = []
resistance_external_convection = []
resistance_conduction_steel = []
resistance_conduction_insulation = []
resistance_totale = []


for e_mm in e_values_mm:
    e = e_mm / 1000  
    Se = 2 * math.pi * L * (re + e)


    resistance_internal_convection.append(1 / (hi * Si))
    resistance_external_convection.append(1 / (he * Se))
    resistance_conduction_steel.append((1 / (2 * math.pi * L * conductivity_steel)) * math.log(re / ri))
    resistance_conduction_insulation.append((1 / (2 * math.pi * L * conductivity_isolation)) * math.log((re + e) / re))
    

    total_resistance = (
        resistance_internal_convection[-1] +
        resistance_external_convection[-1] +
        resistance_conduction_steel[-1] +
        resistance_conduction_insulation[-1]
    )
    
    resistance_totale.append(total_resistance)


print("\nResults:")
print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(
    "Epaisseur e", "Rconv_in (°C/W)", "Rconv_ex (°C/W)", "Rcond_ac (°C/W)", "Rcond_is (°C/W)", "Rtotale (°C/W)"
))

for i, e_value_mm in enumerate(e_values_mm):
    print("{:<15} {:<15.3e} {:<15.3e} {:<15.3e} {:<15.3e} {:<15.3e}".format(
        e_value_mm,
        resistance_internal_convection[i],
        resistance_external_convection[i],
        resistance_conduction_steel[i],
        resistance_conduction_insulation[i],
        resistance_totale[i]
    ))
