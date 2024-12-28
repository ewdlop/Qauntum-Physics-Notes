import math

# Constants
h_bar = h / (2 * math.pi)  # Reduced Planck's constant

# Given uncertainties
delta_x = 1e-10  # Uncertainty in position in meters

# Calculate uncertainty in momentum
delta_p = h_bar / (2 * delta_x)

print(f"Uncertainty in momentum: {delta_p:.4e} kg·m/s")
