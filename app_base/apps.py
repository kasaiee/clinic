from django.apps import AppConfig


class AppBaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_base'
