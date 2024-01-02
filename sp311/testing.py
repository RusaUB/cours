import math

electron = False

rayon_terrestre = 6378
mu = 398600
alpha = 360 / 86164
la = 0

w = 270 if electron else -150
i = 61.00 if electron else 70.20
e = 0.8320  if electron else 0.7990
L_omega = 120 if electron else -51.60
a = 40708 if electron else 87734.00


v_angles = [ i for i in (range(-210,210,30))] if electron else [-200,-160,-120,40,80,160,200]

print(v_angles)

def calculate_la(v):
    v_rad = math.radians(v)
    w_rad = math.radians(w)
    i_rad = math.radians(i)

    la = math.degrees(math.asin(math.sin(w_rad + v_rad) * math.sin(i_rad)))
    return la

def calculate_L0(la, i, w, v):
    la_rad = math.radians(la)
    i_rad = math.radians(i)
    w_rad = math.radians(w)
    v_rad = math.radians(v)
    
    tan_value = math.tan(la_rad) / math.tan(i_rad)

    if -1 <= tan_value <= 1:
        L0 = math.degrees(math.asin(tan_value))
    else:
        if tan_value > 1:
            tan_value = 1
        elif tan_value < -1:
            tan_value = -1
        
        L0 = math.degrees(math.asin(tan_value))


    if -w_rad - math.radians(90) <= v_rad <= -w_rad + math.radians(90):
        pass  
    elif -w_rad - math.radians(450) <= v_rad <= -w_rad - math.radians(270):
        L0 = -360 + L0
    elif -w_rad - math.radians(270) <= v_rad <= -w_rad - math.radians(90):
        L0 = -180 - L0
    elif -w_rad + math.radians(90) <= v_rad <= -w_rad + math.radians(270):
        L0 = 180 - L0
    elif -w_rad + math.radians(270) <= v_rad <= -w_rad + math.radians(450):
        L0 = 360 + L0
    elif -w_rad + math.radians(450) <= v_rad <= -w_rad + math.radians(630):
        L0 = 540 - L0
    else:
        L0 = None
    
    return L0

def calculate_time(v, periapsis=False):
    term1 = -math.sqrt(a**3 / mu) if periapsis else math.sqrt(a**3 / mu)
    term2 = math.asin(math.sqrt(1 - e**2) * math.sin(math.radians(v)) / (1 + e * math.cos(math.radians(v))))
    term3 = e * math.sqrt(1 - e**2) * math.sin(math.radians(v)) / (1 + e * math.cos(math.radians(v)))
    
    v_rad = math.radians(v)

    if -v_c <= v_rad <= v_c:
        t_p = term1 * (term2 - term3)
    
    elif v_c < v_rad < 2*math.pi - v_c:
        t_p = term1 * (math.pi - term2 - term3)
    
    elif v_rad > 2*math.pi - v_c:
        t_p = term1 * (2*math.pi + term2 - term3)
    
    elif -2*math.pi + v_c < v_rad < -v_c:
        t_p = term1 * (-math.pi - term2 - term3)
    
    elif v_rad < -2*math.pi + v_c:
        t_p = term1 * (-2*math.pi + term2 - term3)
    
    return t_p

r_a = a*(1+e) 
r_p = a*(1-e) 

print('\n')
print('r_a =>', r_a)
print('r_p =>', r_p)
print('\n')

z_a = r_a - rayon_terrestre 
z_p = r_p - rayon_terrestre 

print('z_a =>', z_a)
print('z_p =>', z_p)
print('\n')

T = 2*math.pi*math.sqrt(a**3/mu)
print('Période T =>',T)
print('\n')

V_P = (((2*mu)/r_p) - (mu/a))**0.5
V_A = (r_p*V_P)/r_a 
print("Vitesse au periapsis:", round(V_P,2), "km/s")
print('\n')

V_A = (r_p*V_P)/r_a #0.95
print("Vitesse à l'apoapsis:", round(V_A,2), "km/s")
print('\n')

v_c = math.acos(-e)
print('v_c =>',v_c )
tp = calculate_time(v=-w,periapsis=True)
print('Temps à periapsis =>',tp)
print('\n')

print('v=>',v_angles)

t = []

for j in v_angles:
    t.append( round(calculate_time(v=j) + tp,2) )

print("t =>", t)


la = []


for index, v in enumerate(v_angles):
    result_la = calculate_la(v)
    la.append(round(result_la,2))

print('la =>',la )

L0 = [ ]

for index , v in enumerate ( v_angles ) :
    result_la = calculate_la ( v )
    result_L0 = calculate_L0 ( result_la , i , w , v )
    L0.append ( round(result_L0,2) )

print('l0 =>',L0)

Ls = []

for index,l in enumerate(L0) :
    ls = L_omega + l - alpha * t[index]
    Ls.append(round(ls,2))

print('Ls =>',Ls)