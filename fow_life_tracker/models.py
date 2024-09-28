from django.utils.translation import gettext_lazy as _
from django.db import models

# Create your models here.


class Player(models.Model):

    class PlayerColor(models.TextChoices):
        BLUE = 'blue', _('Blue')
        GREEN = 'green', _('Green')
        YELLOW = 'yellow', _('Yellow')
        RED = 'red', _('Red')
        ORANGE = 'orange', _('Orange')
        PURPLE = 'purple', _('Purple')

    name = models.CharField(max_length=100, default='Player')
    life_points = models.PositiveIntegerField(default=4000)
    color = models.CharField(
        max_length=6,
        choices=PlayerColor.choices,
    )

    def __str__(self):
        return f"{self.name} Life Points {self.life_points} color {self.color}"
