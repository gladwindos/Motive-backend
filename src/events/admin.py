from django.contrib import admin

# Register your models here.

from .models import Event

class EventModelAdmin(admin.ModelAdmin):
	list_display = ["title", "user", "start_date", "updated"]
	search_fields = ["title", "user__username"]

admin.site.register(Event, EventModelAdmin)