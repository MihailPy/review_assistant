from django.db import models


class Tasks(models.Model):
    order = models.ForeignKey("orders.Order", verbose_name="Заказ", on_delete=models.PROTECT)
    executor = models.ForeignKey("executors.Executor", on_delete=models.PROTECT, verbose_name="Исполнитель",
                                 blank=False)
    image = models.ForeignKey("orders.Image_order", verbose_name="Скриншот", null=True, on_delete=models.PROTECT)
    text_review = models.CharField(max_length=500, verbose_name="Текст отзыва", null=True)
    correspondence_date = models.DateTimeField(verbose_name="Дата переписки", null=True)
    date_of_the_completed_correspondence = models.DateTimeField(verbose_name="Дата окончания переписки", null=True)
    date_of_withdrawal = models.DateTimeField(verbose_name="Дата отзыва", null=True)
    date_of_writing_the_review = models.DateTimeField(verbose_name="Дата выполнения отзыва", null=True)
    in_progres = models.BooleanField(verbose_name="В работе", help_text="если в работе", null=True)
    execution_or_no = models.BooleanField(help_text="Выберете если исполнено", verbose_name="Исполнено", null=True)
    paymant = models.BooleanField(help_text="Выберете если оплачено", verbose_name="Оплата", null=True)
    hitch = models.BooleanField(help_text="Выберете если произошла заминка", verbose_name="Заминка", null=True)


class Accounting_for_completed_and_failed_tasks(models.Model):
    order = models.ForeignKey("orders.Order", verbose_name="Заказ", on_delete=models.PROTECT)
    executor = models.ForeignKey("executors.Executor", on_delete=models.PROTECT, verbose_name="Исполнитель",
                                 blank=False, default="")
    correspondence_date = models.DateTimeField(verbose_name="Дата переписки", null=True)
    date_of_the_completed_correspondence = models.DateTimeField(verbose_name="Дата окончания переписки", null=True)
    date_of_withdrawal = models.DateTimeField(verbose_name="Дата отзыва", null=True)
    date_of_writing_the_review = models.DateTimeField(verbose_name="Дата выполнения отзыва", null=True)
    execution_or_no = models.BooleanField(help_text="Выберете если исполнено", verbose_name="Исполнено", default=False)
    paymant = models.BooleanField(help_text="Выберете если оплачено", verbose_name="Оплата", null=True)
