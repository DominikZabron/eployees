from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import LeaveRequest

class LeavesListView(generic.ListView):
	model = LeaveRequest
	template_name = 'leaves.html'
"""
	@method_decorator
	def dispatch(self, *args, **kwargs):
		return super(LeavesListView, self).dispatch(*args, **kwargs)
"""
