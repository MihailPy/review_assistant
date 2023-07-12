def save_executor(form, executor):
    executor.name = form.cleaned_data["name"]
    executor.last_name = form.cleaned_data["last_name"]
    executor.phone = form.cleaned_data["phone"]
    executor.gender = form.cleaned_data["gender"]
    executor.link_to_account = form.cleaned_data["link_to_account"]
    executor.telegram_id = form.cleaned_data["telegram_id"]
    executor.date_create = form.cleaned_data["date_create"]
    executor.save()
    return executor


def json_executor(executor):
    return {"name": executor.name,
            "last_name": executor.last_name,
            "phone": executor.phone,
            "link_to_account": executor.link_to_account,
            "telegram_id": executor.telegram_id,
            "date_create": executor.date_create.strftime('%Y-%m-%d'), }
