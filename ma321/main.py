from scipy.optimize import minimize_scalar
import matplotlib.pyplot as plt
import numpy as np

#------------------------------Qestion 1-----------------------------

def F(x):
    return x**4 + 8*x**3 + 24*x**2 + 32*x + 17

# deux méthodes possibles : bounded et golden.
result_bounded = minimize_scalar(F, method='bounded', bounds=(-100, 100), tol=1e-10)
result_golden = minimize_scalar(F, method='golden', tol=1e-10)

print("Minimum trouvé avec la méthode bounded:", result_bounded.x)
print("Minimum trouvé avec la méthode golden:", result_golden.x)

x = np.linspace(-100, 100, 1000)

plt.plot(x,F(x))
plt.show()
#------------------------------Qestion 2-----------------------------

