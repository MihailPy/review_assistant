from django import forms

from .models import Order


class OrderForms(forms.Form):
    model = Order
    customer = forms.CharField(label="Заказчик", required=False,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    date_order_start = forms.DateField(label="С какой даты",
                                       widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    date_order_end = forms.DateField(label="До какой даты",
                                     widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    amount = forms.CharField(label="Кол-во отзывов",
                             widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}))
    gender_man = forms.CharField(label="Мужские", required=False,
                                 widget=forms.CheckboxInput(
                                     attrs={'class': 'form-check-input', 'type': 'checkbox', 'checked': True}))
    gender_woman = forms.CharField(label="Женские", required=False,
                                   widget=forms.CheckboxInput(
                                       attrs={'class': 'form-check-input', 'type': 'checkbox', 'checked': True, }))
    photo = forms.ImageField(label="Фото обявлений", required=False,
                             widget=forms.ClearableFileInput(attrs={'class': 'form-control', 'multiple': True}))
    link_to_account = forms.URLField(label="Ссылка на обявление",
                                     widget=forms.TextInput(attrs={'class': 'form-control'}))
    text = forms.CharField(label="Отзывы", widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    notes = forms.CharField(label="Заметки", required=False,
                            widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}))
    prepayment = forms.CharField(label="Предоплата", required=False,
                                 widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'type': 'checkbox', }))
    paymant = forms.CharField(label="Оплата", required=False,
                              widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'type': 'checkbox', }))
    hide_order = forms.CharField(label="Скрыть", required=False,
                                 widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'type': 'checkbox'}))
    fields = ('customer', 'date_order_start', 'date_order_end', 'amount', 'gender_man', 'gender_woman', 'photo',
              'link_to_account', 'text',
              'notes', 'prepayment', 'paymant', 'hide_order')
