from django.shortcuts import render
from .models import Pizza

# Create your views here.
def index(request):
    pizzas = Pizza.objects.all()
    # # for pizza in pizzas:
    # #     return HttpResponse(pizza.nom + str(pizza.prix))
        
    # pizzas_names_prices = [pizza.nom + ": " + str(pizza.prix) + "€ " for pizza in pizzas]
    # pizzas_names_prices_str = ", ".join(pizzas_names_prices) # permet de concatener et séparer la liste par une , 
    # return HttpResponse("Les pizzas: " + pizzas_names_prices_str)
    return render(request, 'menu/index.html', {'pizzas': pizzas})