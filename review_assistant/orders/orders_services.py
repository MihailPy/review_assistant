import re
from datetime import date, timedelta, datetime
import random

from executors.models import Executor
from customers.models import Customer
from tasks.tasks_services import task_status
from tasks.models import Tasks

from .models import Image_order, Order


def boolean(i):
    if i == "on":
        return True
    else:
        return False


def save_order(request, order, customer):
    order.customer = customer
    order.date_order_start = request.POST.get("date_order_start")
    order.date_order_end = request.POST.get("date_order_end")
    order.amount = request.POST.get("amount")
    order.gender_man = boolean(request.POST.get("gender_man"))
    order.gender_woman = boolean(request.POST.get("gender_woman"))
    order.link_to_account = request.POST.get("link_to_account")
    order.text = request.POST.get("text")
    order.notes = request.POST.get("notes")
    order.prepayment = boolean(request.POST.get("prepayment"))
    order.paymant = boolean(request.POST.get("paymant"))
    order.hide_order = boolean(request.POST.get("hide_order"))
    order.save()
    return order


def save_images(img, order):
    print(img)
    image = Image_order()
    image.order = order
    image.img = img
    image.save()


def json_order(order, customer):
    return {'customer': customer,
            'date_order_start': order.date_order_start.strftime('%Y-%m-%d'),
            'date_order_end': order.date_order_end.strftime('%Y-%m-%d'),
            'amount': order.amount,
            'gender_man': order.gender_man,
            'gender_woman': order.gender_woman,
            'link_to_account': order.link_to_account,
            'text': order.text,
            'notes': order.notes,
            'prepayment': order.prepayment,
            'paymant': order.paymant,
            'hide_order': order.hide_order}


def date_frequence(start, end, amount):
    return (end - start) // amount


def get_img(img):
    return list((img[i], i) for i in range(0, len(img)))


def get_text_of_reviews(text):
    # Разделяем текст по решетке
    return re.split(r"[#]\s*", text)


def get_executors_list():
    # Выбераем исполнителей без задач или с задачами давностью неделя
    executors_list = []
    executors = Executor.objects.all()
    for executor in executors:
        te = Tasks.objects.filter(executor=executor)
        if len(te):
            te = sorted(te, key=lambda i: i.correspondence_date)
            if date.today() - timedelta(days=7) > te[0].date_of_withdrawal.date():
                executors_list.append(executor)
        else:
            executors_list.append(executor)

    return executors_list


def valid_order(order):
    # Проверяем на валидность заказ хватает ли исполнителей, текста и скриншотов
    valid = []
    valid_bool = True
    amount = order.amount
    num_rewiews = len(get_text_of_reviews(order.text))
    len_img = len(get_img(Image_order.objects.all().filter(order=order.id)))
    executors_len = len(get_executors_list())

    if num_rewiews < amount:
        valid.append({"text_reviews_error": True})
        valid_bool = False
    else:
        valid.append({"text_reviews_error": False})
    if len_img < amount:
        valid.append({"img_error": True})
        valid_bool = False
    else:
        valid.append({"img_error": False})
    if executors_len < amount:
        valid.append({"executors_error": True})
        valid_bool = False
    else:
        valid.append({"executors_error": False})
    return valid, valid_bool


def divide_into_tasks_func(id):
    order = Order.objects.get(id=id)
    _, valid = valid_order(order)
    if not len(Tasks.objects.all().filter(order=id)) and valid:
        executors_list = get_executors_list()
        date_start = order.date_order_start
        date_end = order.date_order_end
        task_texts = get_text_of_reviews(order.text)
        images = get_img(Image_order.objects.all().filter(order=id))

        for i in range(0, order.amount):
            task = Tasks()
            task.order = order
            task.image = images[i][0]
            task.executor = executors_list[i]
            task.text_review = task_texts[i]
            task.correspondence_date = date_start
            task.date_of_withdrawal = date_start + timedelta(random.randint(1, 2))
            task.hitch = False
            task.in_progres = False
            task.execution_or_no = False
            task.paymant = False
            # добавить время к дате
            date_start += timedelta(random.randint(1, 3))
            if date_start > date_end:
                date_start = order.date_order_start
            if task.date_of_withdrawal > date_end:
                task.date_of_withdrawal = date_end
            task.save()
