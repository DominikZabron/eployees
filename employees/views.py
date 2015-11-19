from django.views import generic
from django.shortcuts import render_to_response
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.template import RequestContext

from .models import Employee, QualificationsEmployee, Qualifications
from leaves.models import Leave
from trips.models import BusinessTripEmployee


def login(request):
    c = {}
    c.update(csrf(request))    
    return render_to_response('login.html', c)
    
def auth_view(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/accounts/profile')
    else:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect('/accounts/profile')
        else:
            return HttpResponseRedirect('/accounts/invalid')


def invalid_login(request):
    return render_to_response('invalid_login.html')

def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')

class ProfileListView(generic.ListView):
	model = QualificationsEmployee
	template_name = 'profile.html'

	def get_context_data(self, **kwargs):
		context = super(ProfileListView, self).get_context_data(**kwargs)
		context['employee'] = Employee.objects.get(user=self.request.user)
		context['leave'] = Leave.objects.get(user=self.request.user)
		context['trip'] = BusinessTripEmployee.objects.filter(
			employee=self.request.user)[0]
		context['qualifications'] = Qualifications.objects.all()
		return context

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(ProfileListView, self).dispatch(*args, **kwargs)

