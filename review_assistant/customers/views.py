from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render

from .customers_services import save_customer, json_customer
from .forms import Customer_form
from .models import Customer


def customer_page(request, id):
    customer = Customer.objects.get(id=id)
    return render(request, 'customers/customer.html', context={'customer': customer, })


def customers_page(request):
    customers = Customer.objects.all()

    return render(request, 'customers/customers.html', context={'customers': customers})


def create_customer_page(request):
    try:
        if request.method == "POST":
            form = Customer_form(request.POST)
            if form.is_valid():
                customer = save_customer(form, Customer())
                print(customer.id)
            return HttpResponseRedirect("/customer/" + str(customer.id))

        else:
            customers = Customer.objects.all()
            customer_form = Customer_form()
            return render(request, 'customers/create_customer.html', context={'customers': customers,
                                                                              'form': customer_form, })
    except:
        raise Http404("Заказчик не найден")


def edit_customer_page(request, id):
    try:
        customer = Customer.objects.get(id=id)
        if request.method == "POST":
            form = Customer_form(request.POST)
            if form.is_valid():
                customer = save_customer(form, customer)
            return HttpResponseRedirect("/customer/" + str(customer.id))
        else:
            customer_form = Customer_form(json_customer(customer))
            return render(request, 'customers/edit_customer.html', context={'customer': customer,
                                                                            'form': customer_form, })
    except:
        raise Http404("Заказчик не найден")


def delete_customer(request, id):
    try:
        customer = Customer.objects.get(id=id)
        customer.delete()
        return HttpResponseRedirect("/customers/")
    except Customer.DoesNotExist:
        raise Http404("Заказчик не найден")
