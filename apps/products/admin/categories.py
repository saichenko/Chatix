from django.contrib import admin

from ..models.categories import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Represent admin dashboard for model Category."""

    list_display = (
        "name",
        "shop",
        "parent",
    )
    search_fields = (
        "name",
    )
