import numpy as np
import matplotlib.pyplot as plt

# Define the n range
n = np.arange(-7, 8)

# Define the sequence X(n)
X_n = 2 * (n == -2) - (n == 4)

# Plotting the sequence
plt.stem(n, X_n)
plt.title('Plot of X(n) = 2delta(n+2) - delta(n-4)')
plt.xlabel('n')
plt.ylabel('X(n)')
plt.grid(True)
plt.xticks(n)  # Show all integer values of n
plt.ylim(-1.5, 2.5)  # Adjust y-axis limits for better visualization
plt.show()
plt.show()
