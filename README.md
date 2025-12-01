# Advent of Code 2025

My solutions for [Advent of Code 2025](https://adventofcode.com/2025).

## Setup

Requires Python 3.12+ and [uv](https://docs.astral.sh/uv/).

```bash
uv sync
```

Copy `.env.example` to `.env` and add your session cookie:

```bash
cp .env.example .env
```

Get your session cookie from the Advent of Code website (browser dev tools, Application, Cookies, `session`).

## Usage

Run a specific day:

```bash
uv run python main.py --day 1
```

## Adding Solutions

Create a new file in `solvers/` named `day_N.py`:

```python
from solvers.base import BaseSolver


class Solver(BaseSolver):
    def solve_part_one(self):
        input_data = self.client.get_input(2025, 1)
        # your solution here
        return result

    def solve_part_two(self):
        input_data = self.client.get_input(2025, 1)
        # your solution here
        return result
```
