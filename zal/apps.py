from django.apps import AppConfig


class ZalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'zal'

    def ready(self):
        from zal import signals
