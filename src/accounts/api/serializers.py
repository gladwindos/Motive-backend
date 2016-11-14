from django.contrib.auth import get_user_model
from django.db.models import Q

from rest_framework.serializers import (
		CharField,
		EmailField,
		ModelSerializer, 
		HyperlinkedIdentityField, 
		SerializerMethodField,
		ValidationError
		)

from events.models import Event, University
from accounts.models import UserProfile

User = get_user_model()

class UserSerializer(ModelSerializer):
	email = EmailField(label="Email address")
	class Meta:
		model = User
		fields = [
			'id',
			'username',
			'email',
			'password',
			'first_name',
			'last_name'
		]
		extra_kwargs = {"password":
							{"write_only": True}
		}

	def validate_email(self, value):
		user_qs = User.objects.filter(email=value)
		if user_qs.exists():
			raise ValidationError("A user with that email address already exists.")
		return value

class UniversitySerializer(ModelSerializer):

	class Meta:
		model = University

class UserProfileSerializer(ModelSerializer):

	user = UserSerializer()
	university = UniversitySerializer()

	class Meta:
		model = UserProfile

	def create(self, validated_data):

		# Create User
		user_obj = User.objects.create(**validated_data['user'])
		user_obj.set_password(validated_data['user']['password'])
		user_obj.save()

		# Get University
		university_name = validated_data['university']['university']
		university = University.objects.get(university=university_name)


		# Create Profile
		profile_obj = UserProfile(
					user = user_obj,
					university = university
					)

		profile_obj.save()
		return validated_data

















