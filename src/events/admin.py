from django.contrib import admin

# Register your models here.

from .models import Event, University

class EventModelAdmin(admin.ModelAdmin):
	list_display = ["title", "user", "start_date", "updated"]
	search_fields = ["title", "user__username", "university__university"]
	list_filter = ('title','university')

admin.site.register(Event, EventModelAdmin)

admin.site.register(University)