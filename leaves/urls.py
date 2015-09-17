from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^leaves/', views.LeavesListView.as_view()),
	url(r'^leaverequest/', views.leave_request),
	url(r'^leavereq_success/', views.leavereq_success),
]