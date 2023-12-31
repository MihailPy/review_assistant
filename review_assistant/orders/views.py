import re
from datetime import date, timedelta, datetime
import random

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from .forms import OrderForms, PhotoForms
from .models import Order, Image_order
from .orders_services import save_images, save_order, json_order, date_frequence, get_img, get_the_number_of_reviews, \
    valid_order
from executors.models import Executor
from customers.models import Customer
from tasks.models import Tasks

from tasks.tasks_services import task_status


@login_required
def orders_page(request):
    orders = Order.objects.all()
    tasks = Tasks.objects.all()

    return render(request, 'orders/orders.html', context={'orders': orders, 'tasks': tasks, })


@login_required
def create_order_page(request, id):
    orders = Order.objects.all()
    customer = Customer.objects.get(id=id)
    if request.method == "POST":
        form = OrderForms(request.POST)
        order = save_order(request, Order(), customer)
        return redirect("order", order.id)
    else:
        form = OrderForms()
        return render(request, 'orders/create_order.html', context={'id': id,
                                                                    'form': form,
                                                                    'orders': orders,
                                                                    'customer': customer, })


@login_required
def edit_order_page(request, id):
    order = Order.objects.get(id=id)
    customer = order.customer
    if request.method == "POST":
        form = OrderForms(request.POST)
        order = save_order(request, order, customer)
        return redirect("order", order.id)
    else:
        form = OrderForms(json_order(order, customer))
        return render(request, 'orders/edit_order.html', context={'id': id,
                                                                  'form': form,
                                                                  'order': order,
                                                                  'customer': customer, })


@login_required
def order_page(request, id):
    order = Order.objects.get(id=id)
    frequence = date_frequence(order.date_order_start, order.date_order_end, order.amount)
    numbers_text = get_the_number_of_reviews(order.text)
    valid = valid_order(order)
    customer = order.customer
    img = get_img(Image_order.objects.all().filter(order=id))
    tasks = Tasks.objects.all().filter(order=id)
    executors = Executor.objects.all()
    tasks = task_status(tasks)
    return render(request, 'orders/order.html',
                  context={'id': id, 'order': order, 'frequence': frequence, 'customer': customer, 'img': img,
                           'tasks': tasks, 'executors': executors, 'valid': valid, })


@login_required
def edit_img(request, id):
    if request.method == "POST":
        form = PhotoForms(request.POST, request.FILES)
        if form.is_valid():
            order = Order.objects.get(id=id)
            save_images(request.FILES.get("photo"), order)
        return redirect("edit_img", id)
    else:
        form = PhotoForms()
        img = get_img(Image_order.objects.all().filter(order=id))
        return render(request, 'orders/edit_image.html', context={'form': form, 'id': id, 'img': img})


@login_required
def delete_img(request, id):
    img = Image_order.objects.get(id=id)
    order_id = img.order.id
    img.delete()
    return redirect("edit_img", order_id)


@login_required
def divide_into_tasks(request, id):
    order = Order.objects.get(id=id)
    valid = valid_order(order)
    v = []
    for i in valid:
        if list(i.values())[0]:
            v.append(True)
    print(not len(Tasks.objects.all().filter(order=id)), not len(v))
    if not len(Tasks.objects.all().filter(order=id)) and not len(v):
        try:
            executors = Executor.objects.all()
            executors_list = []
            for executor in executors:
                te = Tasks.objects.filter(executor=executor)
                if len(te):
                    te = sorted(te, key=lambda i: i.correspondence_date)
                    if date.today()-timedelta(days=7) > te[0].date_of_withdrawal.date():
                        executors_list.append(executor)
            date_start = order.date_order_start
            date_end = order.date_order_end
            images = get_img(Image_order.objects.all().filter(order=id))

            task_texts = re.split(r"[#]\s*", order.text)
            # print(task_texts)
            # print(order.date_order_start, order.date_order_end)
            frequence = date_frequence(order.date_order_start, order.date_order_end, order.amount)
            for i in range(0, order.amount):
                task = Tasks()
                task.order = order
                task.image = images[i][0]
                task.executor = executors[i]
                task.text_review = task_texts[i]
                # print(Tasks.objects.all().filter(executor=executors[i]))
                if len(Tasks.objects.all().filter(executor=executors[i])) != 0:
                    t = Tasks.objects.all().filter(executor=executors[i])
                    ta = (t[0].date_of_withdrawal + timedelta(days=7)).date()
                    # print(date_start)
                    # print(date_start > ta)
                task.correspondence_date = date_start
                task.date_of_withdrawal = date_start + timedelta(random.randint(1, 2))
                task.hitch = False
                task.in_progres = False
                task.execution_or_no = False
                task.paymant = False
                date_start += timedelta(random.randint(1, 3))
                if date_start > date_end:
                    date_start = order.date_order_start
                if task.date_of_withdrawal > date_end:
                    task.date_of_withdrawal = date_end
                # task.save()
        except Exception as error:
            print(error)

    return redirect("order", order.id)
