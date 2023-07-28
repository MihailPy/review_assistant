from django.contrib.auth.models import User
from django.db import models


class Executor(models.Model):
    name = models.CharField(max_length=35, help_text="Введите имя исполнителя", verbose_name="Имя исполнителя")
    last_name = models.CharField(max_length=35, help_text="Введите фамилию исполнителя",
                                 verbose_name="Фамилия исполнителя", null=True)
    date_create = models.DateField(help_text="Выберете дату создаения аккаунта", verbose_name="Дата создаения аккаунта",
                                   null=True, blank=True)
    link_to_account = models.URLField(help_text="Введите ссылку на аккаунт", verbose_name="Ссылка на аккаунт",
                                      null=True)
    phone = models.CharField(help_text="Ведите номер телефона исполнителя", verbose_name="Телефон исполнителя",
                             max_length=35, null=True)
    gender = models.CharField(help_text="Выберете пол исполнителя", verbose_name="Пол исполнителя", null=True,
                              max_length=20)
    card_number = models.CharField(help_text="Введите номер карты", verbose_name="Номер карты", null=True, max_length=16)
    balance = models.IntegerField(help_text="Баланс", verbose_name="Баланс", null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
