from django.contrib import admin

from ..models.teleorders import TeleOrder


@admin.register(TeleOrder)
class TeleOrderAdmin(admin.ModelAdmin):
    list_display = (
        "product",
        "teleuser",
        "coupon",
        "cost",
        "status",
        "created_at",
        "modified_at",
    )
    list_filter = (
        "status",
        "created_at",
        "modified_at",
    )
