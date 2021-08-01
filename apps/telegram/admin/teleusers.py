from django.contrib import admin

from ..models.teleusers import TeleUser


@admin.register(TeleUser)
class TeleUserAdmin(admin.ModelAdmin):
    """Represent admin dashboard for TeleUser model."""

    list_display = (
        "id",
        "username",
        "phone_num",
        "created_at",
        "modified_at",
    )
    list_filter = (
        "created_at",
        "modified_at",
    )
    search_fields = (
        "id",
        "username",
        "phone_num",
    )
