import numpy as np
import matplotlib.pyplot as plt

# Define x(n) with index 5 as the origin
x = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1]
n = np.arange(-5, 8)  # Index range from -5 to 7

# Compute Y(n) = 2x(n-5) - 3x(n+4)
Y = np.zeros_like(x, dtype=float)
for i in range(len(n)):
    n_minus_5 = i - 5
    n_plus_4 = i + 4
    x_n_minus_5 = x[n_minus_5] if 0 <= n_minus_5 < len(x) else 0
    x_n_plus_4 = x[n_plus_4] if 0 <= n_plus_4 < len(x) else 0
    Y[i] = 2 * x_n_minus_5 - 3 * x_n_plus_4

# Plot x(n)
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.stem(n, x, basefmt="b")
plt.title('Input Signal x(n)')
plt.xlabel('n')
plt.ylabel('x(n)')
plt.grid()

# Plot Y(n)
plt.subplot(2, 1, 2)
plt.stem(n, Y, basefmt="r")
plt.title('Output Signal Y(n) = 2x(n-5) - 3x(n+4)')
plt.xlabel('n')
plt.ylabel('Y(n)')
plt.grid()

plt.tight_layout()
plt.show()
