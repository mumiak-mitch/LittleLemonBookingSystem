from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import Booking

class HomeView(ListView):
    model = Booking
    template_name = "index.html"

class BookingView(CreateView):
    model = Booking
    template_name = "booking.html"
    fields = "__all__"

class BookingDetailView(DetailView):
    model = Booking
    template_name = "details.html"

class BookingUpdateView(UpdateView):
    model = Booking
    template_name = "update.html"
    fields = "__all__"

class BookingDeleteView(DeleteView):
    model = Booking
    template_name = "delete.html"