from django.shortcuts import render_to_response
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

from .models import Employee
from leaves.models import Leave
from trips.models import BusinessTripEmployee


def login(request):
    c = {}
    c.update(csrf(request))    
    return render_to_response('login.html', c)
    
def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/accounts/profile')
    else:
        return HttpResponseRedirect('/accounts/invalid')

"""
@login_required   
def loggedin(request):
    return render_to_response('loggedin.html', 
    	{'full_name': request.user.first_name + ' ' + request.user.last_name}
    )
"""

def invalid_login(request):
    return render_to_response('invalid_login.html')

def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')

@login_required
def profile(request):
	e = Employee.objects.get()
	l = Leave.objects.get()
	t = BusinessTripEmployee.objects.get()
	return render_to_response('profile.html',
		{ 'position': e.position,
			'street': e.street,
			'postcode': e.postcode,
			'city': e.city,
			'medical_check_date': e.medical_check_date,
			'health_safety_date': e.health_safety_date,
			'avatar': e.avatar,
			'available_days': l.available_days,
			'days_left': l.days_left,
			'days_used': l.days_used,
			'trip_count': t.trip_count,
			'settlement_count': t.settlement_count,
		},
		context_instance=RequestContext(request)
	)
