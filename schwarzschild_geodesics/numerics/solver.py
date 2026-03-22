from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from scipy.signal import find_peaks

from schwarzschild_geodesics.constants import ARCSEC_PER_RAD
from schwarzschild_geodesics.models.geodesic_equations import rhs_relativistic, rhs_newtonian
from schwarzschild_geodesics.numerics.integrators import integrate_system


@dataclass
class OrbitSolution:
    tau: np.ndarray
    r: np.ndarray
    phi: np.ndarray
    vr: np.ndarray
    x: np.ndarray
    y: np.ndarray
    success: bool
    message: str


def _build_orbit_solution(integration_result) -> OrbitSolution:
    r = integration_result.y[0]
    phi = integration_result.y[1]
    vr = integration_result.y[2]
    x = r * np.cos(phi)
    y = r * np.sin(phi)
    return OrbitSolution(
        tau=integration_result.tau,
        r=r,
        phi=phi,
        vr=vr,
        x=x,
        y=y,
        success=integration_result.success,
        message=integration_result.message,
    )


def solve_orbits(
    *,
    mass: float,
    r0: float,
    phi0: float,
    vr0: float,
    angular_momentum: float,
    tau_max: float,
    samples: int,
) -> tuple[OrbitSolution, OrbitSolution]:
    """
    Zgjidh orbitën relativiste dhe atë Njutoniane me të njëjtat kushte fillestare.
    """
    y0 = [r0, phi0, vr0]

    rel = integrate_system(
        rhs_relativistic,
        y0=y0,
        tau_max=tau_max,
        samples=samples,
        mass=mass,
        angular_momentum=angular_momentum,
    )
    new = integrate_system(
        rhs_newtonian,
        y0=y0,
        tau_max=tau_max,
        samples=samples,
        mass=mass,
        angular_momentum=angular_momentum,
    )

    return _build_orbit_solution(rel), _build_orbit_solution(new)


def estimate_precession(phi: np.ndarray, r: np.ndarray) -> dict[str, float]:
    """
    Gjen perihelet dhe vlerëson precesionin mesatar për orbitë.
    """
    peaks, _ = find_peaks(-r)
    count = len(peaks)
    if count < 3:
        return {
            "count": count,
            "mean_precession_rad": float("nan"),
            "mean_precession_arcsec": float("nan"),
        }

    phi_peri = phi[peaks]
    delta_phi = np.diff(phi_peri)
    precession_per_orbit = delta_phi - 2.0 * np.pi

    return {
        "count": count,
        "mean_precession_rad": float(np.mean(precession_per_orbit)),
        "mean_precession_arcsec": float(np.mean(precession_per_orbit) * ARCSEC_PER_RAD),
    }
