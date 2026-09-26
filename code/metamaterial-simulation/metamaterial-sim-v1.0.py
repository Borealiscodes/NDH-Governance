"""
metamaterial-sim-v1.0.py — Spectral Solar Manifold (SSM)
Altitude: A1
Membrane: Code • Metamaterial Simulation
Version: v1.0

Simulates metamaterial band-pass behavior, refractive index gradients, and harmonic
confinement factor C for the SSM metamaterial layer. Implements Gaussian band-pass
windows, index modulation, and confinement metrics aligned with engineering specs.

Dependencies:
- numpy
- scipy

This file is the second executable primitive in the SSM code layer.
"""

import numpy as np
from scipy.stats import norm


# ------------------------------------------------------------
# 1. Refractive Index Gradient
# ------------------------------------------------------------

def refractive_index(x, n0=1.42, beta=0.18, L=1.0):
    """
    Refractive index field n(x) = n0 + beta * sin(2πx/L)
    """
    return n0 + beta * np.sin(2 * np.pi * x / L)


# ------------------------------------------------------------
# 2. Band-Pass Windows (Gaussian)
# ------------------------------------------------------------

SOLAR_PEAKS_NM = np.array([450, 550, 650, 800, 1000])
WINDOW_WIDTHS_NM = np.array([40, 35, 30, 25, 20])  # σ values

def bandpass_window(lambda_nm, center_nm, sigma_nm):
    """
    Gaussian band-pass window centered at center_nm with width sigma_nm.
    """
    return norm.pdf(lambda_nm, loc=center_nm, scale=sigma_nm)


# ------------------------------------------------------------
# 3. Harmonic Confinement Factor
# ------------------------------------------------------------

def confinement_factor(eigenfunctions, lambda_nm_grid):
    """
    Computes confinement factor C for each eigenmode.
    eigenfunctions: list of arrays φ_n(x)
    lambda_nm_grid: wavelength grid for band-pass evaluation
    """
    C_values = []

    for n, phi in enumerate(eigenfunctions):
        center = SOLAR_PEAKS_NM[n]
        sigma = WINDOW_WIDTHS_NM[n]

        B = bandpass_window(lambda_nm_grid, center, sigma)

        numerator = np.sum(B * phi**2)
        denominator = np.sum(phi**2)

        C_values.append(numerator / denominator)

    return np.array(C_values)


# ------------------------------------------------------------
# 4. Example Eigenfunction Generator (Placeholder)
# ------------------------------------------------------------

def example_eigenfunctions(N=500, modes=5):
    """
    Generates placeholder eigenfunctions for testing.
    In full simulation, import eigenfunctions from laplacian-spectrum.py.
    """
    x = np.linspace(0, 1, N)
    return [np.sin((n + 1) * np.pi * x) for n in range(modes)]


# ------------------------------------------------------------
# 5. Main Execution
# ------------------------------------------------------------

if __name__ == "__main__":
    lambda_grid = np.linspace(400, 1100, 2000)  # nm
    eigenfuncs = example_eigenfunctions()

    C = confinement_factor(eigenfuncs, lambda_grid)

    print("Confinement Factors:", C)
    print("Minimum Required: C ≥ 1.25")
