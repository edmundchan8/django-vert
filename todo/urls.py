from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('add_task/', views.add_task, name='add_task'),
    path('complete_task/', views.complete_task, name='complete_task'),
]
