from django.urls import path
from . import views

urlpatterns = [
    path('', views.fow_life_tracker, name='fow_life_tracker'),
    # path('choose_player/', views.choose_player, name='choose_player')
]
