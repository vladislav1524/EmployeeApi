from django.contrib import admin
from .models import Department, Employee 


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'patronymic', 'position', 'salary', 'age', 'department')
    search_fields = ('name', 'last_name', 'patronymic', 'position', 'department__name')
    list_filter = ('department', 'salary')
    ordering = ('last_name',)
 