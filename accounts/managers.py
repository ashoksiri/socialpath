from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.db.models import Q
from django.db.models.query import QuerySet


class SocialpathUserManager(BaseUserManager):
    """
    A custom user manager to deal with emails as unique identifiers for auth
    instead of usernames. The default that's used is "UserManager"
    """

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, username=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, email, username, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        user = self.model(email=email, username=username, **extra_fields)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Creates and saves a Superuser with the given email,password,is_staff,is_superuser          and is_active.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, password, **extra_fields)

    def get_client_id(self, user_id):
        try:
            import pdb
            pdb.set_trace()
            client = self.get(id=user_id)
            return client.requested_by_id
        except ObjectDoesNotExist:
            return None

    def get_user_id(self, username):
        try:
            user_id = self.get(email=username)
            return user_id.id
        except ObjectDoesNotExist:
            return None

