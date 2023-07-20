from django import forms

from .models import Tasks
from executors.models import Executor
from orders.models import Image_order


class Task_form(forms.Form):
    model = Tasks
    choices = list((i.id, i.id) for i in Image_order.objects.all())
    image = forms.ChoiceField(label="Скриншот обявления", choices=choices,
                              widget=forms.Select(attrs={'class': 'form-select'}))
    text_review = forms.CharField(label="Текст отзыва", widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    correspondence_date = forms.DateTimeField(label="Дата переписки",
                                              widget=forms.DateTimeInput(attrs={'class': 'form-control'}))
    date_of_withdrawal = forms.DateTimeField(label="Дата отзыва",
                                             widget=forms.DateTimeInput(attrs={'class': 'form-control'}))
    execution_or_no = forms.CharField(label="Исполнено?", required=False,
                                      widget=forms.CheckboxInput(
                                          attrs={'class': 'form-check-input', 'type': 'checkbox', }))
    paymant = forms.CharField(label="Оплата?", required=False,
                              widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'type': 'checkbox', }))
    hitch = forms.CharField(label="Заминка?", required=False,
                            widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'type': 'checkbox', }))
    fields = ('image','text_review','correspondence_date','date_of_withdrawal','execution_or_no','paymant','hitch',)