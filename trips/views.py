from django.shortcuts import render
from django.views import generic
from django.views.generic import edit
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.core.urlresolvers import reverse, reverse_lazy
from datetime import datetime, timedelta

from .models import (BusinessTrip, BusinessTripEmployee, BusinessTripSettlement,
	BusinessTripRoute, BusinessTripAllowance, BusinessTripInvoice, 
	BusinessTripInvoiceFare, BusinessTripInvoiceAccomodation,
	BusinessTripInvoiceOther, BusinessTripInvoiceMilage)
from employees.models import Employee
from .forms import (AddTripForm, AddEmployeeForm, AddRouteForm,
	AddAllowanceForm, AddFareForm, AddAccomodationForm, AddOtherForm,
	AddMilageForm)

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

class AddEmployeeFormView(edit.FormView):
	form_class = AddEmployeeForm
	template_name = 'add_employee.html'
	#success_url = '/trips/trip/'

	def get_success_url(self):
		return reverse('trip', kwargs={'pk': self.kwargs.get('pk', '')})

	def get_context_data(self, **kwargs):
		context = super(AddEmployeeFormView, self).get_context_data(**kwargs)
		context['pk'] = self.kwargs.get('pk', '')
		return context

	def form_valid(self, form):
		employee = form.save(commit=False)
		employee.employee = User.objects.get(username=self.request.user)
		employee.business_trip = BusinessTrip.objects.get(
			id=self.kwargs.get('pk', ''))
		employee.save()
		return super(AddEmployeeFormView, self).form_valid(form)

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(AddEmployeeFormView, self).dispatch(*args, **kwargs)

class SettlementListView(generic.TemplateView):
	template_name = 'settlement.html'

	def get_context_data(self, **kwargs):
		context = super(SettlementListView, self).get_context_data(**kwargs)
		settlement = BusinessTripSettlement.objects.get(
			trip_employee__employee=self.request.user,
			trip_employee__business_trip=self.kwargs.get('pk', ''))
		context['settlement'] = settlement
		context['route_list'] = BusinessTripRoute.objects.filter(
			settlement=settlement)
		context['allowance_list'] = BusinessTripAllowance.objects.filter(
			settlement=settlement)
		context['invoice_list'] = BusinessTripInvoice.objects.filter(
			settlement=settlement)
		return context

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(SettlementListView, self).dispatch(*args, **kwargs)

class AddRouteFormView(edit.FormView):
	form_class = AddRouteForm
	template_name = 'add_route.html'

	def get_context_data(self, **kwargs):
		context = super(AddRouteFormView, self).get_context_data(**kwargs)
		context['pk'] = self.kwargs.get('pk', '')
		return context

	def get_success_url(self):
		return reverse('settlement', kwargs={'pk': self.kwargs.get('pk', '')})

	def form_valid(self, form):
		settlement = BusinessTripSettlement.objects.get(
			trip_employee__employee=self.request.user,
			trip_employee__business_trip=self.kwargs.get('pk', '')
		)
		if settlement.status == 'i':
			route = BusinessTripRoute(settlement=settlement,
				begin=form.cleaned_data['begin'],
				begin_time=form.cleaned_data['begin_time'],
				end=form.cleaned_data['end'],
				end_time=form.cleaned_data['end_time'],
				transportation=form.cleaned_data['transportation']
			)
			route.save()
		return super(AddRouteFormView, self).form_valid(form)

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(AddRouteFormView, self).dispatch(*args, **kwargs)

class DeleteRouteView(edit.DeleteView):
	model = BusinessTripRoute

	def delete(self, request, *args, **kwargs):
		settlement = BusinessTripSettlement.objects.get(
			trip_employee__employee=self.request.user,
			trip_employee__business_trip=self.kwargs.get('rev', '')
		)
		self.object = self.get_object()

		if settlement.status == 'i':
			self.object.delete()

		return HttpResponseRedirect(self.get_success_url())


	def get_success_url(self):
		return reverse_lazy('settlement', kwargs={
			'pk': self.kwargs.get('rev', '')
		})

class AddAllowanceFormView(edit.FormView):
	form_class = AddAllowanceForm
	template_name = 'add_allowance.html'

	def get_context_data(self, **kwargs):
		context = super(AddAllowanceFormView, self).get_context_data(**kwargs)
		context['pk'] = self.kwargs.get('pk', '')
		return context

	def get_success_url(self):
		return reverse('settlement', kwargs={'pk': self.kwargs.get('pk', '')})

	def form_valid(self, form):
		settlement = BusinessTripSettlement.objects.get(
			trip_employee__employee=self.request.user,
			trip_employee__business_trip=self.kwargs.get('pk', '')
		)

		if settlement.status == 'i':

			s_time = form.cleaned_data['begin_time']
			e_time = s_time + timedelta(hours=24)
			end_time = form.cleaned_data['end_time']
			is_first_day = True

			while e_time < end_time:
				r = BusinessTripAllowance.objects.create(
					settlement=settlement,
					begin_time=s_time,
					end_time=e_time,
					is_first_day=is_first_day,
					is_breakfast=form.cleaned_data['is_breakfast'],
					is_dinner=form.cleaned_data['is_dinner'],
					is_supper=form.cleaned_data['is_supper'],
					is_commute_lump=form.cleaned_data['is_commute_lump'],
					is_accomodation_lump=form.cleaned_data['is_accomodation_lump'],
				)

				is_first_day = False
				s_time = e_time 
				e_time = e_time + timedelta(hours=24)

			data = form.save(commit=False)
			data.settlement = settlement
			data.begin_time = s_time
			data.end_time = end_time
			data.is_first_day = is_first_day
			data.save()

		return super(AddAllowanceFormView, self).form_valid(form)

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(AddAllowanceFormView, self).dispatch(*args, **kwargs)

class DeleteAllowanceView(edit.DeleteView):
	model = BusinessTripAllowance

	def delete(self, request, *args, **kwargs):
		settlement = BusinessTripSettlement.objects.get(
			trip_employee__employee=self.request.user,
			trip_employee__business_trip=self.kwargs.get('rev', '')
		)
		self.object = self.get_object()

		if settlement.status == 'i':
			self.object.delete()

		return HttpResponseRedirect(self.get_success_url())

	def get_success_url(self):
		return reverse_lazy('settlement', kwargs={
			'pk': self.kwargs.get('rev', '')
		})

class UpdateAllowanceView(edit.UpdateView):
	model = BusinessTripAllowance
	fields = ['begin_time', 'end_time', 'is_first_day', 'is_breakfast', 
		'is_dinner', 'is_supper', 'is_commute_lump', 'is_accomodation_lump',]
	template_name = 'add_allowance.html'

	def form_valid(self, form):

		settlement = BusinessTripSettlement.objects.get(
			trip_employee__employee=self.request.user,
			trip_employee__business_trip=self.kwargs.get('rev', ''),
		)

		if settlement.status == 'i':
			self.object = form.save()

		#return super(UpdateAllowanceView, self).form_valid(form)
		return HttpResponseRedirect(self.get_success_url())

	def get_success_url(self):
		return reverse_lazy('settlement', kwargs={
			'pk': self.kwargs.get('rev', '')
		})

class AddCostFormView(edit.FormView):
	template_name = 'add_cost.html'

	def get_form_class(self):
		if self.kwargs.get('type', '') == '0':
			return AddOtherForm
		elif self.kwargs.get('type', '') == '1':
			return AddMilageForm
		elif self.kwargs.get('type', '') == '2':
			return AddAccomodationForm
		elif self.kwargs.get('type', '') == '3':
			return AddFareForm

	def get_context_data(self, **kwargs):
		context = super(AddCostFormView, self).get_context_data(**kwargs)
		context['pk'] = self.kwargs.get('pk', '')
		context['type'] = self.kwargs.get('type', '')
		return context

	def get_success_url(self):
		return reverse('settlement', kwargs={'pk': self.kwargs.get('pk', '')})

	def form_valid(self, form):
		data = form.save(commit=False)
		data.settlement = BusinessTripSettlement.objects.get(
			trip_employee__employee=self.request.user,
			trip_employee__business_trip=self.kwargs.get('pk', '')
		)
		if data.settlement.status == 'i':
			data.save()
		return super(AddCostFormView, self).form_valid(form)

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(AddCostFormView, self).dispatch(*args, **kwargs)

class DeleteCostView(edit.DeleteView):
	model = BusinessTripInvoice

	def delete(self, request, *args, **kwargs):
		settlement = BusinessTripSettlement.objects.get(
			trip_employee__employee=self.request.user,
			trip_employee__business_trip=self.kwargs.get('rev', '')
		)
		self.object = self.get_object()

		if settlement.status == 'i':
			self.object.delete()

		return HttpResponseRedirect(self.get_success_url())
		
	def get_success_url(self):
		return reverse_lazy('settlement', kwargs={
			'pk': self.kwargs.get('rev', '')
		})

class SendView(generic.RedirectView):
	permanent = False

	def get_redirect_url(self, *args, **kwargs):
		return reverse_lazy('settlement', kwargs={
			'pk': self.kwargs.get('pk', '')
		})

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		settlement = BusinessTripSettlement.objects.get(
			trip_employee__employee=self.request.user,
			trip_employee__business_trip=self.kwargs.get('pk', '')
		)
		if settlement.status == 'i':
			settlement.status = 'w'
			settlement.save()
		return super(SendView, self).dispatch(*args, **kwargs) 



