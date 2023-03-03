from django.contrib import admin
from .models import Pizza #on import la class

class PizzaAdmin(admin.ModelAdmin):
    list_display = ('nom', 'vegetarienne', 'ingredients', 'prix') # on personnalise l'affichage dans le menu
    search_fields = ['nom', 'ingredients'] # permet d'ajouter un search (qui search sur nom & ingredients)

# Register your models here.
admin.site.register(Pizza, PizzaAdmin) # on ajoute dans le panel admin afin de pouvoir CRUD les pizza

