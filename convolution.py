import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve

# Function to compute convolution
def compute_convolution(signal1, signal2):
    conv_result = convolve(signal1, signal2, mode='full', method='auto')
    return conv_result

# Define parameters
fs = 1000  
t = np.linspace(0, 1, fs, endpoint=False)  
freq = 5  
sin_signal = np.sin(2 * np.pi * freq * t)

# Compute autoconvolution
conv_auto = compute_convolution(sin_signal, sin_signal)

# Compute convolution between original and shifted signal
signal1 = sin_signal
signal2 = np.roll(signal1, 100)  
conv_shifted = compute_convolution(signal1, signal2)

# Compute convolution with a noisy signal
noise = np.random.normal(0, 0.5, fs)
noisy_signal = signal1 + noise
conv_noisy = compute_convolution(signal1, noisy_signal)

# Plot results
plt.figure(figsize=(10, 8))

plt.subplot(3, 1, 1)
plt.plot(conv_auto)
plt.title("Autoconvolution of a Sinusoidal Signal")
plt.xlabel("Samples")
plt.ylabel("Convolution Output")
plt.grid()

plt.subplot(3, 1, 2)
plt.plot(conv_shifted)
plt.title("Convolution between Signal and Shifted Version")
plt.xlabel("Samples")
plt.ylabel("Convolution Output")
plt.grid()

plt.subplot(3, 1, 3)
plt.plot(conv_noisy)
plt.title("Convolution with Noisy Signal")
plt.xlabel("Samples")
plt.ylabel("Convolution Output")
plt.grid()

plt.tight_layout()
plt.show()