from django import forms
from .models import Vehicle, Request, SparePart, Driver, Mechanic


class VehiclesForm(forms.ModelForm):
    Number_plate = forms.CharField()
    Vehicle_type = forms.CharField()
    Engine_capacity = forms.CharField()
    Capacity = forms.IntegerField()

    class Meta:
        model = Vehicle
        fields = ('Number_plate', 'Vehicle_type', 'Engine_capacity', 'Capacity')


class RequestForm(forms.ModelForm):
    DeptRequesting = forms.CharField()
    Reason = forms.CharField()
    Travel_date = forms.DateField(widget=forms.TextInput(attrs={"class": "datepicker"}))
    Return_date = forms.DateField(widget=forms.TextInput(attrs={"class": "datepicker"}))
    Destination = forms.CharField()
    Travellers_desc = forms.CharField()
    Capacity = forms.IntegerField()

    class Meta:
        model = Request
        fields = (
        'DeptRequesting', 'Travel_date', 'Return_date', 'Destination', 'Travellers_desc', 'Reason', 'Capacity')


class SparePartForm(forms.ModelForm):
    Name = forms.CharField()
    Amount = forms.IntegerField()
    Cost = forms.IntegerField()
    Description = forms.CharField()

    class Meta:
        model = SparePart
        fields = ('Name', 'Amount', 'Cost', 'Description')


class DriverForm(forms.ModelForm):
    StaffId = forms.IntegerField()
    Email = forms.EmailField()
    Contact = forms.IntegerField()
    Name = forms.CharField()
    Department = forms.CharField()

    class Meta:
        model = Driver
        fields = ('StaffId', 'Email', 'Contact', 'Name', 'Department')


class MechanicForm(forms.ModelForm):
    StaffId = forms.IntegerField()
    Email = forms.EmailField()
    Contact = forms.IntegerField()
    Name = forms.CharField()
    Department = forms.CharField()

    class Meta:
        model = Mechanic
        fields = ('StaffId', 'Email', 'Contact', 'Name', 'Department')
