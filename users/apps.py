"""Import AppConfig"""
from django.apps import AppConfig


class UsersConfig(AppConfig):
    """UsersConfig"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        import users.signals
