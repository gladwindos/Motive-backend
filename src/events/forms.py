from django import forms

from .models import Event

class EventForm(forms.ModelForm):

	class Meta:
		model = Event
		fields = [
			"title",
			'university',
			"poster",
			"start_date",
			"end_date",
			"description",
			"venue_name",
			"venue_address",
			"venue_city",
			"venue_postcode",
			"contact_details",
			"ticket_link",
		]