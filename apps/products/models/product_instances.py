from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models import BaseModel


class ProductInstance(BaseModel):
    """Represent instance of `Product` model."""

    product = models.ForeignKey(
        verbose_name=_("product"),
        to="products.Product",
        on_delete=models.CASCADE
    )
    text = models.TextField(
        verbose_name=_("text"),
        blank=True,
        null=True
    )
    is_bought = models.BooleanField(
        verbose_name=_("is bought"),
        default=False
    )

    def __str__(self):
        # pylint: disable=invalid-str-returned
        return self.product.name

    class Meta:
        verbose_name = _("product instance")
        verbose_name_plural = _("product instances")
