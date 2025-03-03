import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from sklearn.preprocessing import MinMaxScaler

# Parameters for synthetic ECG signal
fs = 360  # Sampling frequency (Hz)
duration = 10  # Duration in seconds
t = np.linspace(0, duration, int(fs * duration), endpoint=False)

# Generate a synthetic ECG signal using sine waves
def generate_ecg(t):
    p_wave = 0.1 * np.sin(2 * np.pi * 5 * t)  # P wave
    qrs_complex = 0.5 * np.sin(2 * np.pi * 15 * t)  # QRS complex
    t_wave = 0.2 * np.sin(2 * np.pi * 7 * t)  # T wave
    ecg = p_wave + qrs_complex + t_wave
    return ecg

# Generate the synthetic ECG signal
ecg_signal = generate_ecg(t)
noise = 0.02 * np.random.normal(size=len(t))
ecg_signal += noise

# Normalize the signal
scaler = MinMaxScaler(feature_range=(0, 1))
ecg_signal_normalized = scaler.fit_transform(ecg_signal.reshape(-1, 1)).flatten()

# Introduce abnormalities
def introduce_abnormalities(ecg_signal, fs):
    tachycardia_start = int(2 * fs)
    tachycardia_end = int(4 * fs)
    ecg_signal[tachycardia_start:tachycardia_end] = generate_ecg(t[tachycardia_start:tachycardia_end] * 1.5)
    bradycardia_start = int(6 * fs)
    bradycardia_end = int(8 * fs)
    ecg_signal[bradycardia_start:bradycardia_end] = generate_ecg(t[bradycardia_start:bradycardia_end] * 0.5)
    return ecg_signal

ecg_signal_with_abnormalities = introduce_abnormalities(ecg_signal_normalized, fs)

# Detect R-peaks
r_peaks, _ = find_peaks(ecg_signal_with_abnormalities, height=0.5, distance=fs//2)

# Detect diastolic peaks (peaks after R-peaks)
diastolic_peaks = []
for r in r_peaks:
    search_range = r + int(0.1 * fs)  # Search 100ms after R-peak
    if search_range < len(ecg_signal_with_abnormalities):
        diastolic, _ = find_peaks(ecg_signal_with_abnormalities[r:search_range], height=0.2)
        if len(diastolic) > 0:
            diastolic_peaks.append(r + diastolic[0])

diastolic_peaks = np.array(diastolic_peaks)

# Calculate RR intervals and heart rate
rr_intervals = np.diff(r_peaks) / fs
heart_rate = 60 / rr_intervals

# Set thresholds
tachycardia_threshold = 100
bradycardia_threshold = 60

diseases = []
abnormality_points = []
print("\n=== Detected Heart Rate and Abnormalities ===")
for i, hr in enumerate(heart_rate):
    disease = 'Normal'
    if hr > tachycardia_threshold:
        disease = 'Tachycardia'
    elif hr < bradycardia_threshold:
        disease = 'Bradycardia'
    diseases.append(disease)
    if disease != 'Normal':
        abnormality_points.append(r_peaks[i + 1])
    print(f"R-peak at sample {r_peaks[i+1]}: {disease} (Heart Rate: {hr:.2f} bpm)")

print("\nSystolic (R-peaks) detected at samples:", r_peaks)
print("Diastolic peaks detected at samples:", diastolic_peaks)
print("Abnormality found at samples:", abnormality_points)

# Plot ECG with peaks
plt.figure(figsize=(12, 6))
plt.plot(t, ecg_signal_with_abnormalities, label='ECG Signal', color='lime')
plt.scatter(t[r_peaks], ecg_signal_with_abnormalities[r_peaks], color='red', label='Systolic Peaks (R-peaks)', zorder=5)
plt.scatter(t[diastolic_peaks], ecg_signal_with_abnormalities[diastolic_peaks], color='blue', label='Diastolic Peaks', zorder=5)

for i, point in enumerate(r_peaks[1:]):
    if i < len(diseases) and diseases[i] != 'Normal':
        color = 'red' if diseases[i] == 'Tachycardia' else 'orange'
        plt.scatter(t[point], ecg_signal_with_abnormalities[point], color=color, zorder=5)
        plt.annotate(diseases[i], (t[point], ecg_signal_with_abnormalities[point]),
                     textcoords='offset points', xytext=(0, 10), ha='center', color=color, fontsize=9, fontweight='bold')

plt.title('Synthetic ECG Signal with Systolic and Diastolic Peaks', color='black')
plt.xlabel('Time (s)', color='black')
plt.ylabel('Amplitude', color='black')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
