from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, redirect

from .executors_services import save_executor, json_executor
from .forms import Executor_form
from .models import Executor


@login_required
def executor_page(request, id):
    try:
        executor = Executor.objects.get(id=id)
        return render(request, 'executors/executor.html', context={'executor': executor, })
    except Executor.DoesNotExist:
        raise Http404("Исполнитель не найден")


@login_required
def executors_page(request):
    executors = Executor.objects.all()

    return render(request, 'executors/executors.html', context={'executors': executors, })


def create_executor_page(request):
    try:
        if request.method == "POST":
            form = Executor_form(request.POST)
            if form.is_valid():
                executor = save_executor(form, Executor(), request)
                return redirect("home")
        else:
            print(request.user)
            executor = Executor.objects.all()
            executor_form = Executor_form()
            return render(request, 'executors/create_executor.html', context={'executor': executor,
                                                                              'form': executor_form, })
    except Executor.DoesNotExist:
        raise Http404("Исполнитель не найден")


@login_required
def edit_profile_page(request):
    try:
        executor = Executor.objects.get(user=request.user)
        if request.method == "POST":
            form = Executor_form(request.POST)
            if form.is_valid():
                executor = save_executor(form, executor, request)
                return redirect("profile")
        else:
            executor_form = Executor_form(json_executor(executor))
            return render(request, 'executors/edit_profile.html', context={'executor': executor,
                                                                            'form': executor_form, })
    except Executor.DoesNotExist:
        raise Http404("Исполнитель не найден")


@login_required
def delete_executor(request, id):
    try:
        executor = Executor.objects.get(id=id)
        executor.delete()
        return redirect("executors")
    except Executor.DoesNotExist:
        raise Http404("Исполнитель не найден")


@login_required
def profile(request):
    try:
        executor = Executor.objects.get(user=request.user)
        return render(request, 'executors/profile.html', context={'executor': executor, })
    except Executor.DoesNotExist:
        raise Http404("Профиль не найден")
