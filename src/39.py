import numpy as np
from scipy.optimize import minimize

def f(x):
    return x[0]**2 + 3*x[1] - 5

initial_guess = [2, 3]
result = minimize(f, initial_guess)
print("Optimized value:", result.fun)
print("Optimized solution:", result.x)
