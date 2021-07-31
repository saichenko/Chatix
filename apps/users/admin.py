from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import gettext_lazy as _


from .models import User


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    """UI for User model."""
    ordering = ("email", )
    list_display = (
        "email",
        "is_staff",
        "is_superuser",
    )
    list_display_links = (
        "email",
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "password1", "password2"),
        }),
    )
    fieldsets = (
        (None, {
            "fields": (
                "email",
                "password"
            )
        }),
        (_("Permissions"), {
            "fields": (
                "is_active",
                "is_staff",
                "is_superuser",
                "groups",
                "user_permissions"
            )
        }),
        (_("Important dates"), {
            "fields": (
                "created_at",
                "modified_at"
            )
        }),
    )
    readonly_fields = DjangoUserAdmin.readonly_fields + (
        "created_at",
        "modified_at",
    )
