import numpy as np
import matplotlib.pyplot as plt
# Define the unit ramp signal
def unit_ramp(n):
    return np.where(n >= 0, n, 0)

# Define the range of n
n = np.arange(-5, 6)  # From -5 to 5

# Generate the unit ramp signal
r = unit_ramp(n)

# Plot the unit ramp signal
plt.stem(n, r, basefmt=" ")
plt.title("Unit Ramp Signal")
plt.xlabel("n")
plt.ylabel("r[n]")
plt.grid(True)
plt.show()
#R(N) = N, IF N>=0, OTHERWISE 0


# # Define the range of n
# n = np.arange(-5, 6)  # From -5 to 5

# # Generate all three signals
# delta = unit_sample(n)
# u = unit_step(n)
# r = unit_ramp(n)

# # Plot all three signals
# plt.figure(figsize=(12, 8))

# # Unit Sample Sequence
# plt.subplot(3, 1, 1)
# plt.stem(n, delta, basefmt=" ", use_line_collection=True)
# plt.title("Unit Sample Sequence (Discrete Delta Function)")
# plt.xlabel("n")
# plt.ylabel("δ[n]")
# plt.grid(True)

# # Unit Step Signal
# plt.subplot(3, 1, 2)
# plt.stem(n, u, basefmt=" ", use_line_collection=True)
# plt.title("Unit Step Signal")
# plt.xlabel("n")
# plt.ylabel("u[n]")
# plt.grid(True)

# # Unit Ramp Signal
# plt.subplot(3, 1, 3)
# plt.stem(n, r, basefmt=" ", use_line_collection=True)
# plt.title("Unit Ramp Signal")
# plt.xlabel("n")
# plt.ylabel("r[n]")
# plt.grid(True)

# plt.tight_layout()
# plt.show()