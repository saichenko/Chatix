from django.contrib import admin

from ..models.product_instances import ProductInstance


@admin.register(ProductInstance)
class ProductInstanceAdmin(admin.ModelAdmin):
    """Represent admin dashboard for ProductInstance model."""

    list_display = (
        "product",
        "is_bought",
        "created_at",
        "modified_at",
    )
    list_filter = (
        "is_bought",
        "created_at",
        "modified_at",
    )
    search_fields = (
        "text",
    )
