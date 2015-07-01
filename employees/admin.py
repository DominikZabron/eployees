from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.contrib import admin

from .models import Employee

"""
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm

class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = MyUser

class MyUserAdmin(UserAdmin):
    form = MyUserChangeForm

    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('some_extra_data',)}),
    )


admin.site.register(MyUser, MyUserAdmin)

class EmployeeList(admin.ModelAdmin):
	model = Employee
	can_delete = False
	#fields = ('middle_name', 'pesel', 'id_number')
	
	class Meta:
		model = Employee
		can_delete = False
 """

class EmployeeInline(admin.StackedInline):
	model = Employee
	can_delete = False	
			
class UserAdmin(UserAdmin):
	inlines = (EmployeeInline,)
	
	list_display = ('username', 'first_name', 'last_name', 'email')
	
"""
	fieldsets = (
		(None, {'fields': ('username', 'password')}),
		{'fields': 
			('first_name', 'last_name', 'email',
			'middle_name', 'pesel', 'id_number',
			'street', 'city', 'postcode', 'country')
		}), 
		{'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}), 
		{'fields': ('last_login', 'date_joined')}))
"""

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
