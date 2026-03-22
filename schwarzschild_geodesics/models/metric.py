from __future__ import annotations

import numpy as np

from schwarzschild_geodesics.constants import G, C


def schwarzschild_radius(mass: float) -> float:
    """Kthen rrezen e Schwarzschild-it për një masë të dhënë."""
    return 2.0 * G * mass / C**2


def schwarzschild_factor(r: np.ndarray | float, mass: float) -> np.ndarray | float:
    """Faktori f(r) = 1 - r_s/r."""
    rs = schwarzschild_radius(mass)
    return 1.0 - rs / r


def metric_components_equatorial(r: np.ndarray | float, mass: float) -> dict[str, np.ndarray | float]:
    """
    Jep komponentët kryesorë të metrikës në planin ekuatorial.
    """
    f = schwarzschild_factor(r, mass)
    return {
        "g_tt": -f * C**2,
        "g_rr": 1.0 / f,
        "g_phiphi": r**2,
    }
