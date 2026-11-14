from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from django.db import models

from .choices import UserType
from .managers import CustomUserManager

# Create your models here.


class User(AbstractUser):
    """
    Custom user model for Pooshtan.

    Uses email as the authentication identifier instead of username.
    Stores the user's personal name and account type.
    """

    objects = CustomUserManager()

    username = None

    email = models.EmailField(
        _('email address'),
        max_length=255,
        unique=True
    )

    first_name = models.CharField(
        _('first name'),
        max_length=150
    )

    user_type = models.CharField(
        _('user type'),
        max_length=10,
        choices=UserType.choices,
        default=UserType.CUSTOMER
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']

    def __str__(self):
        """Return the user's email and full name."""

        full_name = f'{self.first_name} {self.last_name}'.strip()
        return f'{self.email} - {full_name}'
