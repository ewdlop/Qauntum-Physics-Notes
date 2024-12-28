import numpy as np
import matplotlib.pyplot as plt

def energy_time_uncertainty(lifetime):
    """Calculate uncertainty in energy based on lifetime using ΔE·Δt ≥ ħ/2."""
    hbar = 1.0545718e-34  # Planck's constant (Js)
    return hbar / (2 * lifetime)

# Particle lifetimes (in seconds)
lifetimes = np.logspace(-23, -8, 50)  # Range of interaction times
energy_uncertainties = energy_time_uncertainty(lifetimes)

# Plot
plt.figure(figsize=(8, 5))
plt.loglog(lifetimes, energy_uncertainties, label="ΔE vs. Δt")
plt.xlabel("Lifetime (s)")
plt.ylabel("Energy Uncertainty (J)")
plt.title("Energy-Time Uncertainty Relation")
plt.legend()
plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.show()


import numpy as np
import matplotlib.pyplot as plt

def energy_uncertainty(lifetime):
    """Calculate energy uncertainty (ΔE) using ΔE·Δt ≥ ħ/2."""
    hbar = 1.0545718e-34  # Planck's constant (Js)
    return hbar / (2 * lifetime)

# Simulate a range of lifetimes (in seconds)
lifetimes = np.logspace(-9, -3, 50)  # From nanoseconds to milliseconds
energy_uncertainties = energy_uncertainty(lifetimes)

# Wavelength broadening (assuming a photon energy of ~1 eV)
eV_to_J = 1.60218e-19  # Conversion factor
wavelength_uncertainty = 1240 / (energy_uncertainties / eV_to_J)  # nm

# Plot ΔE and Δλ as functions of lifetime
plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.loglog(lifetimes, energy_uncertainties, label="ΔE (Energy Uncertainty)")
plt.xlabel("Lifetime (s)")
plt.ylabel("ΔE (J)")
plt.title("Energy-Time Uncertainty")
plt.legend()
plt.grid(True, which="both", linestyle="--", linewidth=0.5)

plt.subplot(2, 1, 2)
plt.loglog(lifetimes, wavelength_uncertainty, label="Δλ (Wavelength Uncertainty)", color='orange')
plt.xlabel("Lifetime (s)")
plt.ylabel("Δλ (nm)")
plt.title("Wavelength Broadening")
plt.legend()
plt.grid(True, which="both", linestyle="--", linewidth=0.5)

plt.tight_layout()
plt.show()
