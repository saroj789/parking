from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from slots.models import Parking, Slot
from django.contrib import messages
from .models import BookSlot

# Create your views here.

@login_required(login_url='login')
def booking(request):
  context = {}
  if request.method == "POST":
    city = request.POST.get('city')
    parking_name = request.POST.get('parking_name')
    position = request.POST.get('position')
    print(city,parking_name,position)
    context['city'] = city
    context['parking_name'] = parking_name
    context['position'] = position
    return render(request,'booking/booking.html',context)
  
  return redirect('slots') 


def confirm_booking(request):
  context = {}
  if request.method == "POST":
    city = request.POST.get('city')
    parking_name = request.POST.get('parking_name')
    position = request.POST.get('position')
    car_number = request.POST.get('car_number')

    context['city'] = city
    context['parking_name'] = parking_name
    context['position'] = position
    context['car_number'] = car_number

    try:
      parking = Parking.objects.get(city=city, name=parking_name)
      slot = Slot.objects.get(parking=parking,position=position)
      print(slot,parking)
      bookslot = BookSlot(user=request.user, slot=slot, car_number=car_number)
      bookslot.save()
      slot.is_avail = False
      slot.save()
      messages.success(request, f'Your booking fot {city} : {parking}: {position} has been successfully booked')
    except Exception as e :
      print("exception : ",e)
      messages.success(request, 'Please try after some time !')

  return redirect('slots')
  
      

