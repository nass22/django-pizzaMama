from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers
from .models import Pizza

# Create your views here.
def index(request):
    pizzas = Pizza.objects.all().order_by('prix')
    # # for pizza in pizzas:
    # #     return HttpResponse(pizza.nom + str(pizza.prix))
        
    # pizzas_names_prices = [pizza.nom + ": " + str(pizza.prix) + "€ " for pizza in pizzas]
    # pizzas_names_prices_str = ", ".join(pizzas_names_prices) # permet de concatener et séparer la liste par une , 
    # return HttpResponse("Les pizzas: " + pizzas_names_prices_str)
    return render(request, 'menu/index.html', {'pizzas': pizzas})

def api_get_pizza(request):
    pizzas = Pizza.objects.all().order_by('prix')
    json = serializers.serialize("json", pizzas)
    return HttpResponse(json)