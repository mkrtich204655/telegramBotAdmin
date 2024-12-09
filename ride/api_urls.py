from django.urls import path
from .views_folder.ride_views import RideView
from .views_folder.booking_views import BookingView

urlpatterns = [
    path('get', RideView.as_view({'post': 'get_list'}), name='get_rides'),
    path('show', RideView.as_view({'post': 'show'}), name='show_ride'),
    path('cancel', RideView.as_view({'post': 'cancel'}), name='cancel_ride'),
    path('create', RideView.as_view({'post': 'publish'}), name='create_ride'),
    path('booking', BookingView.as_view({'post': 'get_list'}), name='get_bookings'),
    path('booking/show', BookingView.as_view({'post': 'show'}), name='show_bookings'),
    path('booking/cancel', BookingView.as_view({'post': 'cancel'}), name='cancel_bookings'),
    path('booking/create', BookingView.as_view({'post': 'booking'}), name='create_booking'),
]