from datetime import date, time, datetime

from orders.models import Image_order, Order

from executors.models import Executor

from orders.orders_services import date_frequence, get_the_number_of_reviews
from .models import Tasks


def json_task(task):
    return {'image': task.image.id,
            'text_review': task.text_review,
            'correspondence_date': task.correspondence_date,
            'date_of_withdrawal': task.date_of_withdrawal,
            'execution_or_no': task.execution_or_no,
            'paymant': task.paymant,
            'hitch': task.hitch,
            }


def save_task(form, task):
    task.image = Image_order.objects.get(id=form.cleaned_data['image'])
    task.text_review = form.cleaned_data['text_review']
    task.correspondence_date = form.cleaned_data['correspondence_date']
    task.date_of_withdrawal = form.cleaned_data['date_of_withdrawal']
    task.execution_or_no = form.cleaned_data['execution_or_no']
    task.paymant = form.cleaned_data['paymant']
    task.hitch = form.cleaned_data['hitch']
    task.save()
    return task


def task_status(tasks):
    for task in tasks:
        task.executor_id = Executor.objects.all().get(id=task.executor_id)
        if date.today() > task.correspondence_date.date() and None == task.date_of_the_completed_correspondence \
                and task.in_progres == False:
            task.hitch = True
            task.in_progres = False
            task.save()
        elif date.today() > task.date_of_withdrawal.date() and None == task.date_of_writing_the_review \
                and task.in_progres == False:
            task.hitch = True
            task.in_progres = False
            task.save()
        elif date.today() == task.correspondence_date.date() or date.today() == task.date_of_withdrawal.date():
            task.hitch = False
            task.in_progres = True
            task.save()
        # elif date.today() < task.date_of_the_completed_correspondence or date.today() == task.date_of_writing_the_review.date():
        #     task.hitch = False
        #     task.in_progres = False
        #     task.save()
        else:
            task.hitch = False
            task.in_progres = False
            task.save()
    return sorted(tasks, key=lambda i: i.correspondence_date)
