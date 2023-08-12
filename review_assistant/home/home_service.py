from tasks.models import Tasks
from datetime import date, timedelta, datetime
from tasks.tasks_services import task_status


def get_before(executor):
    yesterday = date.today() + timedelta(days=-1)
    tasks_befor = []
    for task in Tasks.objects.all().filter(executor=executor):
        if task.correspondence_date.date() < yesterday and task.date_of_the_completed_correspondence is None or task.date_of_withdrawal.date() < yesterday and task.date_of_writing_the_review is None:
            tasks_befor.append(task)
            print(True)
    if len(tasks_befor):
        return tasks_befor
    return False


def get_yesterday(executor):
    yesterday = date.today() + timedelta(days=-1)
    tasks_yesterday = []
    if not executor:
        for task in Tasks.objects.all():
            if task.correspondence_date.date() == yesterday or task.date_of_withdrawal.date() == yesterday:
                tasks_yesterday.append(task)
    else:
        for task in Tasks.objects.all().filter(executor=executor):
            if task.correspondence_date.date() == yesterday or task.date_of_withdrawal.date() == yesterday:
                tasks_yesterday.append(task)
    task_status(tasks_yesterday)
    if len(tasks_yesterday):
        return tasks_yesterday
    return False


def get_today(executor):
    today = date.today()
    tasks_today = []
    if not executor:
        for task in Tasks.objects.all():
            if task.correspondence_date.date() == today or task.date_of_withdrawal.date() == today:
                tasks_today.append(task)
    else:
        for task in Tasks.objects.all().filter(executor=executor):
            if task.correspondence_date.date() == today or task.date_of_withdrawal.date() == today:
                tasks_today.append(task)
    task_status(tasks_today)
    if len(tasks_today):
        return tasks_today
    return False


def get_tomorrow(executor):
    tomorrow = date.today() + timedelta(days=+1)
    tasks_tomorrow = []
    if not executor:
        for task in Tasks.objects.all():
            if task.correspondence_date.date() == tomorrow or task.date_of_withdrawal.date() == tomorrow:
                tasks_tomorrow.append(task)
    else:
        for task in Tasks.objects.all().filter(executor=executor):
            if task.correspondence_date.date() == tomorrow or task.date_of_withdrawal.date() == tomorrow:
                tasks_tomorrow.append(task)
    task_status(tasks_tomorrow)
    if len(tasks_tomorrow):
        return tasks_tomorrow
    return False


def get_after(executor):
    tomorrow = date.today() + timedelta(days=+1)
    tasks_after = []
    for task in Tasks.objects.all().filter(executor=executor):
        if task.correspondence_date.date() > tomorrow or task.date_of_withdrawal.date() > tomorrow:
            tasks_after.append(task)
    if len(tasks_after):
        return tasks_after
    return False
