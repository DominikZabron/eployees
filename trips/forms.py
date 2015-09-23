#-*- coding: utf-8 -*-

from django import forms
from django.forms.extras.widgets import SelectDateWidget as sdw

class AddTripForm(forms.Form):
	purpose = forms.CharField(label='Cel wyjazdu', max_length=255)
	begin_date = forms.DateField(label='Rozpoczęcie', widget=sdw)
	description = forms.CharField(label='Opis', widget=forms.Textarea)

class AddEmployeeForm(forms.Form):
	estimated_cost = forms.DecimalField(label='Szacunkowy koszt [zł]',
		decimal_places=2, min_value=0.0)