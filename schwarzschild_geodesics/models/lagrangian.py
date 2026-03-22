from __future__ import annotations

from schwarzschild_geodesics.constants import C
from schwarzschild_geodesics.models.metric import schwarzschild_factor


def lagrangian_equatorial(
    r: float,
    t_dot: float,
    r_dot: float,
    phi_dot: float,
    mass: float,
) -> float:
    """
    Lagranzhiani për një grimcë test në planin ekuatorial.
    """
    f = schwarzschild_factor(r, mass)
    return 0.5 * (-f * C**2 * t_dot**2 + (1.0 / f) * r_dot**2 + r**2 * phi_dot**2)


def conserved_energy(r: float, t_dot: float, mass: float) -> float:
    """
    Energjia specifike relativiste (deri në konvencione shenje).
    """
    f = schwarzschild_factor(r, mass)
    return f * C**2 * t_dot


def conserved_angular_momentum(r: float, phi_dot: float) -> float:
    """
    Momenti këndor specifik.
    """
    return r**2 * phi_dot
