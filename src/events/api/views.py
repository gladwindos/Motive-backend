from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework.filters import (
		SearchFilter,
	)
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST



from events.models import Event
from .serializers import EventDetailSerializer, EventListSerializer, Auth0FavouriteSerializer



class EventDetailAPIView(RetrieveAPIView):
	queryset = Event.objects.all()
	serializer_class = EventDetailSerializer
	lookup_field = 'id'



class EventListAPIView(ListAPIView):
	queryset = Event.objects.filter(start_date__gte=timezone.now(), is_reviewed=True).order_by('start_date') #Event.objects.all()
	serializer_class = EventListSerializer
	filter_backends = [SearchFilter]
	search_fields = ['title', 'user__username', 'university__university']

class Auth0FavouritesAPIView(UpdateAPIView):
	queryset = Event.objects.all()
	serializer_class = Auth0FavouriteSerializer
	lookup_field = 'id'

	def update(self, request, *args, **kwargs):
		favourite_id = request.data.get("auth0_favourite_ids")
		instance = self.get_object()

		if not instance.auth0_favourite_ids:
			instance.auth0_favourite_ids = []

		if favourite_id in instance.auth0_favourite_ids:
			instance.auth0_favourite_ids.remove(favourite_id)
		else:
			instance.auth0_favourite_ids.append(favourite_id)
		
		instance.save()

		serializer = self.get_serializer(instance, data=request.data)
		serializer.is_valid(raise_exception=True)
		self.perform_update(serializer)
		return Response(serializer.data, status=HTTP_200_OK)




	# def get_queryset(self, *args, **kwargs):
	# 	queryset_list = super(EventListAPIView, self)
	# 	query = request.GET.get("q")
	# 	if query


