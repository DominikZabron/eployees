from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import BusinessTripEmployee

class TripsListView(generic.ListView):
	model = BusinessTripEmployee
	template_name = 'trips.html'

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(TripsListView, self).dispatch(*args, **kwargs)

