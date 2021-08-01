from datetime import date

from django.contrib.postgres.fields import CICharField
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models import BaseModel


class Coupon(BaseModel):
    """Represent discount coupon."""

    products = models.ManyToManyField(
        verbose_name=_("products"),
        to="products.Product"
    )
    code = CICharField(
        verbose_name=_("code"),
        max_length=16
    )
    discount = models.PositiveSmallIntegerField(
        verbose_name=_("discount"),
        validators=[
            MinValueValidator(1),
            MaxValueValidator(100)
        ]
    )
    is_active = models.BooleanField(
        verbose_name=_("is active"),
        default=True
    )
    expires_in = models.DateField(
        verbose_name=_("expires in"),
        blank=True,
        null=True,
        validators=[
            MinValueValidator(date.today())
        ]
    )

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = _("coupon")
        verbose_name_plural = _("coupons")
