import math

w = float(input('w : ')) 
i = float(input('i : '))  
e = float(input('e : '))
la = float(input('la : '))
L0 = float(input('L0 : '))
rayon_terrestre = float(input('rayon_terrestre : '))
mu = float(input('mu : '))
a = float(input('a : '))

v_angles_input = input("Enter comma-separated angles in degrees: ")
v_angles = [float(s.strip()) for s in v_angles_input.split(',')]

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
    
    if -w_rad - math.radians(90) <= v_rad <= -w_rad + math.radians(90):
        L0 = math.degrees(math.asin(math.tan(la_rad) / math.tan(i_rad)))
    elif v_rad < -w_rad - math.radians(90):
        L0 = -180 - math.degrees(math.asin(math.tan(la_rad) / math.tan(i_rad)))
    else:
        L0 = 180 - math.degrees(math.asin(math.tan(la_rad) / math.tan(i_rad)))
    
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
print('r_a =>', r_a)
print('r_p =>', r_p)


z_a = r_a - rayon_terrestre 
z_p = r_p - rayon_terrestre 
print('z_a =>', z_a)
print('z_p =>', z_p)

T = 2*math.pi*math.sqrt(a**3/mu)
print('Période T =>',T)

V_P = (((2*mu)/r_p) - (mu/a))**0.5
V_A = (r_p*V_P)/r_a 
print("Vitesse au periapsis:", round(V_P,2), "km/s")

V_A = (r_p*V_P)/r_a #0.95
print("Vitesse à l'apoapsis:", round(V_A,2), "km/s")

v_c = math.acos(-e)
print('v_c =>',v_c )
tp = calculate_time(v=-w,periapsis=True)
print('Temps à periapsis =>',tp)


t = []

for j in v_angles:
    t.append( calculate_time(v=j) + tp )

print("Temps =>",t)


la = []


for index, v in enumerate(v_angles):
    result_la = calculate_la(v)
    la.append(result_la)

print('la =>',la )

L0 = []

for index, v in enumerate(v_angles):
    result_la = calculate_la(v)
    result_L0 = calculate_L0(result_la, i, w, v)
    L0.append(result_L0)

print('l0 =>',L0 )