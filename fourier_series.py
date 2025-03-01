import numpy as np
import matplotlib.pyplot as plt

# Fourier Series Approximation Function
def fourier_series(x, terms):
    if terms < 1:
        raise ValueError("Number of terms must be at least 1")
    
    result = np.zeros_like(x)  # Initialize result with zeros

    for n in range(1, terms + 1, 2):  # Iterate over odd numbers (1, 3, 5,...)
        result += (4 / (np.pi * n)) * np.sin(n * x)  # Fourier series formula

    return result

# Define the Original Square Wave Function
def square_wave(x):
    return np.where(np.sin(x) >= 0, 1, -1)  # Generates a square wave

# Generate X Values
t = np.linspace(-np.pi, np.pi, 400)

# Plot the Approximations
plt.figure(figsize=(8, 6))

# Plot the Original Square Wave
plt.plot(t, square_wave(t), label='Original Square Wave', linestyle='--', color='black')

# Plot Fourier Series Approximations with Different Terms
for terms in [1, 3, 5, 9]:
    plt.plot(t, fourier_series(t, terms), label=f'{terms} terms')

# Add Grid and Labels
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.title('Fourier Series Approximation of a Square Wave')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)

# Show the Plot
plt.show()