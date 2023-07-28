from django import forms

from .models import Executor


class Executor_form(forms.Form):
    model = Executor
    name = forms.CharField(label="Имя", widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label="Фамилия", widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(label="Телефон", widget=forms.TextInput(attrs={'class': 'form-control'}))
    card_number = forms.CharField(label="Номер карты для перевода", widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'cardnumber', 'pattern': "[0-9]*", 'inputmode': 'numeric'}))
    date_create = forms.DateField(label="Дата создания акк",
                                  widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    link_to_account = forms.URLField(label="Ссылка на аккаунт", widget=forms.TextInput(attrs={'class': 'form-control'}))
    gender = forms.ChoiceField(label="Пол аккаунта", choices=(("man", "Мужской"), ("woman", "Женский")),
                               widget=forms.Select(attrs={'class': 'form-select'}))
    fields = ('name', 'last_name', 'date_create', 'phone', 'link_to_account', 'card_number')
