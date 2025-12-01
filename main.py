import argparse
import importlib
from pathlib import Path

from container import Container


def get_available_days() -> list[str]:
    """Find all day_*.py files in solvers directory."""
    solvers_dir = Path(__file__).parent / "solvers"
    days = []
    for path in solvers_dir.glob("day_*.py"):
        day_num = path.stem.split("_")[1]
        days.append(day_num)
    return sorted(days, key=int)


def load_solver(day: str):
    """Dynamically import and return the solver for the given day."""
    module = importlib.import_module(f"solvers.day_{day}")
    return module.Solver()


def main():
    container = Container()
    container.wire(packages=["solvers"])

    available_days = get_available_days()

    parser = argparse.ArgumentParser(description="Advent of Code 2025 solver")
    parser.add_argument(
        "--day",
        type=str,
        required=True,
        choices=available_days,
        help=f"Day to solve (available: {', '.join(available_days)})",
    )
    args = parser.parse_args()

    solver = load_solver(args.day)
    print(f"Day {args.day}")
    print(f"Part 1: {solver.solve_part_one(None)}")
    print(f"Part 2: {solver.solve_part_two(None)}")


if __name__ == "__main__":
    main()
