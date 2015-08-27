#-*- coding: utf-8 -*-

from django.contrib import admin

from .models import (BusinessTrip, BusinessTripEmployee, 
	BusinessTripRoute, BusinessTripSettlement, BusinessTripAllowance,
	BusinessTripInvoiceFare, BusinessTripInvoiceAccomodation,
	BusinessTripInvoiceOther, BusinessTripInvoiceMilage)

@admin.register(BusinessTrip)
class BusinessTripAdmin(admin.ModelAdmin):
	list_display = ('purpose', 'begin_date')
	ordering = ('-begin_date',)


def make_approve(modeladmin, request, queryset):
	queryset.update(status='a')
make_approve.short_description = 'Zaakceptuj wybrane wnioski'
	
def make_disapprove(modeladmin, request, queryset):
	queryset.update(status='r')
make_disapprove.short_description = 'Odrzuć wybrane wnioski'

@admin.register(BusinessTripEmployee)
class BusinessTripEmployeeAdmin(admin.ModelAdmin):
	list_display = ('__str__', 'estimated_cost', 'status')
	exclude = ('status',)
	actions = (make_approve, make_disapprove)

@admin.register(BusinessTripRoute)
class BusinessTripRouteAdmin(admin.ModelAdmin):
	pass

def make_settlement(modeladmin, request, queryset):
	queryset.update(status='a')
make_settlement.short_description = 'Dokonano rozliczenia'
	
def make_settlement_invalid(modeladmin, request, queryset):
	queryset.update(status='r')
make_settlement_invalid.short_description = 'Odrzucono rozliczenie'

@admin.register(BusinessTripSettlement)
class BusinessTripSettlementAdmin(admin.ModelAdmin):
	list_display = ('__str__', 'status')
	exclude = ('status',)
	actions = (make_settlement, make_settlement_invalid)


@admin.register(BusinessTripAllowance)
class BusinessTripAllowanceAdmin(admin.ModelAdmin):
	fieldsets = (
		('Obliczanie diety', {
			'fields': ('settlement', 'begin_time', 'end_time', 'is_first_day',
				'is_breakfast', 'is_dinner', 'is_supper', 'is_commute_lump',
				'is_accomodation_lump')
			}
		),
		('Rachunek kosztów podróży', {
			'fields': ('commute_lump', 'accomodation_lump', 'allowance', 
				'total_allowance'
				)
			}
		)
	)
	readonly_fields = ('commute_lump','accomodation_lump', 'allowance', 
				'total_allowance')

@admin.register(BusinessTripInvoiceFare)
class BusinessTripInvoiceFareAdmin(admin.ModelAdmin):
	pass

@admin.register(BusinessTripInvoiceAccomodation)
class BusinessTripInvoiceAccomodationAdmin(admin.ModelAdmin):
	pass

@admin.register(BusinessTripInvoiceOther)
class BusinessTripInvoiceOtherAdmin(admin.ModelAdmin):
	pass

@admin.register(BusinessTripInvoiceMilage)
class BusinessTripInvoiceMilageAdmin(admin.ModelAdmin):
	fields = ('settlement', 'route', 'car', 'distance', 'value')
	readonly_fields = ('value',)