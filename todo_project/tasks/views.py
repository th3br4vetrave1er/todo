from django.shortcuts import render, redirect
from .models import Task
# Create your views here.


def task_list(request):
    tasks = Task.objects.all()  # получаем все задачи
    return render(request, 'tasks/task_list.html', {'task': tasks})


def add_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST.get('description', '')
        Task.objects.create(title=title, description=description)
        return redirect('task_list')
    return render(request, 'tasks/add_task.html')


def complete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = True
    task.save()
    return redirect('task_list')
