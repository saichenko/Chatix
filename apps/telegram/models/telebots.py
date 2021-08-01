from django.contrib.postgres.fields import CICharField
from django.db import models
from django.utils.translation import gettext as _

from apps.core.models import BaseModel


class TeleBot(BaseModel):
    """Represent telegram bot."""

    shop = models.OneToOneField(
        verbose_name=_("shop"),
        to="shops.Shop",
        on_delete=models.CASCADE
    )
    username = CICharField(
        verbose_name=_("bot name"),
        max_length=60,
        unique=True
    )
    token = CICharField(
        verbose_name=_("token"),
        max_length=36,
        unique=True
    )

    def __str__(self):
        # pylint: disable=invalid-str-returned
        return self.username

    class Meta:
        verbose_name = _("telegram bot")
        verbose_name_plural = _("telegram bots")
