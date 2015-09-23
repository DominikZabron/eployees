from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^trip/', views.TripsListView.as_view()),
	url(r'^(?P<pk>[0-9]+)/', views.TripsDetailView.as_view()),
	url(r'^add_trip/', views.add_trip),
	url(r'^add_employee/(?P<pk>[0-9]+)/', views.add_employee),
]