from solvers.base import BaseSolver


class Solver(BaseSolver):
    def __init__(self):
        super().__init__()
        self.data = self.client.get_input(year=2025, day=1)

    def solve_part_one(self, data):
        # Implement the logic for part one here
        numbers = list(map(str, self.data.splitlines()))
        # implement your logic
        return numbers

    def solve_part_two(self, data):
        numbers = list(map(str, self.data.splitlines()))
        # implement your logic
        return numbers
