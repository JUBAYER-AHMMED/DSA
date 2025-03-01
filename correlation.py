import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import correlate, correlation_lags

# Function to compute autocorrelation
def compute_autocorrelation(signal):
    auto_corr = correlate(signal, signal, mode='full', method='auto')
    lags = correlation_lags(len(signal), len(signal), mode='full')
    return auto_corr, lags

# Function to compute cross-correlation
def compute_cross_correlation(signal1, signal2):
    cross_corr = correlate(signal1, signal2, mode='full', method='auto')
    lags = correlation_lags(len(signal1), len(signal2), mode='full')
    return cross_corr, lags

# Define parameters
fs = 1000  
t = np.linspace(0, 1, fs, endpoint=False)  
freq = 5  
sin_signal = np.sin(2 * np.pi * freq * t)

# Compute autocorrelation
auto_corr, lags_auto = compute_autocorrelation(sin_signal)

# Compute cross-correlation between original and shifted signal
signal1 = sin_signal
signal2 = np.roll(signal1, 100)  
cross_corr, lags_cross = compute_cross_correlation(signal1, signal2)

# Compute cross-correlation with a noisy signal
noise = np.random.normal(0, 0.5, fs)
noisy_signal = signal1 + noise
cross_corr_noise, lags_noise = compute_cross_correlation(signal1, noisy_signal)

# Plot results
plt.figure(figsize=(10, 8))

plt.subplot(3, 1, 1)
plt.plot(lags_auto, auto_corr)
plt.title("Autocorrelation of a Sinusoidal Signal")
plt.xlabel("Lag")
plt.ylabel("Autocorrelation")
plt.grid()

plt.subplot(3, 1, 2)
plt.plot(lags_cross, cross_corr)
plt.title("Cross-Correlation between Two Signals")
plt.xlabel("Lag")
plt.ylabel("Cross-Correlation")
plt.grid()

plt.subplot(3, 1, 3)
plt.plot(lags_noise, cross_corr_noise)
plt.title("Cross-Correlation with Noisy Signal")
plt.xlabel("Lag")
plt.ylabel("Cross-Correlation")
plt.grid()

plt.tight_layout()
plt.show()