import numpy as np
import matplotlib.pyplot as plt

# Parameters
N = 64  # Number of samples
fs = 100  # Sampling frequency (Hz)
n = np.arange(N)  # Time indices

# Define the input signal
A_dc = 0.5  # DC component
A1, f1 = 1.0, 5.0  # Amplitude and frequency of the first sinusoid
A2, f2 = 0.8, 15.0  # Amplitude and frequency of the second sinusoid

# Input signal: x(n) = A_dc + A1 * sin(2*pi*f1*n/fs) + A2 * sin(2*pi*f2*n/fs)
x = A_dc + A1 * np.sin(2 * np.pi * f1 * n / fs) + A2 * np.sin(2 * np.pi * f2 * n / fs)

# DFT Implementation
def DFT(x):
    N = len(x)
    X = np.zeros(N, dtype=complex)
    for k in range(N):
        for n in range(N):
            X[k] += x[n] * np.exp(-2j * np.pi * k * n / N)
    return X

# IDFT Implementation
def IDFT(X):
    N = len(X)
    x = np.zeros(N, dtype=complex)
    for n in range(N):
        for k in range(N):
            x[n] += X[k] * np.exp(2j * np.pi * k * n / N)
        x[n] /= N  # Normalize by N
    return x

# Compute DFT
X = DFT(x)

# Compute IDFT (reconstruct signal)
x_reconstructed = IDFT(X)

# Frequency bins
frequencies = np.fft.fftfreq(N, d=1/fs)

# Print results
print("Original Signal (x):", x)
print("DFT (X):", X)
print("Reconstructed Signal (x_reconstructed):", x_reconstructed.real)  # Should match x
print("Frequency Bins (frequencies):", frequencies)

# Plot 1: Input Signal
plt.figure(figsize=(10, 4))
plt.plot(n, x, "b-", label="Input Signal")
plt.title("Input Signal (x(n))")
plt.xlabel("Time (n)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()
plt.show()

# Plot 2: DFT of the Signal (Magnitude)
plt.figure(figsize=(10, 4))
plt.stem(frequencies, np.abs(X), basefmt=" ", linefmt="green", markerfmt="go", label="Magnitude of DFT")
plt.title("Magnitude of DFT (|X(k)|)")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.grid(True)
plt.legend()
plt.show()

# Plot 3: Reconstructed Signal after IDFT
plt.figure(figsize=(10, 4))
plt.plot(n, x_reconstructed.real, "r-", label="Reconstructed Signal")
plt.title("Reconstructed Signal after IDFT (x_reconstructed(n))")
plt.xlabel("Time (n)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()
plt.show()