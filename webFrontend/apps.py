from django.apps import AppConfig


class WebfrontendConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'webFrontend'

    def ready(self):
        import webFrontend.signals
