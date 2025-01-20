from abc import ABC, abstractmethod


class MapServiceInterface(ABC):
    @abstractmethod
    def get_route_time(self, from_address: list, to_address: list) -> dict:
        pass
