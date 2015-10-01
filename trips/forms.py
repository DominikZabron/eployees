#-*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm
from datetime import datetime
from django.forms.extras.widgets import SelectDateWidget as sdw

from .models import (BusinessTripRoute, BusinessTripAllowance,
	BusinessTripInvoiceFare, BusinessTripInvoiceAccomodation,
	BusinessTripInvoiceOther, BusinessTripInvoiceMilage)

class AddTripForm(forms.Form):
	purpose = forms.CharField(label='Cel wyjazdu', max_length=255)
	begin_date = forms.DateField(label='Rozpoczęcie', widget=sdw)
	description = forms.CharField(label='Opis', widget=forms.Textarea)

class AddEmployeeForm(forms.Form):
	begin_date = forms.DateField(label='Rozpoczęcie', widget=sdw)
	end_date = forms.DateField(label='Zakończenie', widget=sdw)
	estimated_cost = forms.DecimalField(label='Szacunkowy koszt [zł]',
		decimal_places=2, min_value=0.0)
	description = forms.CharField(label="Uzasadnienie", widget=forms.Textarea,
		required=False)

class AddRouteForm(ModelForm):
	class Meta:
		model = BusinessTripRoute
		exclude = ('settlement',)

class AddAllowanceForm(ModelForm):
	class Meta:
		model = BusinessTripAllowance
		exclude = ('settlement',)

class AddFareForm(ModelForm):
	class Meta:
		model = BusinessTripInvoiceFare
		exclude = ('settlement',)

class AddAccomodationForm(ModelForm):
	class Meta:
		model = BusinessTripInvoiceAccomodation
		exclude = ('settlement',)

class AddOtherForm(ModelForm):
	class Meta:
		model = BusinessTripInvoiceOther
		exclude = ('settlement',)

class AddMilageForm(ModelForm):
	class Meta:
		model = BusinessTripInvoiceMilage
		exclude = ('settlement',)
