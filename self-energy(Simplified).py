import numpy as np

# Constants
alpha = 1/137  # Fine-structure constant
m_e = 9.10938356e-31  # Electron mass (kg)
c = 3e8  # Speed of light (m/s)
hbar = 1.0545718e-34  # Reduced Planck constant (J·s)

# Function to calculate self-energy correction (simplified)
def electron_self_energy_correction(alpha, m_e):
    # This is a highly simplified and abstracted formula
    correction = alpha * m_e * c**2
    return correction

# Calculate the self-energy correction
self_energy_correction = electron_self_energy_correction(alpha, m_e)

print(f"Electron self-energy correction: {self_energy_correction:.4e} J")

# Convert to eV
self_energy_correction_eV = self_energy_correction / (1.60218e-19)
print(f"Electron self-energy correction: {self_energy_correction_eV:.4e} eV")
