"""felis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from ajax_select import urls as ajax_select_urls

urlpatterns = [
	url(r'^', include('employees.urls')),
    url(r'^accounts/', include('employees.urls')),
    url(r'^leaves/', include('leaves.urls')),
    url(r'^trips/', include('trips.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^messages/', include('postman.urls', namespace="postman",
        app_name="postman")),
    url(r'^calendar/', include('calendarium.urls')),
    url(r'^autocomplete/', include(ajax_select_urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)