import numpy as np
from scipy.integrate import quad

# Define the function to decompose (Example: Square Wave)
def f(x):
    return np.where(np.sin(x) >= 0, 1, -1)  # Square wave function

# Fourier Series Coefficients Calculation
def fourier_coefficients(f, T, N):
    L = T / 2  # Half period
    a0 = (1 / L) * quad(lambda x: f(x), -L, L)[0]  # Compute a0
    
    an = np.zeros(N)
    bn = np.zeros(N)
    for n in range(1, N + 1):
        an[n-1] = (1 / L) * quad(lambda x: f(x) * np.cos(n * np.pi * x / L), -L, L)[0]
        bn[n-1] = (1 / L) * quad(lambda x: f(x) * np.sin(n * np.pi * x / L), -L, L)[0]
    
    return a0, an, bn

# Parameters
T = 2 * np.pi  # Period of the function
N = 10  # Number of terms

# Compute Fourier Coefficients
a0, an, bn = fourier_coefficients(f, T, N)

# Display Fourier Coefficients
np.set_printoptions(precision=5, suppress=True)  # Format output for readability
print("a0:", a0)
print("an:", an)
print("bn:", bn)
