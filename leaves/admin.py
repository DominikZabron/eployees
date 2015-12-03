#-*- coding: utf-8 -*-

from django.contrib import admin
from django import forms

from .models import Leave, LeaveRequest

def make_approve(modeladmin, request, queryset):
	queryset.update(status='a')
make_approve.short_description = 'Zaakceptuj wybrane wnioski urlopowe'
	
def make_disapprove(modeladmin, request, queryset):
	queryset.update(status='r')
make_disapprove.short_description = 'Odrzuć wybrane wnioski urlopowe'

class LeaveAdmin(admin.ModelAdmin):
	list_display = ('last_name', 'first_name', 'available_days', 
		'days_used', 'days_left')
	list_display_links = None
	list_editable = ('available_days',)
	ordering = ('user__last_name', 'user__first_name')
	
class LeaveRequestAdmin(admin.ModelAdmin):
	exclude = ('status',)
	list_display = ('__str__', 'start_date', 'end_date', 'days', 'status')
	actions = (make_approve, make_disapprove)
		
admin.site.register(Leave, LeaveAdmin)
admin.site.register(LeaveRequest, LeaveRequestAdmin)
