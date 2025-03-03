import numpy as np
import matplotlib.pyplot as plt

# Generate a sinusoidal wave
def generate_sin_wave(frequency, duration=1.0, fs=1000):
    t = np.linspace(0, duration, int(fs * duration), endpoint=False)
    signal = np.sin(2 * np.pi * frequency * t)
    return t, signal

# Define different frequencies
frequencies = [5, 10, 20]
duration = 1.0
fs = 1000

# Generate individual sine waves
t1, signal1 = generate_sin_wave(frequencies[0], duration, fs)
t2, signal2 = generate_sin_wave(frequencies[1], duration, fs)
t3, signal3 = generate_sin_wave(frequencies[2], duration, fs)

# Create subplots for each sine wave
fig, axs = plt.subplots(3, 1, figsize=(8, 6), sharex=True)

axs[0].plot(t1, signal1, color='r')
axs[0].set_title(f'{frequencies[0]} Hz Sinusoidal Wave')
axs[0].set_ylabel('Amplitude')
axs[0].grid(True)

axs[1].plot(t2, signal2, color='g')
axs[1].set_title(f'{frequencies[1]} Hz Sinusoidal Wave')
axs[1].set_ylabel('Amplitude')
axs[1].grid(True)

axs[2].plot(t3, signal3, color='b')
axs[2].set_title(f'{frequencies[2]} Hz Sinusoidal Wave')
axs[2].set_xlabel('Time (s)')
axs[2].set_ylabel('Amplitude')
axs[2].grid(True)

plt.tight_layout()
plt.show()
