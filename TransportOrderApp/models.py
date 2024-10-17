from django.db import models

# Create your models here.

class Departments(models.Model):
    DepartmentId = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=500)
    CustomerName = models.CharField(max_length=500)
    DateOfOrder = models.DateField()


class Customers(models.Model):
    CustomerId = models.AutoField(primary_key=True)
    CustomerName = models.CharField(max_length=500)
    Department = models.CharField(max_length=500)
    DateOfOrder = models.DateField()
    AddressOfPickup = models.CharField(max_length=500)
    AddressOfWaypoint = models.CharField(max_length=500)
    AddressOfDelivery = models.CharField(max_length=500)











