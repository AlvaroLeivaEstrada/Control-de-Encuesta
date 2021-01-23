

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser

# Utilities
from utils.models import BaseUserModel


class User(BaseUserModel,AbstractUser):

    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique': 'A user with that email already exists.'
        }
    )

    is_client = models.BooleanField(
        'client',
        default=True,
        help_text=(
            'Help easily distinguish users and perform queries. '
            'Clients are the main type of user.'
        )
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    

    def __str__(self):

        return self.username

    def get_short_name(self):
        
        return self.username