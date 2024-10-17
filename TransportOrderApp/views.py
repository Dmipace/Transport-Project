from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from TransportOrderApp.models import Departments,Customers
from TransportOrderApp.serializers import DepartmentsSerializer,CustomersSerializer

# Create your views here.

@csrf_exempt
def departmentApi(request, id=0):
    if request.method=='GET':
        departments = Departments.objects.all()
        departments_serializer=DepartmentsSerializer(departments,many=True)
        return JsonResponse(departments_serializer.data,safe=False)
    elif request.method=='POST':
        department_data=JSONParser().parse(request)
        departments_serializer=DepartmentsSerializer(data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Successfully added",safe=False)
        return JsonResponse("Failed to add, something is wrong",safe=False)
    elif request.method=='PUT':
        department_data=JSONParser().parse(request)
        department=Departments.objects.get(DepartmentId=department_data['DepartmentId'])
        departments_serializer=DepartmentsSerializer(department,data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Successfully update",safe=False)
        return JsonResponse("Failed to update, something is wrong")
    elif request.method=='DELETE':
        department=Departments.objects.get(DepartmentId=id)
        department.delete()
        return JsonResponse("Successfully deleted",safe=False)

@csrf_exempt
def customerApi(request, id=0):
    if request.method=='GET':
        customers = Customers.objects.all()
        customers_serializer=CustomersSerializer(customers,many=True)
        return JsonResponse(customers_serializer.data,safe=False)
    elif request.method=='POST':
        customer_data=JSONParser().parse(request)
        customers_serializer=CustomersSerializer(data=customer_data)
        if customers_serializer.is_valid():
            customers_serializer.save()
            return JsonResponse("Successfully added",safe=False)
        return JsonResponse("Failed to add, something is wrong",safe=False)
    elif request.method=='PUT':
        customer_data=JSONParser().parse(request)
        customer=Customers.objects.get(CustomerId=customer_data['CustomerId'])
        customers_serializer=CustomersSerializer(customer,data=customer_data)
        if customers_serializer.is_valid():
            customers_serializer.save()
            return JsonResponse("Successfully update",safe=False)
        return JsonResponse("Failed to update, something is wrong")
    elif request.method=='DELETE':
        customer=Customers.objects.get(CustomerId=id)
        customer.delete()
        return JsonResponse("Successfully deleted",safe=False)

















