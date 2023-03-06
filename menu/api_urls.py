from django.urls import path
from . import views

app_name = 'menu'

urlpatterns = [
    path('getPizzas', views.api_get_pizza),
]