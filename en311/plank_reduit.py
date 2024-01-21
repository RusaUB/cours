import numpy as np
import matplotlib.pyplot as plt

# Constants
c = 3e8  # speed of light in meters per second
h = 6.63e-34  # Planck's constant in J·s
k = 1.38e-23  # Boltzmann constant in J/K
b_wien = 2.898e-3  # Wien's constant in meters·K

def plancks_reduit(T, wavelength):
    c1 = 2 * np.pi * h * c**2
    c2 = h * c / k
    wavelength_max = b_wien / T
    x = wavelength / wavelength_max
    betha = c2 / (wavelength_max * T)
    
    B = (c1 * betha**5) / (c2**5 * (np.exp(betha) - 1))

    # Calculate the normalization factor A
    A = (c1 / B) * (betha**5 / c2**5)
    
    # Calculate the Planck's law
    y = (A * x**(-5)) / (np.exp(betha / x) - 1)

    return x, y

# Generate wavelength values
wavelengths = np.linspace(1e-7, 20e-6, 1000)

# Calculate corresponding emissive power using Planck's law
x, emissive_power = plancks_reduit(T=865, wavelength=wavelengths)

# Plot the spectral distribution
plt.plot(x, emissive_power, color='blue')

# Add a horizontal line at y=1 for reference
plt.axhline(y=1, color='red', linestyle='--', label='y=1')
plt.axvline(x=1,color = 'red', linestyle = '--', label = 'x=1')

plt.xlabel('Wavelength (µm)')
plt.ylabel('Emissive Power (Normalized)')
plt.title(f'Spectral Distribution at T = {865} K (reduit)')
plt.grid(True)
plt.legend()
plt.show()
