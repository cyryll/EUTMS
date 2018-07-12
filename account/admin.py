from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserCreationForm
from .models import Users

# Register your models here.
class UserAdmin(BaseUserAdmin):
    add_form = UserCreationForm

    list_display = ('StaffId','Role')
    list_filter = ('Role',)

    fieldsets = (
        (None,{'fields':('StaffId','Password')}),
        ('Permissions',{'fields':('Role',)})
    )
    search_fields = ('StaffId',)
    ordering = ('StaffId',)

    filter_horizontal = ()

admin.site.register(Users,UserAdmin)

admin.site.unregister(Group)
