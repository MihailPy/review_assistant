from datetime import date, time, datetime, timedelta

from orders.models import Image_order, Order

from executors.models import Executor

from .models import Image_user
from notification.models import Notification


def save_images(img, task, executor):
    print(img)
    image = Image_user()
    image.task = task
    image.img = img
    image.executor = executor
    image.save()


def json_task(task):
    print(task.correspondence_date)
    return {'image': task.image.id,
            'text_review': task.text_review,
            'correspondence_date': task.correspondence_date.strftime('%Y-%m-%dT%H:%M'),
            'date_of_withdrawal': task.date_of_withdrawal.strftime('%Y-%m-%dT%H:%M'),
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
    task.paymant = form.cleaned_data['paymenti']
    task.hitch = form.cleaned_data['hitch']
    task.save()
    return task


def task_status(tasks):
    for task in tasks:
        task.executor_id = Executor.objects.all().get(id=task.executor_id)
        if date.today() > task.correspondence_date.date() and None == task.date_of_the_completed_correspondence:
            task.hitch = True
            task.in_progres = False
            task.save()
        elif date.today() > task.date_of_withdrawal.date() and None == task.date_of_writing_the_review:
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
        if task.correspondence_date < datetime.now() < task.correspondence_date+timedelta(minutes=59):
            if Notification.objects.filter(task=task):
                pass
            else:
                notify = Notification()
                notify.user = task.executor_id.user
                notify.header = "Задача на выполнение"
                notify.body = "Начните переписку"
                notify.datetime_notify = task.correspondence_date
                notify.task = task
                notify.shown = False
                notify.save()
        if task.date_of_withdrawal < datetime.now() < task.date_of_withdrawal+timedelta(minutes=59):
            if Notification.objects.filter(task=task).filter(datetime_notify=task.date_of_withdrawal):
                pass
            else:
                notify = Notification()
                notify.user = task.executor_id.user
                notify.header = "Задача на выполнение"
                notify.body = "Напишите отзыв"
                notify.datetime_notify = task.date_of_withdrawal
                notify.task = task
                notify.shown = False
                notify.save()
    return sorted(tasks, key=lambda i: i.correspondence_date)
