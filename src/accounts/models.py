from django.db import models

# Create your models here.
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from events.models import University

class UserProfile(models.Model):
	user = models.OneToOneField(User, related_name='user')
	university = models.ForeignKey(University, null=False, blank=False) # add default later

	def __str__(self):
		user = self.user
		return "%ss Profile" %user

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

        