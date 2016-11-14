from django.contrib.auth import get_user_model

from rest_framework import authentication

from rest_framework.filters import (
		SearchFilter,
	)
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView

from rest_framework.permissions import (
		AllowAny,
		IsAuthenticated,
		IsAdminUser,
		IsAuthenticatedOrReadOnly,
	)

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED
from rest_framework.views import APIView

from events.models import Event
from accounts.models import UserProfile

from .serializers import UserProfileSerializer

User = get_user_model()

class UserProfileAPIView(RetrieveAPIView):

	authentication_classes = (authentication.TokenAuthentication,)
	serializer_class = UserProfileSerializer

	def get(self, request, format=None):
		queryset = UserProfile.objects.get(user=request.user)
		serializer = UserProfileSerializer(queryset, context={'request': request})
		return Response(serializer.data)

class UserProfileCreateAPIView(CreateAPIView):
	serializer_class = UserProfileSerializer
	queryset = UserProfile.objects.all()

