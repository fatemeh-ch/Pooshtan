from django.db import models
from django.utils.translation import gettext_lazy as _


class UserType(models.TextChoices):
    """
    Defines the available account types in Pooshtan.
    """

    CUSTOMER = 'customer', _('مشتری')
    ADMIN = 'admin', _('مدیر فروشگاه')
    SUPERUSER = 'superuser', _('مدیر سیستم')