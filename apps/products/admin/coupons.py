from django.contrib import admin

from ..models.coupons import Coupon


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    """Represent admin dashboard for Coupon model."""

    list_display = (
        "code",
        "discount",
        "is_active",
        "expires_in",
    )
    list_filter = (
        "is_active",
        "expires_in",
    )
    search_fields = (
        "code",
    )
