from django.contrib.postgres.fields import CICharField
from django.db import models
from django.utils.translation import gettext as _

from apps.core.models import BaseMessengerUserModel


class TeleUser(BaseMessengerUserModel):
    """Represent telegram user."""

    id = models.BigIntegerField(
        verbose_name=_("user id in telegram"),
        primary_key=True
    )
    username = CICharField(
        verbose_name=_("username"),
        max_length=36,
        null=True,
        blank=True
    )

    def __str__(self):
        """Return username if user have it else its id."""
        return self.username if self.username else str(self.id)

    class Meta:
        verbose_name = _("telegram user")
        verbose_name_plural = _("telegram users")
