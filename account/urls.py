from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.login_view , name='login'),
       url(r'^passreset/',views.password , name='password'),
        url(r'^signup/',views.register , name='signup'),
        url(r'^administration/',views.admin , name='admin'),
        url(r'^fleetassistant/',views.fleetassistant , name='fleetassistant'),
        url(r'^user/',views.user , name='user'),
        url(r'^mechanic/',views.mechanic , name='mechanic'),
]