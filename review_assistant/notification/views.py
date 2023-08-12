from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render
from executors.models import Executor
from tasks.models import Tasks
from .models import Notification


@login_required
def get_notification(request):
    user = request.user
    notifys = Notification.objects.filter(user=user)
    json = {}
    for notify in notifys:
        json[str(notify.id)] = {"header": notify.header,
                                "body": notify.body,
                                "datetime_notify": notify.datetime_notify.strftime('%Y-%m-%dT%H:%M'),
                                "task": notify.task.id,
                                "shown": notify.shown,
                                }
    return JsonResponse(json)
    # raise Http404("Исполнитель не найден")
    # response = HttpResponse({})
    # response.set_cookie('name', 'jujule')
    # return response
    # cookie = request.COOKIES['java-tutorial']
    # return HttpResponse()


@login_required
def shown_notification(request, id):
    notify = Notification.objects.get(id=id)
    notify.shown = True
    print("+"*10)
    notify.save()
    return HttpResponse(status=200)
