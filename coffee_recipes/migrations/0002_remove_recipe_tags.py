# Generated by Django 5.0.3 on 2024-05-08 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coffee_recipes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='tags',
        ),
    ]
