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
    telegram_id = models.URLField(help_text="Ведите телеграм id исполнителя", verbose_name="Телеграм id исполнителя",
                                  max_length=35, null=True)
    gender = models.CharField(help_text="Выберете пол исполнителя", verbose_name="Пол исполнителя", null=True,
                              max_length=20)
