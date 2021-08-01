from django.contrib import admin

from .models import Shop


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = (
        "owner",
        "name",
        "require_phone_num",
        "currency",
        "delivery",
        "min_delivery_price",
    )
    list_filter = (
        "currency",
        "require_phone_num",
        "delivery",
    )
    search_fields = (
        "name",
        "description",
    )
