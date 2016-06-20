from django.conf.urls import url
from django.contrib import admin

from .views import (

	event_feed,
	event_create,
	event_detail,
	event_update,
	event_delete
	)

urlpatterns = [

	url(r'^$', event_feed, name='feed'),
	url(r'^create/$', event_create, name='create'),
	url(r'^(?P<id>\d+)/$', event_detail, name='detail'),
	url(r'^(?P<id>\d+)/edit/$', event_update, name='update'),
	url(r'^(?P<id>\d+)/delete/$', event_delete, name='delete'),
]