from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.login),
	url(r'^login/', views.login),
	url(r'^auth/', views.auth_view),
	url(r'^logout/', views.logout),
	#url(r'^loggedin/', views.loggedin),
	url(r'^invalid/', views.invalid_login),
	url(r'^profile/', views.profile),
]