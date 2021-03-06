from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.auth_view, name='profile'),
	url(r'^login/', views.login),
	url(r'^logout/', views.logout, name='logout'),
	#url(r'^loggedin/', views.loggedin),
	url(r'^invalid/', views.invalid_login),
	url(r'^profile/', views.ProfileListView.as_view()),
]