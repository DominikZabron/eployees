#-*- coding: utf-8 -*-

from django import forms
from django.forms.extras.widgets import SelectDateWidget as sdw

ACCEPTED_FORMATS = ['%d-%m-%Y', '%d.%m.%Y', '%d/%m/%Y']

class LeaveRequestForm(forms.Form):
	start_date = forms.DateField(label='początek urlopu', widget=sdw)
	end_date = forms.DateField(label='koniec urlopu', widget=sdw)
	days = forms.IntegerField(label='ilość dni', min_value=1)