import numpy as np

def F(x): 
    return x**4 + 8*x**3 + 24*x**2 + 32*x + 17 
def G(x): 
    return np.sqrt((-2-x)**2+2) 

def H(x): 
    return np.exp(x)-x 

def dF(x): 
    return 4*x**3 + 24*x**2 + 48*x + 32 
def dG(x): 
    return (x + 2)/np.sqrt((-x - 2)**2 + 2) 

def dH(x): 
    return np.exp(x) - 1 
def d2F(x): 
    return 12*(x**2 + 4*x + 4) 
def d2G(x): 
    return (-(x + 2)**2/((x + 2)**2 + 2) + 1)/np.sqrt((x + 2)**2 + 2) 

def d2H(x): 
    return np.exp(x) 