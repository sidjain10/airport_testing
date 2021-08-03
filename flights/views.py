import flights
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import json
from django.views.decorators.csrf import csrf_exempt
from pprint import pprint
from .models import Flight, Passenger

# Create your views here.
def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })

def flight(request, flight_id):
    flight = Flight.objects.get(pk=flight_id)
    return render(request, "flights/flight.html", {
        "flight": flight,
        "passengers": flight.passenger.all(),
        "non_passengers": Passenger.objects.exclude(flights=flight).all()
    })

def book(request, flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(pk=flight_id)
        passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse("flight", args=(flight_id, )))

    else:
        return "HELLO"    

@csrf_exempt
def data(requset):

    if requset.method == "POST":
        data = json.loads(requset.body)
        air ={}
        ll = []       
        code = data.get('code')
        city = data.get('city')
        for i in range(0, len(code)):
            air[code[i]] = city[i]
            ll.append(f"{code[i]}-{city[i]}")
        # pprint(air)
        # print(" ////////  CITY ///////  ")
        # pprint(city)
        # print()
        # print("////// CODE //////")
        # pprint(code)
        # print()
        print("//////  llllllll ///////")
        pprint(ll)
        return render(requset, "flights/data.html")


    return render(requset, "flights/data.html")