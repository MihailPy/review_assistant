from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import OrderForms
from .models import Order
from .orders_services import save_images, save_order, json_order
from ..customers.models import Customer


def orders_page(request):
    orders = Order.objects.all()
    # tasks = Tasks.objects.all()

    return render(request, 'sucks/orders.html', context={'orders': orders, 'tasks': tasks, })


def create_order(request, id):
    orders = Order.objects.all()
    customer = Customer.objects.get(id=id)
    if request.method == "POST":
        form = OrderForms(request.POST)
        order = save_order(request, Order(), customer)
        save_images(request)
        return HttpResponseRedirect("/order/" + str(order.id))
    else:
        form = OrderForms()
        return render(request, 'sucks/create_order.html', context={'id': id,
                                                                   'form': form,
                                                                   'orders': orders,
                                                                   'customer': customer, })


def edit_order(request, id):
    order = Order.objects.get(id=id)
    customer = Customer.objects.get(id=order.customer.id)
    if request.method == "POST":
        form = OrderForms(request.POST)
        order = save_order(request, order, customer)
        save_images(request)
        return HttpResponseRedirect("/order/" + str(order.id))
    else:
        form = OrderForms(json_order(order, customer))
        return render(request, 'sucks/edit_order.html', context={'id': id,
                                                                 'form': form,
                                                                 'order': order,
                                                                 'customer': customer, })


def order(request, id):
    order = Order.objects.get(id=id)
    customer = order.customer
    img = Image_order.objects.all().filter(order=id)
    tasks = Tasks.objects.all().filter(order=id)
    executors = Executor.objects.all()
    print(tasks)
    for task in tasks:
        task.executor_id = Executor.objects.all().get(id=task.executor_id)
        print(date.today(), task.date_of_completion)
        print(date.today() < task.date_of_completion)
        print(date.today() > task.date_of_completion)
        print(date.today() == task.date_of_completion)
        print(type(task.execution_date))
        print(task.in_progres)
        # print(task.executor_id)
        if date.today() > task.date_of_completion and None == task.execution_date and task.in_progres == False:
            task.hitch = True
            task.in_progres = False
            task.save()
            print(1)
        elif date.today() == task.date_of_completion:
            task.hitch = False
            task.in_progres = True
            task.save()
            print(2)
        elif date.today() < task.date_of_completion:
            task.hitch = False
            task.in_progres = False
            task.save()
            print(3)
        else:
            task.hitch = False
            task.in_progres = False
            task.save()
            print(4)
    l = list((img[i], i) for i in range(0, len(img)))
    return render(request, 'sucks/order.html',
                  context={'id': id, 'order': order, 'customer': customer, 'img': img,
                           'tasks': tasks, 'executors': executors, 'l': l})
