import numpy as np
import matplotlib.pyplot as plt
# Define the unit step signal
def unit_step(n):
    return np.where(n >= 0, 1, 0)

# Define the range of n
n = np.arange(-5, 6)  # From -5 to 5

# Generate the unit step signal
u = unit_step(n)

# Plot the unit step signal
plt.stem(n, u, basefmt=" ")
plt.title("Unit Step Signal")
plt.xlabel("n")
plt.ylabel("u[n]")
plt.grid(True)
plt.show()