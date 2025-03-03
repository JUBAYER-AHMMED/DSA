import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, ifft
from scipy.io.wavfile import write
import sounddevice as sd  # For audio playback

# Parameters
sample_rate = 44100  # Sampling rate (Hz)
duration = 2.0  # Duration of the signal (seconds)
frequency = 440.0  # Frequency of the sine wave (Hz)
noise_amplitude = 0.2  # Amplitude of the noise

# Generate time array
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

# Generate a pure sine wave
sine_wave = np.sin(2 * np.pi * frequency * t)

# Add random noise
noise = noise_amplitude * np.random.normal(size=len(t))
noisy_signal = sine_wave + noise

# Apply DFT (FFT)
fft_signal = fft(noisy_signal)

# Compute frequencies corresponding to FFT bins
frequencies = np.fft.fftfreq(len(fft_signal), 1 / sample_rate)

# Filter out high frequencies (noise)
cutoff_frequency = 500  # Remove frequencies above 500 Hz
fft_signal_filtered = fft_signal.copy()
fft_signal_filtered[np.abs(frequencies) > cutoff_frequency] = 0

# Apply Inverse DFT (IFFT)
cleaned_signal = np.real(ifft(fft_signal_filtered))

# Normalize the cleaned signal to avoid clipping
cleaned_signal = cleaned_signal / np.max(np.abs(cleaned_signal))

# Create a single figure with subplots
plt.figure(figsize=(15, 12))

# Plot 1: Original Signal
plt.subplot(5, 1, 1)
plt.plot(t, sine_wave, color='b')
plt.title("Original Signal (Pure Sine Wave, 440 Hz)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)

# Plot 2: Signal After Adding Noise
plt.subplot(5, 1, 2)
plt.plot(t, noisy_signal, color='r')
plt.title("Signal After Adding Noise")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)

# Plot 3: Signal After DFT (Frequency Domain)
plt.subplot(5, 1, 3)
plt.plot(frequencies[:len(frequencies)//2], np.abs(fft_signal[:len(fft_signal)//2]), color='g')
plt.title("Signal After DFT (Frequency Domain)")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.grid(True)

# Plot 4: Signal After Filtering (Frequency Domain)
plt.subplot(5, 1, 4)
plt.plot(frequencies[:len(frequencies)//2], np.abs(fft_signal_filtered[:len(fft_signal_filtered)//2]), color='m')
plt.title("Signal After Filtering (Frequency Domain)")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.grid(True)

# Plot 5: Signal After IDFT (Cleaned Signal)
plt.subplot(5, 1, 5)
plt.plot(t, cleaned_signal, color='orange')
plt.title("Signal After IDFT (Cleaned Signal)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)

# Adjust layout and display the figure
plt.tight_layout()
plt.savefig("combined_figures.png", dpi=300)
plt.show()

# Save the signals as .wav files
write("original_sine_wave.wav", sample_rate, sine_wave.astype(np.float32))
write("noisy_signal.wav", sample_rate, noisy_signal.astype(np.float32))
write("cleaned_signal.wav", sample_rate, cleaned_signal.astype(np.float32))

# Play the audio signals using sounddevice
print("Playing the original sine wave...")
sd.play(sine_wave, sample_rate)
sd.wait()

print("Playing the noisy signal...")
sd.play(noisy_signal, sample_rate)
sd.wait()

print("Playing the cleaned signal...")
sd.play(cleaned_signal, sample_rate)
sd.wait()

print("Audio signals saved as .wav files:")
print("- original_sine_wave.wav")
print("- noisy_signal.wav")
print("- cleaned_signal.wav")