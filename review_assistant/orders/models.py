from django.db import models

class Order(models.Model):
    customer_id = models.IntegerField(help_text="Выберете закзчика", verbose_name="Заказчик", )
    date_order_start = models.DateField(help_text="Дата заказа", verbose_name="Дата заказа", null=True)
    date_order_end = models.DateField(help_text="Дата заказа", verbose_name="Дата заказа", null=True)
    amount = models.IntegerField(help_text="Введите количество отзывов", verbose_name="Количество отзывов", null=True)
    gender_man = models.BooleanField(help_text="Выберете пол исполнителя", verbose_name="Мужской пол", null=True,
                                     default=False)
    gender_woman = models.BooleanField(help_text="Выберете пол исполнителя", verbose_name="Женский пол", null=True,
                                       default=False)
    link_to_account = models.URLField(help_text="Укажите ссылку на объявление", verbose_name="Ссылка на объявление")
    text = models.TextField(help_text="Введите тексты отзывов", verbose_name="Тексты отзывов", null=True)
    notes = models.TextField(help_text="Заметки заказа", verbose_name="Заметки заказа", null=True)
    prepayment = models.BooleanField(help_text="Выберете если заказ преддоплачен", verbose_name="Предоплата", null=True)
    paymant = models.BooleanField(help_text="Выберете если заказ оплачен", verbose_name="Оплата", null=True)
    hide_order = models.BooleanField(help_text="Скрыть заказ", verbose_name="Скрыть", null=True)  # hidden
    in_progers = models.BooleanField(help_text="Выполняеться", verbose_name="Выполняеться", null=True)
    divided_into_tasks = models.BooleanField(help_text="Задачи", verbose_name="Задачи", null=True)


class Image_order(models.Model):
    order = models.ForeignKey("Order", verbose_name="Заказ", null=True, blank=True, on_delete=models.PROTECT)
    img = models.ImageField(help_text="Скриншот обявления", verbose_name="Скриншот обявления", null=True,
                            upload_to="images/%Y/%m/%d")
