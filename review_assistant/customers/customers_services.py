def save_customer(form, customer):
    customer.name = form.cleaned_data["name"]
    customer.last_name = form.cleaned_data["last_name"]
    customer.tg_un = form.cleaned_data["username"]
    customer.phone = form.cleaned_data["phone"]
    customer.notes = form.cleaned_data["notse"]
    customer.save()

    return customer


def json_customer(customer):
    return {"name": customer.name,
            "last_name": customer.last_name,
            "phone": customer.phone,
            "username": customer.tg_un,
            "notes": customer.notes}


