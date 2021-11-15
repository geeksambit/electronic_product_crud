from django.db import models

# Create your models here.

import uuid
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken



class UserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

  


class User(AbstractUser):

    class ROLE:
        ADMIN = 'a'
        MANAGER = 'm'
        USER = 'u'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = None
    email = models.EmailField(unique=True)
    ROLE_CHOICES = (
        (ROLE.ADMIN, 'ADMIN'),
        (ROLE.MANAGER, 'MANAGER'),
        (ROLE.USER, 'USER'),
    )
    role = models.CharField(max_length=3, choices=ROLE_CHOICES, default=ROLE.USER)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated At"))

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return "{0}".format(self.email)

    class Meta:
        db_table = 'users'

