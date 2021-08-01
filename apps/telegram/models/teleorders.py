from django.db import models
from django.utils.translation import gettext as _

from apps.core.models import BaseOrderModel


class TeleOrder(BaseOrderModel):
    """Represent Telegram bot order."""

    teleuser = models.ForeignKey(
        verbose_name=_("telegram user"),
        to="telegram.TeleUser",
        on_delete=models.PROTECT
    )

    class Meta:
        verbose_name = _("Telegram order")
        verbose_name_plural = _("Telegram orders")
