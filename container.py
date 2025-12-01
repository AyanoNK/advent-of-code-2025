from dependency_injector import containers, providers

from client import AdventOfCodeClient


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    client = providers.Singleton(AdventOfCodeClient)
