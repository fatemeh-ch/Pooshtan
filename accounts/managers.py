from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _

from accounts.choices import UserType


class CustomUserManager(BaseUserManager):
    """
    Custom manager for the Pooshtan User model.

    Provides methods for creating regular users and superusers
    using email as the authentication identifier.
    """

    def create_user(self, email, password=None, **extra_fields):
        """
        Create and return a regular user.

        Normalize the email address, set the user's password
        securely, and save the user to the selected database.

        Args:
            email: The user's unique email address.
            password: The user's raw password.
            **extra_fields: Additional User model fields.

        Returns:
            User: The newly created user instance.

        Raises:
            ValueError: If the email address is not provided.
        """

        if not email:
            raise ValueError(_('Email must be set.'))

        email = self.normalize_email(email)

        user = self.model(
            email=email,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Create and return a superuser.

        Set the required administrative permissions and assign
        the SUPERUSER account type.

        Args:
            email: The superuser's unique email address.
            password: The superuser's raw password.
            **extra_fields: Additional User model fields.

        Returns:
            User: The newly created superuser instance.

        Raises:
            ValueError: If the required administrative flags
            or account type are not correctly configured.
        """

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('user_type', UserType.SUPERUSER)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))

        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        if extra_fields.get('is_active') is not True:
            raise ValueError(_('Superuser must have is_active=True.'))

        if extra_fields.get('user_type') != UserType.SUPERUSER:
            raise ValueError(_('Superuser must have SUPERUSER account type.'))

        return self.create_user(
            email=email,
            password=password,
            **extra_fields
        )