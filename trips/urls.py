from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^trip/', views.TripsListView.as_view()),
]