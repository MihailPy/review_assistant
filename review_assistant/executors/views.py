from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render

from .executors_services import save_executor, json_executor
from .forms import Executor_form
from .models import Executor


def executor_page(request, id):
    try:
        executor = Executor.objects.get(id=id)
        return render(request, 'executors/executor.html', context={'executor': executor, })
    except Executor.DoesNotExist:
        raise Http404("Исполнитель не найден")


def executors_page(request):
    executors = Executor.objects.all()

    return render(request, 'executors/executors.html', context={'executors': executors, })


def create_executor_page(request):
    try:
        if request.method == "POST":
            form = Executor_form(request.POST)
            if form.is_valid():
                executor = save_executor(form, Executor())
                return HttpResponseRedirect("/executor/" + str(executor.id))
        else:
            executor = Executor.objects.all()
            executor_form = Executor_form()
            return render(request, 'executors/create_executor.html', context={'executor': executor,
                                                                              'form': executor_form, })
    except Executor.DoesNotExist:
        raise Http404("Исполнитель не найден")


def edit_executor_page(request, id):
    try:
        executor = Executor.objects.get(id=id)
        if request.method == "POST":
            form = Executor_form(request.POST)
            if form.is_valid():
                executor = save_executor(form, executor)
                return HttpResponseRedirect("/executor/" + str(executor.id))
        else:
            executor_form = Executor_form(json_executor(executor))
            return render(request, 'executors/edit_executor.html', context={'executor': executor,
                                                                            'form': executor_form, })
    except Executor.DoesNotExist:
        raise Http404("Исполнитель не найден")


def delete_executor(request, id):
    try:
        executor = Executor.objects.get(id=id)
        executor.delete()
        return HttpResponseRedirect("/executors/")
    except Executor.DoesNotExist:
        raise Http404("Исполнитель не найден")
