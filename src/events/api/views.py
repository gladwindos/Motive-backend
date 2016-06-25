from rest_framework.filters import (
		SearchFilter,
	)
from rest_framework.generics import ListAPIView, RetrieveAPIView

from events.models import Event
from .serializers import EventDetailSerializer, EventListSerializer



class EventDetailAPIView(RetrieveAPIView):
	queryset = Event.objects.all()
	serializer_class = EventDetailSerializer
	lookup_field = 'id'



class EventListAPIView(ListAPIView):
	queryset = Event.objects.all()
	serializer_class = EventListSerializer
	filter_backends = [SearchFilter]
	search_fields = ['title', 'user__username', 'university__university']






	# def get_queryset(self, *args, **kwargs):
	# 	queryset_list = super(EventListAPIView, self)
	# 	query = request.GET.get("q")
	# 	if query


