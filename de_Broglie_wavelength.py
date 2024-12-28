import numpy as np

# Constants
h = 6.626e-34  # Planck's constant in Js
m_e = 9.109e-31  # Mass of electron in kg
v = 2.2e6  # Velocity of electron in m/s

# Calculate momentum
p = m_e * v

# Calculate de Broglie wavelength
lambda_de_broglie = h / p

print(f"de Broglie wavelength of an electron: {lambda_de_broglie:.4e} meters")
