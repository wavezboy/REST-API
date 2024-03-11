from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt  # to allow all domain to access our api method
from rest_framework.parsers import JSONParser  # to pass the icncoming data to a data module
from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from Employee.models import Departments, Employees
from Employee.serializers import DepartmentSerializer, EmployeeSerializer

# Create your views here.

@csrf_exempt
@api_view(["GET", "PUT", "DELETE", "POST"])
def deparmentApi(request, id=0):
    
    if request.method == 'GET':
        departments = Departments.objects.all()
        departments_serializer = DepartmentSerializer(departments, many=True)
        return JsonResponse(departments_serializer.data, safe=False)
  
    elif request.method == 'POST':
        departments_serializer = DepartmentSerializer(data=request.data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return Response(departments_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(departments_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
    elif request.method == 'PUT':
        department_data = JSONParser().parse(request)
        department = Departments.objects.get(DepartmentId=department_data["DepartmentId"])
        departments_serializer = DepartmentSerializer(department, data=department_data)
        if departments_serializer.is_valid():
             departments_serializer.save()
             return JsonResponse(departments_serializer.data, safe=False)
        return JsonResponse(departments_serializer.errors, safe= False)
    
    elif request.method == 'DELETE':
        department = Departments.objects.get(DepartmentId=id)
        department.delete()
        return JsonResponse('Deleted Succesfully', safe=False)
        
        
@csrf_exempt
@api_view(["GET", "PUT", "POST", "DELETE"])
def employeeApi(request, id=0):
    
    if request.method == "GET":
        employees = Employees.objects.all()
        employee_serializer = EmployeeSerializer(employees, many=True)
        return JsonResponse(employee_serializer.data, safe=False)
   
    elif request.method == "POST":
        employee_serializer = EmployeeSerializer(data=request.data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse(employee_serializer.data, safe=False)  
        return JsonResponse(employee_serializer.errors, safe=False)   
        


