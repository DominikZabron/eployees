#-*- coding: utf-8 -*-

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.contrib import admin
from django.forms import ModelForm, CharField

from .models import Employee

"""
class EmployeeList(admin.ModelAdmin):
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
			'pesel', 'id_number', 'email',
			'medical_check_date', 'health_safety_date'
		)

		
class EmployeeListAdmin(admin.ModelAdmin):
	form = EmployeeListAdminForm
	list_display = ('name',)
	ordering = ('user__last_name', 'user__first_name')
	
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


