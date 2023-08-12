from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from .forms import OrderForms, PhotoForms
from .models import Order, Image_order
from .orders_services import save_images, save_order, json_order, date_frequence, get_img, \
    valid_order, divide_into_tasks_func
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
    frequence_res = date_frequence(order.date_order_start, order.date_order_end, order.amount)
    valid, _ = valid_order(order)
    customer = order.customer
    img = get_img(Image_order.objects.all().filter(order=id))
    tasks = Tasks.objects.all().filter(order=id)
    executors = Executor.objects.all()
    tasks = task_status(tasks)
    return render(request, 'orders/order.html',
                  context={'id': id, 'order': order, 'frequence': frequence_res, 'customer': customer, 'img': img,
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
    divide_into_tasks_func(id)
    return redirect("order", id)
