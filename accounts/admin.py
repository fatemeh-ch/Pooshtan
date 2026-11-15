from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    
    """
    Customizes the Django admin interface for managing Pooshtan users.

    Defines the displayed columns, filters, search fields,
    and form layouts for viewing, creating, and editing users.
    """

    model = User

    list_display = [
        'email',
        'first_name',
        'last_name',
        'user_type',
        'is_active',
        'is_staff',
        'is_superuser',
    ]

    list_filter = [
        'user_type',
        'is_active',
        'is_staff',
        'is_superuser',
    ]

    ordering = ('email',)

    search_fields = (
        'email',
        'first_name',
        'last_name',
    )

    fieldsets = (
        ('Authentication', {
            'fields': ('email', 'password')
        }),
        ('Personal Information', {
            'fields': (
                'first_name',
                'last_name',
                'user_type',
            )
        }),
        ('Permissions', {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
            )
        }),
        ('Group Permissions', {
            'fields': (
                'groups',
                'user_permissions',
            )
        }),
        ('Important Dates', {
            'fields': (
                'last_login',
                'created_at',
                'updated_at',
            )
        }),
    )

    readonly_fields = (
        'last_login',
        'created_at',
        'updated_at',
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'first_name',
                'user_type',
                'password1',
                'password2',
            ),
        }),
    )

    filter_horizontal = ('groups', 'user_permissions')
