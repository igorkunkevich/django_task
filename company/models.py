from django.utils.translation import gettext_lazy as _
from django.db import models
from django.contrib.auth.models import User
from datetime import date


class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    employee_name = models.CharField("Name", max_length=100, unique=True)
    salary = models.PositiveIntegerField("Salary", default=0)
    total_salary = models.PositiveIntegerField("total_salary", default=0)
    stat_date = models.DateField("1st day of working", default=date.today)

    class PositionChoice(models.TextChoices):
        TRAINEE = "TR", _("Trainee")
        WORKER = "WR", _("Worker")
        BUILDER = "BL", _("Builder")
        MANAGER = "LM", _("Manager")
        DIRECTOR = "DR", _("Director")

    position = models.CharField(
        max_length=10, choices=PositionChoice.choices, default=PositionChoice.TRAINEE
    )

    class Meta:
        verbose_name = "WORKER"
        verbose_name_plural = "WORKERS"
