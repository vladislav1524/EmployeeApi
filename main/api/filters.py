import django_filters
from .models import Employee


# фильтр для объектов Employee
class EmployeeFilter(django_filters.FilterSet):
    last_name = django_filters.CharFilter(field_name='last_name', lookup_expr='icontains') # Фильтрация по фамилии
    department_id = django_filters.NumberFilter(field_name='department_id') # Фильтрация по ID департамента

    class Meta:
        model = Employee
        fields = ['last_name', 'department_id']
        