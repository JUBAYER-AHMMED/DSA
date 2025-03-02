import numpy as np
import matplotlib.pyplot as plt

# Define signal operations
def signal_addition(x1, x2):
    return x1 + x2

def signal_multiplication(x1, x2):
    return x1 * x2

def signal_scaling(x, alpha):
    return alpha * x

def signal_shifting(n, shift):
    return n + shift

def signal_folding(x):
    return np.flip(x)

# Define input signals and time axis
n = np.array([-2, -1, 0, 1, 2])
x1 = np.array([1, 2, 3, 4, 5])
x2 = np.array([5, 4, 3, 2, 1])

# Perform signal operations
added_signal = signal_addition(x1, x2)
multiplied_signal = signal_multiplication(x1, x2)
scaled_signal = signal_scaling(x1, 2)
shifted_signal1 = signal_shifting(n, -2)
shifted_signal2 = signal_shifting(n, 2)
folded_signal = signal_folding(x1)

# Plot the results
plt.figure(figsize=(10, 8))

plt.subplot(4, 2, 1)
plt.stem(n, x1)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Original Signal x1")
plt.grid()

plt.subplot(4, 2, 2)
plt.stem(n, x2)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Original Signal x2")
plt.grid()

plt.subplot(4, 2, 3)
plt.stem(n, added_signal)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Signal Addition")
plt.grid()

plt.subplot(4, 2, 4)
plt.stem(n, multiplied_signal)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Signal Multiplication")
plt.grid()

plt.subplot(4, 2, 5)
plt.stem(n, scaled_signal)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Scaled Signal (x1 * 2)")
plt.grid()

plt.subplot(4, 2, 6)
plt.stem(shifted_signal1, x1)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Shifted Signal (Shift = -2)")
plt.grid()

plt.subplot(4, 2, 7)
plt.stem(shifted_signal2, x1)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Shifted Signal (Shift = +2)")
plt.grid()

plt.subplot(4, 2, 8)
plt.stem(n, folded_signal)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Folded Signal (x1)")
plt.grid()

plt.tight_layout()
plt.show()