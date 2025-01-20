import requests
from .map_service_interface import MapServiceInterface


class GoogleMapService(MapServiceInterface):
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://maps.googleapis.com/maps/api"

    def get_route_time(self,  from_address: list, to_address: list) -> dict:
        pass
