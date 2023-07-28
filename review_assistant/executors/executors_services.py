def save_executor(form, executor, request):
    executor.name = form.cleaned_data["name"]
    executor.last_name = form.cleaned_data["last_name"]
    executor.phone = form.cleaned_data["phone"]
    executor.gender = form.cleaned_data["gender"]
    executor.link_to_account = form.cleaned_data["link_to_account"]
    executor.card_number = form.cleaned_data["card_number"]
    executor.date_create = form.cleaned_data["date_create"]
    executor.user = request.user
    executor.save()
    return executor


def json_executor(executor):
    print(executor.date_create)
    if executor.date_create is not None:
        date = executor.date_create.strftime('%Y-%m-%d')
    else:
        date = executor.date_create
    return {"name": executor.name,
            "last_name": executor.last_name,
            "phone": executor.phone,
            "link_to_account": executor.link_to_account,
            "card_number": executor.card_number,
            "date_create": date,
            "gender": executor.gender}
