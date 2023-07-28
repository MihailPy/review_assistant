from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from executors.models import Executor


@login_required
def home(request):
    user = request.user
    if not user.is_staff:
        executor = Executor.objects.get(user=user)
        return render(request, 'home/home_page.html', {'user': user, 'executor': executor})
    return redirect("home_admin")




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
