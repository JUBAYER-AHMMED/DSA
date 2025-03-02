import numpy as np
import matplotlib.pyplot as plt

# Define the time range
t = np.linspace(0, 1, 1000)  # Time from 0 to 1 second with 1000 points

# Define the signal components
x_t = (
    0.25  # DC component
    + 2 * np.sin(2 * np.pi * 5 * t)  # 5 Hz component
    + np.sin(2 * np.pi * 12.5 * t)  # 12.5 Hz component
    + 1.5 * np.sin(2 * np.pi * 20 * t)  # 20 Hz component
    + 0.5 * np.sin(2 * np.pi * 35 * t)  # 35 Hz component
)

# Plot the signal
plt.figure(figsize=(10, 6))
plt.plot(t, x_t, label="x(t)")
plt.title("Signal x(t) = 0.25 + 2sin(2π·5t) + sin(2π·12.5t) + 1.5sin(2π·20t) + 0.5sin(2π·35t)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()
plt.show()