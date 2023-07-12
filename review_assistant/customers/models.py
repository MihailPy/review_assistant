from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=35, help_text="Введите имя заказчика", verbose_name="Имя закзчика")
    last_name = models.CharField(max_length=35, help_text="Введите фамилию заказчика", verbose_name="Фамилия заказчика",
                                 null=True)
    phone = models.CharField(max_length=15, help_text="Ведите номер телефона закзчика",
                             verbose_name="Номер телефона заказчика", null=True)
    tg_un = models.URLField(max_length=50, help_text="Ведите username закзчика",
                            verbose_name="Username заказчика", null=True)
    notes = models.TextField(help_text="Заметки заказчика", verbose_name="Заметки заказчика", null=True)

    def __str__(self):
        return self.name
