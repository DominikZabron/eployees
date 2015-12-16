from django.contrib import admin

from .models import Car

@admin.register(Car)
class AdminCar(admin.ModelAdmin):
	list_display = ('name', 'brand', 'is_company_owned','next_tech_inspection',
		'user',	'registration_number')
