from __future__ import annotations

from dataclasses import dataclass

from schwarzschild_geodesics.constants import G, C


@dataclass
class PhaseState:
    r: float
    phi: float
    vr: float


def radial_acceleration_relativistic(r: float, angular_momentum: float, mass: float) -> float:
    """
    Ekuacion radial i reduktuar për orbitat ekuatoriale.
    """
    mu = G * mass
    return -mu / r**2 + angular_momentum**2 / r**3 - 3.0 * mu * angular_momentum**2 / (C**2 * r**4)


def radial_acceleration_newtonian(r: float, angular_momentum: float, mass: float) -> float:
    """
    Ekuacion radial klasik.
    """
    mu = G * mass
    return -mu / r**2 + angular_momentum**2 / r**3


def rhs_relativistic(tau: float, y: list[float], *, mass: float, angular_momentum: float) -> list[float]:
    """
    Sistemi i rendit të parë për rastin relativist.
    """
    r, phi, vr = y
    dr_dtau = vr
    dphi_dtau = angular_momentum / r**2
    dvr_dtau = radial_acceleration_relativistic(r, angular_momentum, mass)
    return [dr_dtau, dphi_dtau, dvr_dtau]


def rhs_newtonian(tau: float, y: list[float], *, mass: float, angular_momentum: float) -> list[float]:
    """
    Sistemi i rendit të parë për rastin Njutonian.
    """
    r, phi, vr = y
    dr_dtau = vr
    dphi_dtau = angular_momentum / r**2
    dvr_dtau = radial_acceleration_newtonian(r, angular_momentum, mass)
    return [dr_dtau, dphi_dtau, dvr_dtau]
