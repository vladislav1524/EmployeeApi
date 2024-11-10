from django.shortcuts import render
from rest_framework import viewsets
from .serializers import EmployeeSerializer, DepartmentSerializer
from .models import Employee, Department
from django_filters.rest_framework import DjangoFilterBackend
from .filters import EmployeeFilter
from django.contrib.auth.mixins import LoginRequiredMixin


class EmployeeViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = EmployeeFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        last_name = self.request.query_params.get('last_name', None)
        department_id = self.request.query_params.get('department_id', None)

        if last_name:
            queryset = queryset.filter(last_name__icontains=last_name)  # Фильтрация по фамилии
        if department_id:
            queryset = queryset.filter(department_id=department_id)  # Фильтрация по ID департамента

        return queryset
    
    

class DepartmentViewSet(viewsets.ModelViewSet):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()
    pagination_class = None
