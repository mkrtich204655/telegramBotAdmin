from django.conf import settings
from .google_map_service import GoogleMapService

# Initialize the map service with the API key from settings
map_service = GoogleMapService(api_key=settings.GOOGLE_MAPS_API_KEY)
