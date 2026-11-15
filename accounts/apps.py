from django.apps import AppConfig


class AccountsConfig(AppConfig):
    """
    Configuration for the accounts application.
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    def ready(self):
        """
        Imports signal handlers when the application is ready.
        """
        import accounts.signals