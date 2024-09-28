from django import forms
from .models import Player


class ChoosePlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ('name', 'life_points', 'color')
