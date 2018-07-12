from django import forms
from .models import Vehicles,Requests

class VehiclesForm(forms.ModelForm):
    Number_plate =forms.CharField()
    Vehicle_type = forms.CharField()
    Engine_capacity = forms.CharField()
    Capacity = forms.IntegerField()
    #Availability = forms.BooleanField()
    class Meta:
        model = Vehicles
        fields = ('Number_plate', 'Vehicle_type','Engine_capacity','Capacity')

class RequestForm(forms.ModelForm):
    DeptRequesting = forms.CharField()
    Reason = forms.CharField()
    Travel_date = forms.DateField(widget = forms.TextInput(attrs={"class":"datepicker"}))
    Return_date = forms.DateField(widget = forms.TextInput(attrs={"class":"datepicker"}))
    Destination = forms.CharField()
    Travellers_desc = forms.CharField()
    Capacity = forms.IntegerField()

    class Meta:
        model = Requests
        fields = ('DeptRequesting','Travel_date','Return_date','Destination','Travellers_desc','Reason', 'Capacity')

class SparePartForm(forms.ModelForm):
    Amount = forms.IntegerField()
    Name = forms.CharField()
    Cost = forms.IntegerField()
    Description = forms.CharField()