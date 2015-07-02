from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.contrib import admin
from django.forms import ModelForm, CharField

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
	
	fieldsets = (
		(None, {'fields': ('username', 'password')}),
		{'fields': 
			('first_name', 'last_name', 'email',
			'middle_name', 'pesel', 'id_number',
			'street', 'city', 'postcode', 'country')
		}), 
		{'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}), 
		{'fields': ('last_login', 'date_joined')}))

# This works, source: docs.djangoproject.com

class EmployeeInline(admin.StackedInline):
	model = Employee
	can_delete = False	
			
class UserAdmin(UserAdmin):
	inlines = (EmployeeInline,)
	
	list_display = ('username', 'last_name', 'first_name', 'email')
	
# working code ends here
"""

class EmployeeListAdminForm(ModelForm):	
	imie = CharField(max_length=200)
	nazwisko = CharField(max_length=200)
	email = CharField(max_length=200)
	
	def __init__(self, *args, **kwds):
		super(EmployeeListAdminForm, self).__init__(*args, **kwds)
		self.fields['imie'].initial = self.instance.user.first_name
		self.fields['nazwisko'].initial = self.instance.user.last_name
		self.fields['email'].initial = self.instance.user.email	
		#self.fields['user'].queryset = User.objects.order_by('last_name')
		
	class Meta:
		model = Employee
		fields = (
			'imie', 'middle_name', 'nazwisko',
			'street', 'city', 'postcode', 'country',
			'pesel', 'id_number', 'email'
		)

		
class EmployeeListAdmin(admin.ModelAdmin):
	form = EmployeeListAdminForm
	list_display = ('name',)
	
	def name(self, obj):
		full_name = "%s %s" % (obj.user.last_name, obj.user.first_name)
		
		if full_name <> ' ':
			return full_name
		else:
			return '<< ERROR::Uzytkownicy::Dane osobowe:: >>BRAK DANYCH<< >>'
			
	name.short_description = "Pracownicy"
	
	def has_add_permission(self, request):
		return False

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Employee, EmployeeListAdmin)


