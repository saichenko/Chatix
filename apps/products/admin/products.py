from django.contrib import admin

from ..models.products import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "category",
        "shop",
        "name",
        "price",
        "is_hidden",
        "has_instances",
        "created_at",
        "modified_at",
    )
    list_filter = (
        "is_hidden",
        "has_instances",
        "created_at",
        "modified_at",
    )
    search_fields = (
        "name",
        "description",
    )
