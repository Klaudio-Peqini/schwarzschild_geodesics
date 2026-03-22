#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

from schwarzschild_geodesics.constants import M_SUN
from schwarzschild_geodesics.models.metric import schwarzschild_radius
from schwarzschild_geodesics.numerics.solver import solve_orbits, estimate_precession
from schwarzschild_geodesics.visualization.potentials import plot_effective_potentials
from schwarzschild_geodesics.visualization.orbits import plot_orbit_comparison


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Studim numerik i orbitave Schwarzschild dhe krahasim me gravitetin Njutonian."
    )
    parser.add_argument(
        "--mode",
        choices=["potential", "orbit", "precession"],
        default="orbit",
        help="Zgjidhni llojin e analizës numerike.",
    )
    parser.add_argument("--mass", type=float, default=M_SUN, help="Masa qendrore në kg.")
    parser.add_argument("--r0", type=float, default=4.6e10, help="Rrezja fillestare në m.")
    parser.add_argument("--phi0", type=float, default=0.0, help="Këndi fillestar në rad.")
    parser.add_argument("--vr0", type=float, default=0.0, help="Shpejtësia radiale fillestare.")
    parser.add_argument("--L", type=float, default=5.2e15, help="Momenti këndor specifik.")
    parser.add_argument("--tau-max", type=float, default=2.0e7, help="Koha afine / vetjake maksimale.")
    parser.add_argument("--samples", type=int, default=25000, help="Numri i pikave të ruajtura.")
    parser.add_argument(
        "--output-dir",
        type=str,
        default="outputs",
        help="Dosja ku ruhen figurat dalëse.",
    )
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    rs = schwarzschild_radius(args.mass)
    print(f"Masa qendrore = {args.mass:.6e} kg")
    print(f"Rrezja e Schwarzschild-it = {rs:.6e} m")

    if args.mode == "potential":
        outpath = output_dir / "effective_potential.pdf"
        plot_effective_potentials(
            mass=args.mass,
            angular_momentum=args.L,
            output_path=outpath,
        )
        print(f"Figura u ruajt te: {outpath}")
        return

    rel_solution, new_solution = solve_orbits(
        mass=args.mass,
        r0=args.r0,
        phi0=args.phi0,
        vr0=args.vr0,
        angular_momentum=args.L,
        tau_max=args.tau_max,
        samples=args.samples,
    )

    if args.mode == "orbit":
        outpath = output_dir / "orbit_comparison.pdf"
        plot_orbit_comparison(
            rel_solution=rel_solution,
            newton_solution=new_solution,
            output_path=outpath,
        )
        print(f"Figura u ruajt te: {outpath}")
        return

    if args.mode == "precession":
        result = estimate_precession(rel_solution.phi, rel_solution.r)
        if result["count"] < 3:
            print("Nuk u gjetën mjaftueshëm perihele. Provoni të rrisni --tau-max ose të ndryshoni parametrat.")
        else:
            print(f"Numri i periheleve të gjetura: {result['count']}")
            print(f"Precesioni mesatar për orbitë [rad]: {result['mean_precession_rad']:.12e}")
            print(f"Precesioni mesatar për orbitë [arcsec]: {result['mean_precession_arcsec']:.12e}")


if __name__ == "__main__":
    main()
