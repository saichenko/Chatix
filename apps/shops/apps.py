from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ShopsAppConfig(AppConfig):
    """Default configuration for Shops app."""
    name = "apps.shops"
    verbose_name = _("Shops")
