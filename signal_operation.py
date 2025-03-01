import numpy as np
import matplotlib.pyplot as plt

# Define a sample discrete signal
n = np.arange(-10, 11)
x = np.sin(0.2 * np.pi * n)
y = np.cos(0.2 * np.pi * n)

# 1. Signal Addition
addition = x + y

# 2. Signal Shifting
shift = 3  # Shift by 3 units to the right
shifted_signal = np.roll(x, shift)

# 3. Signal Folding
folded_signal = x[::-1]

# 4. Signal Multiplication
multiplication = x * y

# Plotting results
plt.figure(figsize=(10, 8))

plt.subplot(2, 2, 1)
plt.stem(n, addition, basefmt=" ")
plt.title("Signal Addition")
plt.xlabel("n")
plt.ylabel("Amplitude")

plt.subplot(2, 2, 2)
plt.stem(n, shifted_signal, basefmt=" ")
plt.title("Signal Shifting (Right by 3)")
plt.xlabel("n")
plt.ylabel("Amplitude")

plt.subplot(2, 2, 3)
plt.stem(n, folded_signal, basefmt=" ")
plt.title("Signal Folding")
plt.xlabel("n")
plt.ylabel("Amplitude")

plt.subplot(2, 2, 4)
plt.stem(n, multiplication, basefmt=" ")
plt.title("Signal Multiplication")
plt.xlabel("n")
plt.ylabel("Amplitude")

plt.tight_layout()
plt.show()