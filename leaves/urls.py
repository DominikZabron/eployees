from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^leaves/', views.LeavesListView.as_view()),
]