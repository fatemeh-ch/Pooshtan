from django.db.models.signals import post_save
from django.dispatch import receiver

from accounts.models import User, Profile, UserType


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    Creates a profile for newly registered customer accounts.

    Args:
        sender: The model class that sent the signal.
        instance: The saved User instance.
        created: Indicates whether a new User instance was created.
        **kwargs: Additional signal arguments.
    """
    if created and instance.user_type == UserType.CUSTOMER:
        Profile.objects.create(user=instance)