from django.shortcuts import render
from .models import Parking, Slot
from django.db.models import Q
from django.contrib import messages

def get_cities():
    cities = Parking.objects.values('city').distinct()
    print('cities : ',[c for c in cities ])
    return cities
    # cities = Parking.objects.all().distinct('city')    #in postgres
  

  

def slots(request):
  context = {}
 
  cities = get_cities()
  context['cities'] = cities
  if request.method == "POST":
    city = request.POST.get('city')
    parking_name = request.POST.get('parking_name')

    context['city'] = city
    context['parking_name'] = parking_name

    parking = None
    slots  = None
    parkings= None

    try:
      if city and parking_name:
        parking = Parking.objects.get( Q(city__iexact = city) & Q(name__iexact = parking_name) )
        slots = Slot.objects.filter(parking = parking) 

        context['total_slots']  = slots.count()
        context['filled_slots'] = slots.filter(is_avail=False).count()
        context['avail_slots'] = slots.filter(is_avail=True).count()
        context['parking']  = parking  
        context['slots']    = slots 
        print("context : ",context)
        return render(request,'slots/slots.html', context=context)

      elif city:
        parkings = Parking.objects.filter(city__iexact = city)
        context['parkings'] = parkings
        print("context : ",context)
        return render(request,'slots/check_slots.html',context)

      else:
        return render(request,'slots/check_slots.html')
    except Exception as e:
      print("Exception : ",e)
      return render(request,'slots/check_slots.html')
    
  else:
    cities = get_cities()
    context['cities'] = cities
    return render(request,'slots/check_slots.html', context)
