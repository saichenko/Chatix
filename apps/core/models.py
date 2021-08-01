from django.db import models
from django.utils.translation import gettext as _


class BaseModel(models.Model):
    """Base model for apps' models.

    This class adds to models `created_at` and `modified_at` fields.
    """

    created_at = models.DateTimeField(
        verbose_name=_("created at"),
        auto_now_add=True
    )
    modified_at = models.DateTimeField(
        verbose_name=_("modified at"),
        auto_now=True
    )

    class Meta:
        abstract = True


class BaseAttachmentModel(BaseModel):
    """Base model for attachment models.

    This class adds to models `file` field. Inherited from `BaseModel`.
    """

    file = models.FileField(
        verbose_name=_("file"),
        upload_to="attachments/"
    )

    class Meta:
        abstract = True


class BaseOrderModel(BaseModel):
    """Base model for order models.

    This class adds to models: `product`, `coupon`, `cost`, `status`.
    Inherited from `BaseModel`.
    """

    STATUSES = (
        (1, _("Pending")),
        (2, _("Shipped")),
        (3, _("Completed")),
        (4, _("Declined")),
        (5, _("Canceled")),
        (6, _("Refunded")),
    )

    product = models.ForeignKey(
        verbose_name=_("product"),
        to="products.Product",
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    coupon = models.ForeignKey(
        verbose_name=_("coupon"),
        to="products.Coupon",
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    cost = models.DecimalField(
        verbose_name=_("price"),
        max_digits=10,
        decimal_places=2
    )
    status = models.PositiveSmallIntegerField(
        verbose_name=_("status"),
        choices=STATUSES,
        blank=True,
        null=True
    )

    class Meta:
        abstract = True


class BaseMessengerUserModel(BaseModel):
    """Represent user of messenger.

    This class adds field `phone_num` to model. Inherited from `BaseModel`.
    """

    phone_num = models.CharField(
        verbose_name=_("phone number"),
        max_length=18,
        null=True,
        blank=True
    )
    addresses = models.ManyToManyField(
        verbose_name=_("addresses"),
        to="products.Address",
        blank=True
    )
    used_coupons = models.ManyToManyField(
        verbose_name=_("used coupons"),
        to="products.Coupon",
        blank=True
    )

    class Meta:
        abstract = True
