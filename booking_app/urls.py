from django.urls import path
from .views import form_view, bookings

urlpatterns = [
    path('', form_view, name="booking"),
    path('bookings/', bookings, name="bookings"),
]