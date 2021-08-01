from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class TelegramAppConfig(AppConfig):
    """Default configuration for Telegram app."""
    name = "apps.telegram"
    verbose_name = _("Telegram")
