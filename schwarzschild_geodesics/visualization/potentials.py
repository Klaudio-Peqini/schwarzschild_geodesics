from __future__ import annotations

from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

from schwarzschild_geodesics.constants import G, C
from schwarzschild_geodesics.models.metric import schwarzschild_factor, schwarzschild_radius


def relativistic_effective_potential(r: np.ndarray, *, mass: float, angular_momentum: float) -> np.ndarray:
    """
    Potenciali efektiv relativist për grimca test masive.
    """
    f = schwarzschild_factor(r, mass)
    return f * (C**2 + angular_momentum**2 / r**2)


def newtonian_effective_potential(r: np.ndarray, *, mass: float, angular_momentum: float) -> np.ndarray:
    """
    Potenciali efektiv Njutonian për njësi mase.
    """
    mu = G * mass
    return -mu / r + angular_momentum**2 / (2.0 * r**2)


def plot_effective_potentials(
    *,
    mass: float,
    angular_momentum: float,
    output_path: str | Path | None = None,
    r_min: float | None = None,
    r_max: float = 2.0e11,
    n_points: int = 4000,
) -> None:
    """
    Vizaton potencialin efektiv relativist dhe atë Njutonian.
    """
    rs = schwarzschild_radius(mass)
    if r_min is None:
        r_min = max(3.2 * rs, 1.0e7)

    r = np.linspace(r_min, r_max, n_points)
    v_rel = relativistic_effective_potential(r, mass=mass, angular_momentum=angular_momentum)
    v_new = newtonian_effective_potential(r, mass=mass, angular_momentum=angular_momentum)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(r, v_rel, label="Potenciali efektiv relativist")
    ax.plot(r, v_new, label="Potenciali efektiv Njutonian")
    ax.set_xlabel("r [m]")
    ax.set_ylabel("Potenciali efektiv")
    ax.set_title("Krahasimi i potencialeve efektive")
    ax.grid(True, alpha=0.3)
    ax.legend()

    if output_path is not None:
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_path, bbox_inches="tight")

    plt.show()
