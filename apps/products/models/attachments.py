from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models import BaseAttachmentModel


class ProductAttachment(BaseAttachmentModel):
    """Represent file attachment for `Product` model."""

    product = models.ForeignKey(
        verbose_name=_("product"),
        to="products.Product",
        on_delete=models.CASCADE
    )

    def __str__(self):
        # pylint: disable=invalid-str-returned
        return self.product.name

    class Meta:
        verbose_name = _("product attachment")
        verbose_name_plural = _("product attachments")


class ProductInstanceAttachment(BaseAttachmentModel):
    """Represent file attachment for `ProductInstance` model."""

    product_instance = models.ForeignKey(
        verbose_name=_("product instance"),
        to="products.ProductInstance",
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.product_instance.product.name

    class Meta:
        verbose_name = _("product instance attachment")
        verbose_name_plural = _("product instance attachments")
