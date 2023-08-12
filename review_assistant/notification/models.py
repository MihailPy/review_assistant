from django.contrib.auth.models import User
from django.db import models


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    header = models.CharField(max_length=150, help_text="Header notification", verbose_name="Заголовок уведомления", null=True)
    body = models.CharField(max_length=200, help_text="Body notification", verbose_name="Тело уведомления", null=True)
    datetime_notify = models.DateTimeField(help_text="Datetime Notification", verbose_name="Время отправки уведомления", null=True)
    task = models.ForeignKey("tasks.Tasks", verbose_name="Задача", null=True, blank=True, on_delete=models.PROTECT)
    shown = models.BooleanField(verbose_name="Показано?", null=True)