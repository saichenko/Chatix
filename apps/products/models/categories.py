from django.contrib.postgres.fields import CICharField
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models import BaseModel


class Category(BaseModel):
    """Represent users custom product category."""

    parent = models.ForeignKey(
        verbose_name=_("parent category"),
        to="self",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="sub_categories"
    )
    shop = models.ForeignKey(
        verbose_name=_("shop"),
        to="shops.Shop",
        on_delete=models.CASCADE,
        related_name="categories"
    )
    name = CICharField(
        verbose_name=_("name"),
        max_length=16
    )

    def __str__(self):
        # pylint: disable=invalid-str-returned
        return self.name

    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("categories")
