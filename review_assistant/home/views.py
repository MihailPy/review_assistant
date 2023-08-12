from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from executors.models import Executor
from .home_service import *


@login_required
def home(request):
    webpush_settings = getattr(settings, 'WEBPUSH_SETTINGS', {})
    vapid_key = webpush_settings.get('VAPID_PUBLIC_KEY')
    user = request.user
    if not user.is_staff:
        executor = Executor.objects.get(user=user)
        today = get_today(executor)
        tomorrow = get_tomorrow(executor)
        after = get_after(executor)
        return render(request, 'home/home_page.html', {'user': user,
                                                       'executor': executor,
                                                       'today': today,
                                                       'tomorrow': tomorrow,
                                                       'after': after,
                                                       "datetime": datetime.today(),
                                                       'vapid_key': vapid_key})
    else:
        yesterday = get_yesterday(False)
        today = get_today(False)
        tomorrow = get_tomorrow(False)
        return render(request, 'home/home_admin.html', {'user': user,
                                                        'today': today,
                                                        'tomorrow': tomorrow,
                                                        'yesterday': yesterday
                                                        'vapid_key': vapid_key})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            username = form.cleaned_data.get('username')
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            messages.success(request, f'Создан аккаунт {username}!')
            executor = Executor()
            executor.user = new_user
            executor.name = new_user.first_name
            executor.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'home/register.html', {'form': form})
