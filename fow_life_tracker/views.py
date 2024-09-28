from django.shortcuts import render
from .models import Player
from .forms import ChoosePlayerForm
# Create your views here.


def fow_life_tracker(request):
    form = ChoosePlayerForm()
    new_player = []
    if request.method == "POST":
        name = request.POST['name']
        life_points = request.POST['life_points']
        color = request.POST['color']
        new_player = Player(name=name, life_points=life_points, color=color)
        new_player.save()

    return render(request, "fow_life_tracker/index.html", {'form': form, 'players': new_player})
