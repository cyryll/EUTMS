from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.login_view , name='login'),
     url(r'^logout/$',views.logout_view , name='logout'),
       url(r'^passreset/',views.password , name='password'),
        url(r'^signup/$',views.register , name='signup'),
        url(r'^administration/',views.admin , name='admin'),
        url(r'^fleetassistant/',views.fleetassistant , name='fleetassistant'),
        url(r'^user/',views.user , name='user'),
        url(r'^mechanic/',views.mechanic , name='mechanic'),
        url(r'^request/$',views.requests , name='requests'),
        url(r'status/$',views.booking_status , name='booking_status'),
        url(r'driver/$',views.add_driver , name='driver'),
        url(r'driverDetails/$',views.remove_driver , name='driverDetails'),
         url(r'vehicle/$',views.add_vehicle , name='vehicle'),
        url(r'vehicleDetails/$',views.remove_vehicle , name='vehicleDetails'),
        url(r'userDetails/$',views.user_details , name='userDetails'),
        url(r'mechanics/$',views.mechanics , name='mechanics'),
        url(r'spareparts/$',views.add_sparepart , name='spareparts'),
]
