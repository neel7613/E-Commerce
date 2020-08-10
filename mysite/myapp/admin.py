from django.contrib import admin
from .models import Category,Device,ExtendedUser,Cart
# Register your models here.
from .forms import NewUserForm,MyUserChangeForm
from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.forms import UserCreationForm,UserChangeForm


admin.site.register(Category)
admin.site.register(Device)
admin.site.register(Cart)

class MyUserAdmin(UserAdmin):


    form = MyUserChangeForm
    add_form = NewUserForm


    ordering = ('email',)
    list_display = ('email','is_superuser','full_name')
    list_filter = ('email',)
    search_fields = ('email',)
    fieldsets = (
        (None,{
            'fields' : (
                        'email',
                        'password',
                        'full_name',
                        'address',
                        )
                }),

        )
    add_fieldsets = (
        (None,{
            'fields' : (
                        'email',
                        'password1',
                        'password2',
                        'full_name',
                        'address',
                        )
                }),

        )
admin.site.register(ExtendedUser,MyUserAdmin)
