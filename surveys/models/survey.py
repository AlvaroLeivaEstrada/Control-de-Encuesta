# Django
from django.db import models

# Models
from users.models.users import User

# Utilities
from utils.models import BaseUserModel


class Survey(models.Model):

	title = models.CharField(max_length=20, blank=False)
	about = models.CharField(max_length=240, blank=False)
	# user = models.ForeignKey(User, on_delete=models.CASCADE)
	average = models.PositiveIntegerField(default=0)