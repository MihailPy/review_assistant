from django import forms

from .models import Customer


class Customer_form(forms.Form):
    model = Customer()
    name = forms.CharField(label="Имя", widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label="Фамилия", widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.URLField(label="Username", widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.IntegerField(label="Телефон", widget=forms.TextInput(attrs={'class': 'form-control'}))
    notse = forms.CharField(label="Заметки", required=False, widget=forms.Textarea(attrs={'class': 'form-control'}))
    fields = ('name', 'last_name', 'phone', 'username', 'notes')

