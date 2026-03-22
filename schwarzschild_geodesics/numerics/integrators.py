from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

import numpy as np
from scipy.integrate import solve_ivp


@dataclass
class IntegrationResult:
    tau: np.ndarray
    y: np.ndarray
    success: bool
    message: str


def integrate_system(
    rhs: Callable,
    y0: list[float],
    tau_max: float,
    samples: int,
    **rhs_kwargs,
) -> IntegrationResult:
    """
    Integron një sistem ODE me solve_ivp.
    """
    tau_eval = np.linspace(0.0, tau_max, samples)
    sol = solve_ivp(
        lambda tau, y: rhs(tau, y, **rhs_kwargs),
        (0.0, tau_max),
        y0,
        t_eval=tau_eval,
        rtol=1e-9,
        atol=1e-9,
    )
    return IntegrationResult(tau=sol.t, y=sol.y, success=sol.success, message=sol.message)
