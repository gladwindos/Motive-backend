from django.contrib import admin

# Register your models here.

from .models import Event, University, Venue

class EventModelAdmin(admin.ModelAdmin):
	list_display = ["title", "user", "start_date", "updated", "is_reviewed"]
	search_fields = ["title", "user__username", "university__university", "is_reviewed"]
	list_filter = ('title','university')

admin.site.register(Event, EventModelAdmin)

admin.site.register(University)

admin.site.register(Venue)