#-*- coding: utf-8 -*-

from django import forms
from datetimewidget.widgets import DateWidget

dateOptions = {
		'format': 'yyyy-mm-dd',
		'bootstrap_version': 3,
		'clearBtn': True,
		'weekStart': 1,
		'todayHighlight': True,
}

class LeaveRequestForm(forms.Form):
	start_date = forms.DateField(label='początek urlopu', widget=DateWidget(
		options=dateOptions))
	end_date = forms.DateField(label='koniec urlopu', widget=DateWidget(
		options=dateOptions))
	days = forms.IntegerField(label='ilość dni', min_value=1)

