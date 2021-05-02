from django.contrib import admin
from company.models.employee import Employee


@admin.action(description="Удалить данные о начисленной зарплате")
def delete_total_salary(self, request, queryset):
    queryset.update(total_salary=0)


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("employee_name", "position", "salary", "total_salary", "api_user")
    list_filter = ("position", "level")
    actions = [delete_total_salary]


admin.site.register(Employee, EmployeeAdmin)

