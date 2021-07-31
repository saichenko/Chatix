from django.contrib import admin

from .models import Shop


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = (
        "owner",
        "name",
        "currency",
    )
    list_filter = (
        "currency",
    )
    search_fields = (
        "name",
        "description",
    )
