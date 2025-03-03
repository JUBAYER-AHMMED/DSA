import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from scipy.fft import fft, ifft
from scipy.io.wavfile import write
import sounddevice as sd

# Parameters
sample_rate = 1000  # Sampling rate (Hz)
duration = 10  # Duration of the signal (seconds)
frequency = 1.2  # Heart rate frequency (Hz, ~72 BPM)

# Generate time array
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

# Simulate a PPG signal (systolic and diastolic peaks)
ppg_signal = (
    1.5 * np.sin(2 * np.pi * frequency * t) +  # Systolic component
    0.5 * np.sin(4 * np.pi * frequency * t)    # Diastolic component
)

# Add noise to simulate real-world data
noise = 0.1 * np.random.normal(size=len(t))
ppg_signal += noise

# Normalize the signal
ppg_signal = (ppg_signal - np.min(ppg_signal)) / (np.max(ppg_signal) - np.min(ppg_signal))

# Detect systolic peaks (highest peaks)
systolic_peaks, _ = find_peaks(ppg_signal, height=0.7, distance=int(sample_rate / frequency))

# Detect diastolic peaks (second-highest peaks)
diastolic_peaks, _ = find_peaks(ppg_signal, height=0.4, distance=int(sample_rate / frequency))

# Calculate heart rate (BPM)
rr_intervals = np.diff(systolic_peaks) / sample_rate  # RR intervals in seconds
heart_rate = 60 / np.mean(rr_intervals)  # Average heart rate in BPM

# Plot the PPG signal with detected peaks
plt.figure(figsize=(12, 6))
plt.plot(t, ppg_signal, label='PPG Signal', color='b')
plt.plot(t[systolic_peaks], ppg_signal[systolic_peaks], "x", label='Systolic Peaks', color='r', markersize=10)
plt.plot(t[diastolic_peaks], ppg_signal[diastolic_peaks], "o", label='Diastolic Peaks', color='g', markersize=8)
plt.title(f"PPG Signal with Detected Peaks (Heart Rate: {heart_rate:.2f} BPM)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Print extracted features
print("Extracted Features:")
print(f"- Systolic Peaks: {systolic_peaks}")
print(f"- Diastolic Peaks: {diastolic_peaks}")
print(f"- Heart Rate: {heart_rate:.2f} BPM")