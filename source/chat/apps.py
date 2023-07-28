from django.apps import AppConfig


class ChatConfig(AppConfig):
    """
    AppConfig for the chat app.

    This AppConfig defines the configuration for the chat app, including the app name and default auto field.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'source.chat'
