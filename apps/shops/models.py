from django.contrib.postgres.fields import CICharField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class Shop(models.Model):
    """Shop model which contains main data for shop bots."""

    CURRENCIES = (
        (1, "USD"),
        (2, "EUR"),
        (3, "RUB"),
        (4, "UAH"),
        (5, "BYN"),
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
