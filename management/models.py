from django.db import models
from account.models import Staff, Users


# Create your models here.
class Drivers(models.Model):
    Staff_id = models.OneToOneField(
        Staff, primary_key=True, on_delete=models.CASCADE)
    Availability = models.BooleanField()


class Mechanics(models.Model):
    Staff_id = models.OneToOneField(
        Staff, primary_key=True, on_delete=models.CASCADE)
    Availability = models.BooleanField()


class Vehicles(models.Model):
    #Attributes
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
    #relations
    Driver_id = models.ForeignKey(
        Drivers, related_name='vehicle', on_delete=models.CASCADE)
    Mechanic_id = models.ForeignKey(
        Mechanics, related_name='mechanic', on_delete=models.CASCADE)


class SpareParts(models.Model):
    #attributes
    SparePart_id = models.AutoField(
        primary_key=True, verbose_name='Spare part ID')
    Amount = models.IntegerField(verbose_name='Quantity')
    Name = models.CharField(max_length=100, verbose_name='Name')
    Cost = models.IntegerField(verbose_name='Cost')
    Description = models.CharField(max_length=255, verbose_name='Description')


class Requests(models.Model):
    #attributes
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
    Travellers_desc = models.CharField(max_length = 50)
    Capacity = models.IntegerField()
    Cofirm_status = models.BooleanField()
    # relations
    User_id = models.ForeignKey(Users, on_delete=models.CASCADE)


class BusAllocation(models.Model):
    #Attributes
    Request_id = models.OneToOneField(
        Requests,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    Driver_fee = models.IntegerField()
    Fuel_money = models.IntegerField()
    Estimated_distance = models.IntegerField()
    #Relations
    Driver_id = models.ForeignKey(Drivers, on_delete=models.CASCADE)
    Vehicle_id = models.ForeignKey(Vehicles, on_delete=models.CASCADE)
