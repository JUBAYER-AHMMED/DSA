import numpy as np
import matplotlib.pyplot as plt

# Define x(n)
n = np.arange(-6, 7)  # n ranges from -6 to 6
x_n = np.array([1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1])  # x(n) values

# Define the range of n for Y(n)
n_Y = np.arange(-10, 11)  # n ranges from -10 to 10 (to accommodate shifts)

# Initialize Y(n) with zeros
Y_n = np.zeros_like(n_Y, dtype=float)

# Initialize components for shifting and scaling
x_n_minus_5 = np.zeros_like(n_Y, dtype=float)  # x(n-5)
x_n_plus_4 = np.zeros_like(n_Y, dtype=float)  # x(n+4)
scaled_x_n_minus_5 = np.zeros_like(n_Y, dtype=float)  # 2x(n-5)
scaled_x_n_plus_4 = np.zeros_like(n_Y, dtype=float)  # 3x(n+4)
folded_x_n_plus_4 = np.zeros_like(n_Y, dtype=float)  # -3x(n+4)

# Compute the components
for i, n_val in enumerate(n_Y):
    # Compute x(n-5)
    if (n_val - 5) in n:  # Check if n-5 is within the original range of x(n)
        x_n_minus_5[i] = x_n[np.where(n == n_val - 5)[0][0]]
        scaled_x_n_minus_5[i] = 2 * x_n_minus_5[i]  # Scale by 2

    # Compute x(n+4)
    if (n_val + 4) in n:  # Check if n+4 is within the original range of x(n)
        x_n_plus_4[i] = x_n[np.where(n == n_val + 4)[0][0]]
        scaled_x_n_plus_4[i] = 3 * x_n_plus_4[i]  # Scale by 3
        folded_x_n_plus_4[i] = -3 * x_n_plus_4[i]  # Fold and scale by -3

# Compute Y(n) = 2x(n-5) - 3x(n+4)
Y_n = scaled_x_n_minus_5 + folded_x_n_plus_4

# Create a figure with subplots
plt.figure(figsize=(10, 8))

# Plot 1: Input Signal x(n)
plt.subplot(4, 2, 1)
plt.stem(n, x_n, basefmt=" ", linefmt="blue", markerfmt="bo", label="x(n)")
plt.title("Input Signal: x(n)")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()
plt.xticks(n)

# Plot 2: Shifting x(n) to x(n-5)
plt.subplot(4, 2, 2)
plt.stem(n_Y, x_n_minus_5, basefmt=" ", linefmt="green", markerfmt="go", label="x(n-5)")
plt.title("Shifting: x(n-5)")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()
plt.xticks(n_Y)

# Plot 3: Shifting x(n) to x(n+4)
plt.subplot(4, 2, 3)
plt.stem(n_Y, x_n_plus_4, basefmt=" ", linefmt="red", markerfmt="ro", label="x(n+4)")
plt.title("Shifting: x(n+4)")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()
plt.xticks(n_Y)

# Plot 4: Scaling x(n-5) to 2x(n-5)
plt.subplot(4, 2, 4)
plt.stem(n_Y, scaled_x_n_minus_5, basefmt=" ", linefmt="purple", markerfmt="mo", label="2x(n-5)")
plt.title("Scaling: 2x(n-5)")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()
plt.xticks(n_Y)

# Plot 5: Scaling x(n+4) to 3x(n+4)
plt.subplot(4, 2, 5)
plt.stem(n_Y, scaled_x_n_plus_4, basefmt=" ", linefmt="orange", markerfmt="co", label="3x(n+4)")
plt.title("Scaling: 3x(n+4)")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()
plt.xticks(n_Y)

# Plot 6: Folding 3x(n+4) to -3x(n+4)
plt.subplot(4, 2, 6)
plt.stem(n_Y, folded_x_n_plus_4, basefmt=" ", linefmt="brown", markerfmt="yo", label="-3x(n+4)")
plt.title("Folding: -3x(n+4)")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()
plt.xticks(n_Y)

# Plot 7: Final Result Y(n) = 2x(n-5) - 3x(n+4)
plt.subplot(4, 2, 7)
plt.stem(n_Y, Y_n, basefmt=" ", linefmt="black", markerfmt="ko", label="Y(n) = 2x(n-5) - 3x(n+4)")
plt.title("Final Result: Y(n) = 2x(n-5) - 3x(n+4)")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()
plt.xticks(n_Y)

plt.tight_layout()
plt.show()