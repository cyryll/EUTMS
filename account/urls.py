from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.index , name='index'),
       url(r'^passreset/',views.password , name='password'),
        url(r'^signup/',views.signup , name='signup'),
        url(r'^administration/',views.admin , name='admin'),
        url(r'^fleetassistant/',views.fleetassistant , name='fleetassistant'),
        url(r'^user/',views.user , name='user'),
        url(r'^mechanic/',views.mechanic , name='mechanic'),
]