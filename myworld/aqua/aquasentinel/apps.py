from django.apps import AppConfig


class AquasentinelConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'aquasentinel'

    def ready(self):
        import aquasentinel.signals
