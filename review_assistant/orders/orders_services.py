import re
from executors.models import Executor
from .models import Image_order


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


def get_the_number_of_reviews(text):
    return len(re.split(r"[#]\s*", text))


def valid_order(order):
    valid = []
    amount = order.amount
    num_rewiews = get_the_number_of_reviews(order.text)
    len_img = len(get_img(Image_order.objects.all().filter(order=order.id)))
    executors_len = len(Executor.objects.all())

    if num_rewiews < amount:
        valid.append({"text_reviews_error": True})
    else:
        valid.append({"text_reviews_error": False})
    if len_img < amount:
        valid.append({"img_error": True})
    else:
        valid.append({"img_error": False})
    if executors_len < amount:
        valid.append({"executors_error": True})
    else:
        valid.append({"executors_error": False})

    return valid
