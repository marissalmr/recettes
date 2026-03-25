from django.apps import AppConfig


class AuthentificationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'authentification'

class Triggers(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'recettes'
    def ready(self):
        import recettes.signals