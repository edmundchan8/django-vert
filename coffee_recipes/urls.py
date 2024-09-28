from django.urls import path
from . import views

urlpatterns = [
    path('coffee_recipes/', views.index, name='coffee_recipes'),
    path('add_recipe/', views.add_recipe, name='add_recipe'),
]
