#-*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm
from datetime import datetime
from datetimewidget.widgets import DateTimeWidget, DateWidget

from .models import (BusinessTripRoute, BusinessTripAllowance,
	BusinessTripInvoiceFare, BusinessTripInvoiceAccomodation,
	BusinessTripInvoiceOther, BusinessTripInvoiceMilage,
	BusinessTripEmployee)

dateTimeOptions = {
		'format': 'yyyy-mm-dd hh:ii',
		'bootstrap_version': 3,
		'clearBtn': True,
		'weekStart': 1,
		'todayHighlight': True,
	}

dateOptions = {
		'format': 'yyyy-mm-dd',
		'bootstrap_version': 3,
		'clearBtn': True,
		'weekStart': 1,
		'todayHighlight': True,
}

class AddTripForm(forms.Form):
	purpose = forms.CharField(label='Cel wyjazdu', max_length=255)
	begin_date = forms.DateField(label='Rozpoczęcie', widget=DateWidget(
		options=dateOptions))
	description = forms.CharField(label='Opis', widget=forms.Textarea)

class AddEmployeeForm(ModelForm):
	class Meta:
		model = BusinessTripEmployee
		exclude = ('employee', 'business_trip', 'status')
		widgets = {
			'begin_date': DateWidget(options=dateOptions),
			'end_date': DateWidget(options=dateOptions),
			'description': forms.Textarea,
		}

class AddRouteForm(ModelForm):
	class Meta:
		model = BusinessTripRoute
		exclude = ('settlement',)
		widgets = {
			'begin_time': DateTimeWidget(options=dateTimeOptions),
			'end_time': DateTimeWidget(options=dateTimeOptions),
		}

class AddAllowanceForm(ModelForm):
	class Meta:
		model = BusinessTripAllowance
		exclude = ('settlement', 'is_first_day',)
		widgets = {
			'begin_time': DateTimeWidget(options=dateTimeOptions),
			'end_time': DateTimeWidget(options=dateTimeOptions),
		}


class AddFareForm(ModelForm):

	def __init__(self, pk, *args, **kwargs):
		super(AddFareForm, self).__init__(*args, **kwargs)
		self.fields['route'].queryset = BusinessTripRoute.objects.filter(
			settlement__trip_employee__business_trip=pk)

	class Meta:
		model = BusinessTripInvoiceFare
		exclude = ('settlement',)

class AddAccomodationForm(ModelForm):

	def __init__(self, pk, *args, **kwargs):
		super(AddAccomodationForm, self).__init__(*args, **kwargs)
		self.fields['overnight'].queryset = BusinessTripAllowance.objects.filter(
			settlement__trip_employee__business_trip=pk)

	class Meta:
		model = BusinessTripInvoiceAccomodation
		exclude = ('settlement',)

class AddOtherForm(ModelForm):
	class Meta:
		model = BusinessTripInvoiceOther
		exclude = ('settlement',)

class AddMilageForm(ModelForm):

	def __init__(self, pk, *args, **kwargs):
		super(AddMilageForm, self).__init__(*args, **kwargs)
		self.fields['route'].queryset = BusinessTripRoute.objects.filter(
			settlement__trip_employee__business_trip=pk)
		self.fields['name'].initial = pk

	class Meta:
		model = BusinessTripInvoiceMilage
		exclude = ('settlement',)
