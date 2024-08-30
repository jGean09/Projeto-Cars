from django.shortcuts import render
from cars.models import car

def cars_view(request):
    cars = car.objects.all()
    print(cars)
    
    return render(
        request,
        'cars.html',
        {'cars': cars } 
    )
