import json
from datetime import datetime
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from .forms import BookingForm
from .models import Booking

def form_view(request):
    form = BookingForm()

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'success'})
    
    return render(request, 'booking.html', {'form': form})

@csrf_exempt
def bookings(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        exist = Booking.objects.filter(
            reservation_date=data['reservation_date'],
            reservation_slot=data['reservation_slot']
        ).exists()
        if not exist:
            booking = Booking(
                first_name=data['first_name'],
                reservation_date=data['reservation_date'],
                reservation_slot=data['reservation_slot'],
            )
            booking.save()
        else:
            return HttpResponse("{'error': 1}", content_type='application/json')

    date = request.GET.get('date', datetime.today().date())

    bookings = Booking.objects.filter(reservation_date=date)
    booking_json = serializers.serialize('json', bookings)

    return HttpResponse(booking_json, content_type='application/json')