from django.contrib import admin

from website.models import ContactModel


@admin.register(ContactModel)
class ContactAdmin(admin.ModelAdmin):
    """
    Configures the Django admin interface for managing contact messages.

    Provides date-based navigation, filtering, searching, and
    a customized layout for displaying and reviewing messages.
    """

    date_hierarchy = 'created_date'

    list_display = [
        'user_full_name',
        'short_subject',
        'is_reviewed',
        'created_date',
    ]

    list_filter = ('is_reviewed',)

    fields = [
        'subject',
        ('user_full_name', 'email'),
        'message',
        'is_reviewed',
    ]

    ordering = ('-created_date',)

    search_fields = [
        'subject',
        'message',
        'user_full_name',
        'email',
    ]
