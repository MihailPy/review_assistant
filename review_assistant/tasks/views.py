from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import Task_form
from .models import Tasks
from .tasks_services import json_task, save_task, task_status
from orders.models import Order


def tasks_page(request):
    tasks = Tasks.objects.all()
    tasks = task_status(tasks)
    orders = Order.objects.all()
    return render(request, 'tasks/tasks.html', context={'tasks': tasks, 'orders': orders})


def task_page(request, id):
    task = Tasks.objects.get(id=id)

    return render(request, 'tasks/task.html', context={'task': task, })


def edit_task_page(request, id):
    task = Tasks.objects.get(id=id)
    if request.method == "POST":
        form = Task_form(request.POST)
        if form.is_valid():
            task = save_task(form, task)
            return HttpResponseRedirect("/task/" + str(task.id))
    else:
        form = Task_form(json_task(task))
        return render(request, 'tasks/edit_task.html', context={'task': task, 'form': form})
