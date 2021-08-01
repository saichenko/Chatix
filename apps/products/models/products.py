from django.contrib.postgres.fields import CICharField
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models import BaseModel


class Product(BaseModel):
    """Represent product of shop."""

    category = models.ForeignKey(
        verbose_name=_("category"),
        to="products.Category",
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    shop = models.ForeignKey(
        verbose_name=_("shop"),
        to="shops.Shop",
        on_delete=models.CASCADE
    )
    name = CICharField(
        verbose_name=_("name"),
        max_length=128
    )
    description = models.TextField(
        verbose_name=_("description"),
        null=True,
        blank=True
    )
    image = models.ImageField(
        verbose_name=_("image"),
        upload_to="products/",
        blank=True,
        null=True
    )
    price = models.DecimalField(
        verbose_name=_("price"),
        max_digits=10,
        decimal_places=2
    )
    amount = models.PositiveSmallIntegerField(
        verbose_name=_("amount"),
        blank=True,
        null=True
    )
    is_hidden = models.BooleanField(
        verbose_name=_("is hidden"),
        default=False
    )
    is_digital = models.BooleanField(
        verbose_name=_("is digital product"),
        default=False
    )

    def __str__(self):
        # pylint: disable=invalid-str-returned
        return self.name

    class Meta:
        verbose_name = _("product")
        verbose_name_plural = _("products")
