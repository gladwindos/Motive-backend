from django.conf.urls import url
from django.contrib import admin

from .views import (
	EventDetailAPIView,
	EventListAPIView,

	)

urlpatterns = [

	url(r'^$', EventListAPIView.as_view(), name='list'),
	# url(r'^create/$', event_create, name='create'),
	url(r'^(?P<id>\d+)/$', EventDetailAPIView.as_view(), name='detail'),
	# url(r'^(?P<id>\d+)/edit/$', event_update, name='update'),
	# url(r'^(?P<id>\d+)/delete/$', event_delete, name='delete'),
]