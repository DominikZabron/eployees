#-*- coding: utf-8 -*-

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.contrib import admin
from django.forms import ModelForm, CharField

from .models import Employee, Qualifications, QualificationsEmployee


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
			'imie', 'middle_name', 'nazwisko', 'position',
			'street', 'city', 'postcode', 'country',
			'pesel', 'id_number', 'email', 'avatar',
		)


class QualificationsEmployeeInline(admin.TabularInline):
	model = QualificationsEmployee
	extra = 0


@admin.register(Employee)		
class EmployeeAdmin(admin.ModelAdmin):
	form = EmployeeListAdminForm
	list_display = ('name',)
	ordering = ('user__last_name', 'user__first_name')
	inlines = [QualificationsEmployeeInline]
	
	def name(self, obj):
		full_name = "%s %s" % (obj.user.last_name, obj.user.first_name)
		
		if full_name <> ' ':
			return full_name
		else:
			return '<< BRAK DANYCH >>'
			
	name.short_description = "Pracownicy"
	
	def has_add_permission(self, request):
		return False



admin.site.unregister(User)
admin.site.register(User, UserAdmin)

@admin.register(Qualifications)
class QualificationsAdmin(admin.ModelAdmin):
	list_display = ('name', 'ordinal')
	list_editable = ('ordinal',)
	ordering = ('ordinal',)





