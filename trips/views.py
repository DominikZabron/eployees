from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

from .models import BusinessTrip, BusinessTripEmployee
from employees.models import Employee
from .forms import AddTripForm, AddEmployeeForm

class TripsListView(generic.ListView):
	model = BusinessTrip
	template_name = 'trips.html'

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(TripsListView, self).dispatch(*args, **kwargs)

class TripsDetailView(generic.DetailView):
	model = BusinessTrip
	template_name = 'trips_detail.html'

	def get_context_data(self, **kwargs):
		context = super(TripsDetailView, self).get_context_data(**kwargs)

		context['trip_employees'] = BusinessTripEmployee.objects.filter(
			business_trip=self.kwargs.get('pk', ''))
	
		return context

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(TripsDetailView, self).dispatch(*args, **kwargs)

def add_trip(request):

	if request.method == 'POST':
		form = AddTripForm(request.POST)

		if form.is_valid():
			cd = form.cleaned_data
			trip = BusinessTrip(
				purpose = cd['purpose'],
				begin_date = cd['begin_date'],
				description = cd['description'],
			)
			trip.save()
			return HttpResponseRedirect('/trips/trip/')

	else:
		form = AddTripForm()

	return render(request, 'add_trip.html', {'form': form})

def add_employee(request, pk):

	if request.method == 'POST':
		form = AddEmployeeForm(request.POST)

		if form.is_valid():
			cd = form.cleaned_data
			employee = BusinessTripEmployee(
				employee = User.objects.get(username=request.user),
				business_trip = BusinessTrip.objects.get(id=pk),
				estimated_cost = cd['estimated_cost'],
			)

			try:
				employee.save()
			except:
				pass

			return HttpResponseRedirect('/trips/trip/')

	else:
		form = AddEmployeeForm()

	return render(request, 'add_employee.html', {'form': form, 'pk':pk })

