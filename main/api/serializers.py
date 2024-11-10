from rest_framework import serializers
from .models import Employee, Department
from django.db.models import Sum


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'photo', 'last_name', 'patronymic', 'position', 'salary', 'age', 'department']
    
    def create(self, validated_data):
        employee = super().create(validated_data)
        return employee
    

class DepartmentSerializer(serializers.ModelSerializer):
    employee_count = serializers.SerializerMethodField()
    total_salary = serializers.SerializerMethodField()

    class Meta:
        model = Department
        fields = ['id', 'name', 'employee_count', 'total_salary'] 

    def get_employee_count(self, obj): # число сотрудников
        return obj.employees.count()

    def get_total_salary(self, obj): # суммарный оклад 
        return obj.employees.aggregate(total=Sum('salary'))['total'] or 0
    