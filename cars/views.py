from django.shortcuts import render
from cars.models import car
from cars.forms import CarForm

def cars_view(request):
    cars = car.objects.all()
    search = request.GET.get('search')
    #print(request)
    if search:
        # icontains vs contains(do mesmo jeito da string)
        cars = car.objects.filter(model__icontains=search).order_by('model')
    else:
        cars = car.objects.all().order_by('-model')
    
    #cars = car.objects.filter(brand__name = "fiat")
    #cars = car.objects.filter(model__contains = "Mustang")
    #"model__contains" qualquer string que contém essa string "Fusca"
    #print(cars)
    
    return render(
        request,
        'cars.html',
        {'cars': cars } 
    )

def new_car_view(request):
    new_car_form = CarForm()
    return render(request, 'new_car.html', { 'new_car_form': new_car_form })