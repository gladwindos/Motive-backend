from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings 
from django.utils import timezone

# Create your models here.

def upload_location(instance, filename):
	return "%s/%s" %(instance.id, filename)

# class Image(models.Model):
# 	event = models.ForeignKey(Event)
# 	poster = models.ImageField(upload_to=upload_location, null=True, blank=False)

# 	def __str__(self):
# 		return "%s " %(event.title)
	

class Event(models.Model):
	title = models.CharField(max_length=120)
	poster = models.ImageField(upload_to=upload_location, null=True, blank=False)
	start_date = models.DateTimeField(auto_now=False, auto_now_add=False, default=timezone.now)   # Remove default
	end_date = models.DateTimeField(auto_now=False, auto_now_add=False, default=timezone.now) 	# Remove default
	ticket_link = models.URLField(null=True, blank=True)
	description = models.TextField(max_length=5000, blank=True, null=True)
	venue_name = models.CharField(max_length=40)
	venue_address = models.CharField(max_length=40)
	venue_city = models.CharField(max_length=40)
	venue_postcode = models.CharField(max_length=10)
	contact_details = models.TextField(max_length=120)
	ticket_link = models.URLField(null=True, blank=True)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
	is_reviewed = models.BooleanField(default=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("events:detail", kwargs={"id": self.id})

	class Meta:
		ordering = ["start_date", "end_date"]
