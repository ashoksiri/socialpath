from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db import models

from accounts.managers import SocialpathUserManager

STATUS_CHOICES = (
    (0, 'inactive'),
    (1, 'active')
)

class User(AbstractUser):

    REQUIRED_FIELDS = []

    GENDER_CHOICES = (
        ('male', 'male'),
        ('female', 'female'),
        ('other', 'other')
    )
    USER_TYPE_CHOICES = (
        (1, 'admin'),
        (2, 'manager'),
        (3, 'user')
    )
    age = models.IntegerField(
        null=True,
        blank=True,
        default=10,
        help_text="age of the user"
    )
    gender = models.CharField(
        max_length=6,
        choices=GENDER_CHOICES,
        null=True,
        blank=True,
        default='male',
        help_text="gender of the user"

    )
    phone = models.CharField(
        max_length=20,
        verbose_name='Phone number',
        null=True,
        blank=True,
        help_text="phone number of the user"
    )
    profile_picture = models.FileField(
        null=True,
        blank=True,
        help_text="profile picture of the user",
        max_length=500
    )

    username = models.CharField(
        unique=True,
        max_length=255,
        help_text="unique user name of the user"
    )
    email = models.EmailField(_('email address'), blank=False, unique=True)
    requested_by = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(max_length=500, null=True, blank=True)
    job_role = models.CharField(max_length=50, null=True, blank=True)

    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    updated_time = models.DateTimeField(auto_now=True)

    objects = SocialpathUserManager()

    def __str__(self):
        return self.username
