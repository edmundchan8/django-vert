from django.shortcuts import render
from .models import Recipe

# Create your views here.


def index(request):
    recipes = Recipe.objects.all()
    return render(request, 'coffee_recipes/coffee_recipe.html', {'recipes': recipes})


def add_recipe(request):
    return render(request, 'coffee_recipes/add_recipe.html')
