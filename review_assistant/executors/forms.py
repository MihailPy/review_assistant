from django import forms

from .models import Executor


class Executor_form(forms.Form):
    model = Executor
    name = forms.CharField(label="Имя", widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label="Фамилия", widget=forms.TextInput(attrs={'class': 'form-control'}))
    date_create = forms.DateField(label="Дата создания акк",
                                  widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    link_to_account = forms.URLField(label="Ссылка", widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(label="Телефон", widget=forms.TextInput(attrs={'class': 'form-control'}))
    telegram_id = forms.CharField(label="Телеграм id", widget=forms.TextInput(attrs={'class': 'form-control'}))
    gender = forms.ChoiceField(label="Пол", choices=(("man", "Мужской"),("woman", "Женский")), widget=forms.Select(attrs={'class': 'form-select'}))
    fields = ('name', 'last_name', 'date_create', 'phone', 'link_to_account', "telegram_id")
