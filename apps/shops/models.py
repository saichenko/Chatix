from django.contrib.postgres.fields import CICharField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class Shop(models.Model):
    """Shop model which contains main data for shop bots."""

    CURRENCIES = (
        (1, "USD, $"),
        (2, "EUR, €"),
        (3, "RUB, ₽"),
        (4, "UAH, ₴"),
        (5, "BYN, Br"),
    )
    REQUIRE_PHONE_CASES = (
        (1, _("Always")),
        (2, _("Never")),
        (3, _("If delivery is selected")),
    )

    owner = models.OneToOneField(
        verbose_name=_("owner"),
        to="users.User",
        on_delete=models.CASCADE
    )
    name = CICharField(
        verbose_name=_("name"),
        max_length=64
    )
    description = models.TextField(
        verbose_name=_("description"),
        max_length=1024
    )
    currency = models.PositiveSmallIntegerField(
        verbose_name=_("currency"),
        choices=CURRENCIES,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )
    require_phone_num = models.PositiveSmallIntegerField(
        verbose_name=_("require phone number"),
        choices=REQUIRE_PHONE_CASES,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(3)
        ]
    )
    delivery = models.BooleanField(
        verbose_name=_("is delivery available"),
        default=False
    )
    min_delivery_price = models.DecimalField(
        verbose_name=_("minimum price for delivery"),
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )
    image = models.ImageField(
        verbose_name=_("image"),
        upload_to="shops/",
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("shop")
        verbose_name_plural = _("shops")
