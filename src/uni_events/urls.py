"""uni_events URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
1. Add an import:  from my_app import views
2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
1. Add an import:  from other_app.views import Home
2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
1. Import the include() function: from django.conf.urls import url, include
2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import RedirectView

from accounts.views import (login_view, register_view, logout_view)
from events.views import event_list

from rest_framework.authtoken import views

urlpatterns = [
	url(r'^$', RedirectView.as_view(pattern_name='events:list')),
	url(r'^admin/', admin.site.urls),
	url(r'^events/', include("events.urls", namespace='events')),
	url(r'^login/', login_view, name='login'),
	url(r'^my-events/', event_list, name='my-events'),
	url(r'^register/', register_view, name='register'),
	url(r'^logout/', logout_view, name='logout'),
	url(r'^api/events/', include("events.api.urls", namespace='events-api')),
	url(r'^api/users/', include("accounts.api.urls", namespace='users-api')),
]

urlpatterns += [
    url(r'^api-token-auth/', views.obtain_auth_token)
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

