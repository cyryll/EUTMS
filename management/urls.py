from django.conf.urls import url
from . import views

urlpatterns=[
        url(r'^administration/',views.admin , name='admin'),
        url(r'^fleetassistant/',views.fleetassistant , name='fleetassistant'),
        url(r'^user/',views.user , name='user'),
        url(r'^mechanic/',views.mechanic , name='mechanic'),
        url(r'^mechanic/',views.mechanic2 , name='mechanic2'),
        url(r'^request/$',views.requests , name='requests'),
        url(r'status/$',views.booking_status , name='booking_status'),
        url(r'fleetview/$',views.fleetview , name='fleetview'),
        url(r'driverDetails/',views.remove_driver , name='driverDetails'),
        url(r'vehicle/$',views.add_vehicle , name='vehicle'),
        url(r'vehicleDetails/$',views.remove_vehicle , name='vehicleDetails'),
        url(r'mechanics/$',views.mechanics , name='mechanics'),
        url(r'spareparts/$',views.add_sparepart , name='spareparts'),
        url(r'^administration/',views.admin2 , name='admin2'),
        
]