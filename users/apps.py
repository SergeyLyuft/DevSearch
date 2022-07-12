from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
#register signals which we have in signals.py
    def ready(self):
        import users.signals
