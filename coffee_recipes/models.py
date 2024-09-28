from django.db import models
from taggit.managers import TaggableManager

# Create your models here.


class Recipe(models.Model):
    title = models.CharField(max_length=255)
    rating = models.PositiveIntegerField()
    grind = models.DecimalField(max_digits=50, decimal_places=2)
    instructions = models.TextField()
    tags = TaggableManager()

