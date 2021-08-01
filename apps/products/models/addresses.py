from django.db import models
from django.utils.translation import gettext as _

from apps.core.models import BaseModel


class Address(BaseModel):
    """Represent address Users ordering."""

    location = models.JSONField(
        verbose_name=_("location")
    )
    details = models.TextField(
        verbose_name=_("additional"),
        max_length=1024,
        help_text=_(
            "Indicate the entrance, floor and other "
            "information for the courier."
        )
    )

    class Meta:
        verbose_name = _("address")
        verbose_name_plural = _("addresses")
