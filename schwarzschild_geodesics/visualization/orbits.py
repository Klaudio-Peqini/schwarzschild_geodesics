from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt


def plot_orbit_comparison(*, rel_solution, newton_solution, output_path: str | Path | None = None) -> None:
    """
    Vizaton orbitën relativiste dhe orbitën Njutoniane.
    """
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.plot(rel_solution.x, rel_solution.y, label="Orbitë relativiste")
    ax.plot(newton_solution.x, newton_solution.y, linestyle="--", label="Orbitë Njutoniane")
    ax.scatter([0.0], [0.0], s=120, marker="o", label="Masa qendrore")
    ax.set_xlabel("x [m]")
    ax.set_ylabel("y [m]")
    ax.set_title("Krahasimi i orbitës relativiste me atë Njutoniane")
    ax.axis("equal")
    ax.grid(True, alpha=0.3)
    ax.legend()

    if output_path is not None:
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_path, bbox_inches="tight")

    plt.show()
