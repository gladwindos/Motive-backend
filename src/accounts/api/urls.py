from django.conf.urls import url
from django.contrib import admin

from .views import (
	UserCreateAPIView,
	UserLoginAPIView,
	UserDetailAPIView
	)

urlpatterns = [

	url(r'^login/$', UserLoginAPIView.as_view(), name='login'),
	url(r'^register/$', UserCreateAPIView.as_view(), name='register'),
	url(r'^user-detail/$', UserDetailAPIView.as_view(), name='user-detail'),


]