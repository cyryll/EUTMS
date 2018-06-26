from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserCreationForm
from .models import Users

# Register your models here.
class UserAdmin(BaseUserAdmin):
    add_form = UserCreationForm

    list_display = ('staffId','email','is_admin','is_staff')
    list_filter = ('is_admin',)

    fieldsets = (
        (None,{'fields':('staffId','email','password')}),
        ('Permissions',{'fields':('is_admin','is_staff')})
    )
    search_fields = ('staffId','email')
    ordering = ('staffId','email')

    filter_horizontal = ()

admin.site.register(Users,UserAdmin)

admin.site.unregister(Group)
