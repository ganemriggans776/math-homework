import numpy as np
from scipy.optimize import minimize

def f(x):
    return x**2 - 4*x + 3

result = minimize(f, x0=0)
print("Optimized value:", result.fun)
