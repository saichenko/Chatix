from django.contrib import admin

from ..models.products import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Represent admin dashboard for Product model."""

    list_display = (
        "category",
        "shop",
        "name",
        "price",
        "is_hidden",
        "is_digital",
        "created_at",
        "modified_at",
    )
    list_filter = (
        "is_hidden",
        "is_digital",
        "created_at",
        "modified_at",
    )
    search_fields = (
        "name",
        "description",
    )
