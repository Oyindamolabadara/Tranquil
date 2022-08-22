"""Apps"""
from django.apps import AppConfig


class BlogConfig(AppConfig):
    """Configuring the Blog App"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
