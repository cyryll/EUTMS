from django.contrib import admin
from .models import Vehicle,Request,SparePart
from .forms import VehiclesForm,RequestForm,SparePartForm
# Register your models here.

class VehicleAdmin(admin.ModelAdmin):
    add_form = VehiclesForm

    list_display = ('Number_plate','Vehicle_type','Engine_capacity','Capacity')
    list_filter = ('Vehicle_type',)

    filter_horizontal = ()

admin.site.register(Vehicle,VehicleAdmin)

class RequestAdmin(admin.ModelAdmin):
    add_form = RequestForm

    list_display = ('DeptRequesting','Reason','Travel_date','Destination','Travellers_desc','Capacity')
    list_filter = ('DeptRequesting',)

    filter_horizontal = ()

admin.site.register(Request,RequestAdmin)

class SparepartAdmin(admin.ModelAdmin):
    add_form = SparePartForm

    list_display = ('Name','Amount','Cost','Description')
    list_filter = ('Name',)

    filter_horizontal = ()
admin.site.register(SparePart,SparepartAdmin)