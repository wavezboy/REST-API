from rest_framework import serializers
from Employee.models import Departments, Employees

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = '__all__'
        
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Departments
        fields = '__all__'