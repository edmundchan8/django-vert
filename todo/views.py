from django.shortcuts import render, redirect, HttpResponse
from .models import Task


# Create your views here.
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'todo/task_list.html', {'tasks': tasks})


def add_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        new_task = Task(title=title)
        new_task.save()
        return redirect('task_list')

    return render(request, 'todo/add_task.html')


def complete_task(request):
    if request.method == 'POST':
        task = Task.objects.get(pk=request.POST.get('id'))
        task.completed = True
        task.save()
        tasks = Task.objects.all()
        return render(request, 'todo/task_list.html', {'tasks': tasks})
