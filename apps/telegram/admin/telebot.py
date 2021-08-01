from django.contrib import admin

from ..models.telebots import TeleBot


@admin.register(TeleBot)
class TeleBotAdmin(admin.ModelAdmin):
    list_display = (
        "shop",
        "username",
    )
    list_filter = (
        "created_at",
        "modified_at",
    )
    search_fields = (
        "username",
        "token",
    )
