from rest_framework import serializers
from TransportOrderApp.models import Departments, Customers


class DepartmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Departments
        fields=('DepartmentId','DepartmentName','CustomerName','DateOfOrder')

class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customers
        fields=('CustomerId','CustomerName','Department','DateOfOrder','AddressOfPickup','AddressOfWaypoint','AddressOfDelivery')





























