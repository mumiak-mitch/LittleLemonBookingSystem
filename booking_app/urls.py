from django.urls import path
from .views import HomeView, BookingView, BookingDetailView, BookingUpdateView, BookingDeleteView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('book/', BookingView.as_view(), name="booking"),
    path('details/<int:pk>/', BookingDetailView.as_view(), name="details"),
    path('update/<int:pk>/', BookingUpdateView.as_view(), name="update"),
    path('delete/<int:pk>/', BookingDeleteView.as_view(), name="delete"), 
]