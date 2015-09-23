from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect

from .models import LeaveRequest, Leave
from .forms import LeaveRequestForm

class LeavesListView(generic.ListView):
	model = LeaveRequest
	template_name = 'leaves.html'
	queryset = LeaveRequest.objects.order_by('-end_date')

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(LeavesListView, self).dispatch(*args, **kwargs)

@login_required
def leave_request(request):

	if request.method == 'POST':
		form = LeaveRequestForm(request.POST)

		if form.is_valid():
			cd = form.cleaned_data
			req = LeaveRequest(
				leave=Leave.objects.get(user=request.user),
				start_date=cd['start_date'],
				end_date=cd['end_date'],
				days=cd['days'],
			)
			req.save()
			return HttpResponseRedirect('/leaves/leavereq_success/')

	else:
		form = LeaveRequestForm()

	return render(request, 'leaverequest.html', {'form': form})

def leavereq_success(request):
	return render(request, 'leavereq_success.html', {})

