from django.db import models
from account.models import Users


# Create your models here.
class StaffProfile(models.Model):
    Email = models.EmailField(primary_key = True, max_length=100)
    Contact = models.CharField(max_length=13)
    Name = models.CharField(max_length=70)
    Department = models.CharField(max_length=50)
    Availability = models.BooleanField(default=True)
    Date = models.DateField(auto_now=False)


class Driver(models.Model):
    StaffId = models.IntegerField(primary_key=True, unique=True)

    def __str__(self):
        return self.StaffId


class Mechanic(models.Model):
    StaffId = models.IntegerField(primary_key=True, unique=True)

    def __str__(self):
        return self.StaffId


class Vehicle(models.Model):
    # Attributes
    Number_plate = models.CharField(
        max_length=7,
        primary_key=True,
        unique=True,
        verbose_name='Lisence Plate')
    Vehicle_type = models.CharField(max_length=15, verbose_name='Vehicle type')
    Engine_capacity = models.CharField(
        max_length=10, verbose_name='Engine Capacity')
    Capacity = models.IntegerField(verbose_name='Vehicle Capacity')
    Availability = models.BooleanField(default=True)
    # relations
    Driver = models.ForeignKey(
        Driver, related_name='vehicle', on_delete=models.CASCADE)
    Mechanic = models.ForeignKey(
        Mechanic, related_name='mechanic', on_delete=models.CASCADE)

    def __str__(self):
        return self.Number_plate


class SparePart(models.Model):
    # attributes
    SparePart_id = models.AutoField(
        primary_key=True, verbose_name='Spare part ID')
    Amount = models.IntegerField(verbose_name='Quantity')
    Name = models.CharField(max_length=100, verbose_name='Name')
    Cost = models.IntegerField(verbose_name='Cost')
    Description = models.CharField(max_length=255, verbose_name='Description')

    def __str__(self):
        return self.SparePart_id


class Request(models.Model):
    # attributes
    Request_id = models.AutoField(
        verbose_name='request ID',
        primary_key=True,
        unique=True,
    )
    DeptRequesting = models.CharField(max_length=100)
    Reason = models.CharField(max_length=100)
    Travel_date = models.DateField(auto_now=False)
    Return_date = models.DateField(auto_now=False)
    Destination = models.CharField(max_length=40)
    Travellers_desc = models.CharField(max_length=50)
    Capacity = models.IntegerField()
    Cofirm_status = models.BooleanField()
    # relations
    User = models.ForeignKey(Users, on_delete=models.CASCADE)


class BusAllocation(models.Model):
    # Attributes
    Request = models.OneToOneField(
        Request,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    Driver_fee = models.IntegerField()
    Fuel_money = models.IntegerField()
    Estimated_distance = models.IntegerField()
    # Relations
    Driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    Vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    # Travel_date = models.ForeignKey(Requests, on_delete=models.CASCADE)
