import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import hbar, m_e
from scipy.sparse import diags
from scipy.sparse.linalg import expm

# Constants
L = 1e-8  # Length of the domain in meters
N = 1000  # Number of grid points
dx = L / (N - 1)  # Spatial step size
x = np.linspace(0, L, N)  # Spatial grid

# Time parameters
dt = 1e-18  # Time step size in seconds
T = 1e-15  # Total simulation time in seconds
steps = int(T / dt)  # Number of time steps

# Potential barrier
V0 = 20 * 1.60218e-19  # Barrier height in joules (20 eV)
a = L / 5  # Barrier width
V = np.zeros_like(x)
V[int(N/2 - a/dx):int(N/2 + a/dx)] = V0

# Initial wave packet
x0 = L / 4
sigma = L / 20
k0 = 5e10
psi_0 = np.exp(-(x - x0)**2 / (2 * sigma**2)) * np.exp(1j * k0 * x)
psi_0 /= np.sqrt(np.sum(np.abs(psi_0)**2) * dx)  # Normalize

# Hamiltonian
diagonal = hbar**2 / (2 * m_e * dx**2)
off_diagonal = -hbar**2 / (2 * m_e * dx**2)
H = diags([diagonal + V, off_diagonal, off_diagonal], [0, -1, 1], shape=(N, N))

# Time evolution operator
U = expm(-1j * H * dt / hbar)

# Time evolution
psi = psi_0
for _ in range(steps):
    psi = U @ psi

# Probability density
prob_density = np.abs(psi)**2

# Plot potential and final probability density
plt.figure(figsize=(10, 6))
plt.plot(x, V / 1.60218e-19, label='Potential barrier (eV)')
plt.plot(x, prob_density, label='Probability density')
plt.xlabel('Position (m)')
plt.ylabel('Energy (eV) / Probability density')
plt.title('Quantum Tunneling')
plt.legend()
plt.grid(True)
plt.show()
