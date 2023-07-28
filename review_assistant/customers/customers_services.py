import re


def save_customer(form, customer):
    customer.name = form.cleaned_data["name"]
    customer.last_name = form.cleaned_data["last_name"]
    un_re = re.compile(r"^@(\w)+")
    if un_re.search(form.cleaned_data["username"]):
        customer.tg_un = "https://t.me/"+form.cleaned_data["username"][1:]
    else:
        customer.tg_un = form.cleaned_data["username"]
    customer.phone = form.cleaned_data["phone"]
    customer.notes = form.cleaned_data["notes"]
    customer.save()

    return customer


def json_customer(customer):
    return {"name": customer.name,
            "last_name": customer.last_name,
            "phone": customer.phone,
            "username": customer.tg_un,
            "notes": customer.notes}
