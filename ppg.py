import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

# Bandpass filter function
def bandpass_filter(data, fs=100):
    b, a = signal.butter(4, [0.5 / (0.5 * fs), 5.0 / (0.5 * fs)], btype='band')
    return signal.filtfilt(b, a, data)

# Peak detection function
def detect_peaks(signal_data):
    peaks, _ = signal.find_peaks(signal_data, distance=50, height=0.3)
    return peaks

# Heart rate extraction function
def extract_heart_rate(peaks, fs=100):
    if len(peaks) < 2:
        return 0
    rr_intervals = np.diff(peaks) / fs
    return 60 / np.mean(rr_intervals)

# Abnormality detection function (if RR intervals vary drastically)
def detect_abnormalities(peaks, fs=100):
    rr_intervals = np.diff(peaks) / fs
    mean_rr = np.mean(rr_intervals)
    abnormal_peaks = [i for i, rr in enumerate(rr_intervals) if abs(rr - mean_rr) > 0.2 * mean_rr]
    return abnormal_peaks

# Generate synthetic PPG signal
fs = 100
t = np.linspace(0, 10, fs * 10)
sine_signal = np.sin(2 * np.pi * 1.2 * t)
noise_signal = 0.1 * np.random.normal(0, 1, len(t))
ppg_signal = sine_signal + noise_signal

# Process PPG signal
filtered_signal = bandpass_filter(ppg_signal, fs)
normalized_signal = (filtered_signal - np.min(filtered_signal)) / (np.max(filtered_signal) - np.min(filtered_signal))
peaks = detect_peaks(normalized_signal)
heart_rate = extract_heart_rate(peaks, fs)
abnormalities = detect_abnormalities(peaks, fs)

# Print results
print(f"Estimated Heart Rate: {heart_rate:.2f} BPM")
print(f"Detected Abnormalities: {len(abnormalities)}")

# Plot Results
plt.figure(figsize=(15, 10))

plt.subplot(4, 1, 1)
plt.plot(t, ppg_signal, label='Raw PPG Signal')
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.legend()
plt.grid()

plt.subplot(4, 1, 2)
plt.plot(t, filtered_signal, label='Filtered Signal')
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.legend()
plt.grid()

plt.subplot(4, 1, 3)
plt.plot(t, normalized_signal, label='Normalized Signal')
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.legend()
plt.grid()

plt.subplot(4, 1, 4)
plt.plot(t, normalized_signal, label='Peak Detection')
plt.plot(t[peaks], normalized_signal[peaks], 'ro', label='Detected Peaks')
for ab in abnormalities:
    plt.plot(t[peaks[ab]], normalized_signal[peaks[ab]], 'kx', label='Abnormal Peak')
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()