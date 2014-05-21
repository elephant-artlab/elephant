# coding: utf-8
from django.conf.urls import patterns, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('website.views',
	url(r'^$', 'home_view'),
	url(r'^about', 'about_view'),
	url(r'^contact', 'contact_view'),
	url(r'^services', 'services_view'),
	url(r'^test', 'test_view'),
    url(r'^project/(?P<project_id>-?\d+)/$', 'project_view'),
    url(r'^skype', 'skype_view'),
)