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


def save_images(request):
    if request.FILES.getlist("photo") is not None:
        for p in request.FILES.getlist("photo"):
            image = Image_order()
            image.img = p
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
