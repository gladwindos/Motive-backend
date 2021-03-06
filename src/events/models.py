from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.urlresolvers import reverse
from django.conf import settings 
from django.utils import timezone

# Create your models here.

def upload_location(instance, filename):
	return "%s/main/%s" %(instance.id, filename)

def upload_location_feed(instance, filename):
	return "%s/feed/%s" %(instance.id, filename)

class University(models.Model):
	university = models.CharField(max_length=120)

	def __str__(self):
		return self.university

class Venue(models.Model):
	name = models.CharField(max_length=60)
	address = models.CharField(max_length=60, null=True, blank=True)
	city = models.CharField(max_length=60, null=True, blank=True)
	postcode = models.CharField(max_length=10, null=True, blank=True)

	def __str__(self):
		return self.name

class Event(models.Model):
	title = models.CharField(max_length=120)
	poster = models.ImageField(upload_to=upload_location, null=True, blank=False)
	feed_poster = models.ImageField(upload_to=upload_location_feed, null=True, blank=True)
	university = models.ManyToManyField(University)
	start_date = models.DateTimeField(auto_now=False, auto_now_add=False, default=timezone.now)   # Remove default
	end_date = models.DateTimeField(auto_now=False, auto_now_add=False, default=timezone.now) 	# Remove default
	ticket_link = models.URLField(null=True, blank=True)
	description = models.TextField(max_length=5000, blank=True, null=True)

	venue = models.OneToOneField(Venue, on_delete=models.CASCADE, null=True, blank=True)

	venue_name = models.CharField(max_length=40, blank=True,null=True)
	venue_address = models.CharField(max_length=40, blank=True,null=True)
	venue_city = models.CharField(max_length=40, blank=True,null=True)
	venue_postcode = models.CharField(max_length=10, blank=True,null=True)

	contact_details = models.TextField(max_length=120, blank=True,null=True)
	ticket_link = models.URLField(null=True, blank=True)
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	is_reviewed = models.BooleanField(default=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	auth0_favourite_ids = ArrayField(models.CharField(max_length=50, null=True, blank=True), blank=True, null=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("events:detail", kwargs={"id": self.id})

	class Meta:
		ordering = ["start_date", "end_date"]
