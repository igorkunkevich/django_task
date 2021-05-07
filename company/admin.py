from django.contrib import admin
from company.models import Employee


@admin.action(description="Удалить данные о начисленной зарплате")
def delete_total_salary(self, request, queryset):
    queryset.update(total_salary=0)


@admin.action(description="Начислить зарплату")
def update_salary(self, request, queryset):
    for worker in queryset:
        worker.total_salary = worker.total_salary + worker.salary
        worker.save()


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("employee_name", "position", "salary", "total_salary")
    list_filter = ("position", "salary")
    actions = [delete_total_salary, update_salary]


admin.site.register(Employee, EmployeeAdmin)
