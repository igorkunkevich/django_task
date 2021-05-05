from rest_framework import serializers
from .models import Employee


class EmployeeListSerializer(serializers.ModelSerializer):
    """Список Работников"""

    class Meta:
        model = Employee
        fields = (
            "employee_name",
            "salary",
            "total_salary",
            "stat_date",
            "position",
        )

