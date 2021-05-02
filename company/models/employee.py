from django.db import models
from django.contrib.auth.models import User
from datetime import date


class Employee(models.Model):
    """Работники"""
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=20)
    employee_name = models.CharField("ФИО", max_length=100, unique=True)
    salary = models.PositiveIntegerField("Зарплата", default=0)
    total_salary = models.IntegerField("Всего Начислено", default=None)
    stat_date = models.DateField("Дата начала работы", default=date.today)
    position = models.CharField("Должность", max_length=50)
    level = models.SmallIntegerField("Уровень", default=1)
    api_user = models.BooleanField()

    class Meta:
        verbose_name = "Работник"
        verbose_name_plural = "Работники"

