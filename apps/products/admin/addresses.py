from django.contrib import admin

from ..models.addresses import Address


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    """Represent admin dashboard for Address."""

    list_display = (
        "created_at",
        "modified_at",
    )
    list_filter = (
        "created_at",
        "modified_at",
    )
