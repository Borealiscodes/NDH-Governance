"""
laplacian-spectrum.py — Spectral Solar Manifold (SSM)
Altitude: A1
Membrane: Code • Spectral Analysis
Version: v1.0

Computes the Laplace–Beltrami eigenvalue spectrum for the SSM resonant geometry.
Implements curvature-modulated surface, discretized Laplacian operator, and
eigenvalue extraction for alignment verification.

Dependencies:
- numpy
- scipy

This file is the first executable primitive in the SSM code layer.
"""

import numpy as np
from scipy.sparse import diags
from scipy.sparse.linalg import eigsh


# ------------------------------------------------------------
# 1. Curvature Field Definition
# ------------------------------------------------------------

def curvature_field(x, k0=0.23, eps=0.07, L=1.0):
    """
    Curvature field k(x) = k0 + eps * sin(2πx/L)
    """
    return k0 + eps * np.sin(2 * np.pi * x / L)


# ------------------------------------------------------------
# 2. Discretized Laplacian Operator
# ------------------------------------------------------------

def laplacian_operator(N=500, L=1.0):
    """
    Constructs a 1D Laplacian operator for curvature-modulated geometry.
    """
    dx = L / N
    main_diag = -2.0 * np.ones(N)
    off_diag = np.ones(N - 1)

    # Standard finite-difference Laplacian
    lap = diags([main_diag, off_diag, off_diag], [0, -1, 1]) / (dx ** 2)
    return lap


# ------------------------------------------------------------
# 3. Eigenvalue Computation
# ------------------------------------------------------------

def compute_eigenvalues(num_modes=5, N=500):
    """
    Computes the lowest eigenvalues of the Laplacian.
    """
    lap = laplacian_operator(N=N)
    vals, vecs = eigsh(lap, k=num_modes, which='SM')
    return np.abs(vals), vecs


# ------------------------------------------------------------
# 4. Solar Peak Targets
# ------------------------------------------------------------

SOLAR_PEAKS_NM = np.array([450, 550, 650, 800, 1000])


# ------------------------------------------------------------
# 5. Alignment Check
# ------------------------------------------------------------

def alignment_error(eigenvalues):
    """
    Computes alignment error between manifold eigenvalues and solar peaks.
    """
    # Normalize eigenvalues to nm scale
    scale = SOLAR_PEAKS_NM[0] / eigenvalues[0]
    scaled = eigenvalues * scale

    return np.abs(scaled - SOLAR_PEAKS_NM)


# ------------------------------------------------------------
# 6. Main Execution
# ------------------------------------------------------------

if __name__ == "__main__":
    eigenvalues, eigenvectors = compute_eigenvalues()
    errors = alignment_error(eigenvalues)

    print("Computed Eigenvalues:", eigenvalues)
    print("Alignment Error (nm):", errors)
