from datetime import datetime
from django.utils import timezone

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from jinja2 import Template
from .forms import Task_form, ImageForms
from .models import Tasks
from .tasks_services import json_task, save_task, task_status, save_images
from orders.models import Order
from executors.models import Executor


@login_required
def add_image(request, id):
    if request.method == "POST":
        task = Tasks.objects.get(id=id)
        task.date_of_writing_the_review = datetime.today()
        task.save()
        form = ImageForms(request.POST, request.FILES)
        if form.is_valid():
            save_images(request.FILES.get("image"), task, task.executor)
        return redirect("task", task.id)


@login_required
def confirm_execution(request, id):
    task = Tasks.objects.get(id=id)
    task.execution_or_no = True
    task.in_progres = False
    task.save()
    return redirect('task', task.id)


@login_required
def confirm_correspondence(request, id):
    task = Tasks.objects.get(id=id)
    print(datetime.today())
    print(task.correspondence_date)
    task.in_progres = True
    task.date_of_the_completed_correspondence = datetime.today()
    task.save()
    return redirect('task', task.id)


@login_required
def tasks_page(request):
    user = request.user
    if not user.is_staff:
        executor = Executor.objects.get(user=user)
        tasks = Tasks.objects.all().filter(executor=executor)
        tasks = task_status(tasks)
        return render(request, 'tasks/tasks_user.html', context={'tasks': tasks, })
    else:
        tasks = Tasks.objects.all()
        tasks = task_status(tasks)
        tasks_list = []
        orders = Order.objects.all()
        for order in orders:
            tasks_list.append(Tasks.objects.all().filter(order=order))
        zipped = dict(zipped=zip(orders, tasks_list))
        print(zipped)
        return render(request, 'tasks/tasks.html', context={'tasks_list': tasks_list,
                                                            'orders': zipped,
                                                            'orders_range': range(len(orders)),
                                                            })


@login_required
def task_page(request, id):
    task = Tasks.objects.get(id=id)
    form = ImageForms()

    return render(request, 'tasks/task.html', context={'task': task,
                                                       "datetime": datetime.today(),
                                                       "form": form})


@login_required
def edit_task_page(request, id):
    task = Tasks.objects.get(id=id)
    if request.method == "POST":
        form = Task_form(request.POST)
        if form.is_valid():
            task = save_task(form, task)
            return redirect('task', task.id)
            # return HttpResponseRedirect("/task/" + str(task.id))
    else:
        form = Task_form(json_task(task))
        return render(request, 'tasks/edit_task.html', context={'task': task, 'form': form})
