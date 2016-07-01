from rest_framework.serializers import (
		ModelSerializer, 
		HyperlinkedIdentityField, 
		SerializerMethodField
		)

from events.models import Event

event_detail_url = HyperlinkedIdentityField(
			view_name='events-api:detail',
			lookup_field='id',
			)

class EventListSerializer(ModelSerializer):
	url = event_detail_url

	# user = SerializerMethodField()

	class Meta:
		model = Event
		fields = [
			'id',
			'url',
			'title',
			'university',
			'poster',
			'start_date',
			'end_date',
			'ticket_link',
			'description',
			'venue_name',
			'venue_address',
			'venue_city',
			'venue_postcode',
			'contact_details',
		]

	def get_user(self, obj):
		return str(obj.user.username)


class EventDetailSerializer(ModelSerializer):
	# user = SerializerMethodField()
	poster = SerializerMethodField()
	class Meta:
		model = Event
		fields = [
			'id',
			'title',
			'university',
			'poster',
			'start_date',
			'end_date',
			'ticket_link',
			'description',
			'venue_name',
			'venue_address',
			'venue_city',
			'venue_postcode',
			'contact_details',
			'ticket_link',
		]

	def get_user(self, obj):
		return str(obj.user.username)

	def get_poster(self, obj):
		try:
			poster = obj.poster.url
		except:
			poster = None
		return poster















