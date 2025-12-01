from abc import ABC, abstractmethod

from dependency_injector.wiring import Provide, inject

from client import AdventOfCodeClient
from container import Container


class BaseSolver(ABC):
    @inject
    def __init__(self, client: AdventOfCodeClient = Provide[Container.client]):
        self.client = client

    @abstractmethod
    def solve_part_one(self, data):
        pass

    @abstractmethod
    def solve_part_two(self, data):
        pass
