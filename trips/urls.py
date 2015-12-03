from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^trip/', views.TripsListView.as_view(paginate_by=10)),
	url(r'^(?P<pk>[0-9]+)/', views.TripsDetailView.as_view(), name='trip'),
	url(r'^add_trip/', views.add_trip),
	url(r'^add_employee/(?P<pk>[0-9]+)/', views.AddEmployeeFormView.as_view()),
	url(r'^settlement/(?P<pk>[0-9]+)/', views.SettlementListView.as_view(),
		name='settlement'),
	url(r'^add_route/(?P<pk>[0-9]+)/', views.AddRouteFormView.as_view()),
	url(r'^delete_route/(?P<rev>[0-9]+)/(?P<pk>[0-9]+)/',
		views.DeleteRouteView.as_view()),
	url(r'^add_allowance/(?P<pk>[0-9]+)/',
		views.AddAllowanceFormView.as_view()),
	url(r'^delete_allowance/(?P<rev>[0-9]+)/(?P<pk>[0-9]+)/',
		views.DeleteAllowanceView.as_view()),
	url(r'^update_allowance/(?P<rev>[0-9]+)/(?P<pk>[0-9]+)/',
		views.UpdateAllowanceView.as_view()),
	#url(r'^add_fare/(?P<pk>[0-9]+)/', views.AddFareFormView.as_view()),
	url(r'^add_cost/(?P<pk>[0-9]+)/(?P<type>[0-3]{1})/',
		views.AddCostFormView.as_view()),
	#url(r'^add_milage/(?P<pk>[0-9]+)/', views.AddMilageFormView.as_view()),
	#url(r'^add_other/(?P<pk>[0-9]+)/', views.AddOtherFormView.as_view()),
	url(r'^delete_cost/(?P<rev>[0-9]+)/(?P<pk>[0-9]+)/',
		views.DeleteCostView.as_view()),
	url(r'^send/(?P<pk>[0-9]+)/', views.SendView.as_view()),
]