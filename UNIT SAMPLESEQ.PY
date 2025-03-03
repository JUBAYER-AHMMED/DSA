import numpy as np
import matplotlib.pyplot as plt

# Define the unit sample sequence
def unit_sample(n):
    return np.where(n == 0, 1, 0)

# Define the range of n
n = np.arange(-5, 6)  # From -5 to 5

# Generate the unit sample sequence
delta = unit_sample(n)

# Plot the unit sample sequence
plt.stem(n, delta, basefmt=" ")
plt.title("Unit Sample Sequence (Discrete Delta Function)")
plt.xlabel("n")
plt.ylabel("δ[n]")
plt.grid(True)
plt.show()