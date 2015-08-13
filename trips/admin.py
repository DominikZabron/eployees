#-*- coding: utf-8 -*-

from django.contrib import admin

from .models import BusinessTrip, BusinessTripItem, BusinessTripSettlement

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

@admin.register(BusinessTripItem)
class BusinessTripItemAdmin(admin.ModelAdmin):
	list_display = ('__str__', 'business_trip', 'estimated_cost', 'status')
	exclude = ('status',)
	actions = (make_approve, make_disapprove)

@admin.register(BusinessTripSettlement)
class BusinessTripSettlementAdmin(admin.ModelAdmin):
	list_display = ('__str__', 'costs_all', 'status')
	exclude = ('status',)
	actions = (make_approve, make_disapprove)

