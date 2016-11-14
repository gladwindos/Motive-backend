from django.conf.urls import url
from django.contrib import admin

from .views import (
	UserProfileAPIView,
	UserProfileCreateAPIView,
	)

urlpatterns = [
	url(r'^user-profile/$', UserProfileAPIView.as_view(), name='user-profile'),
	url(r'^create-profile/$', UserProfileCreateAPIView.as_view(), name='create-profile'),
]