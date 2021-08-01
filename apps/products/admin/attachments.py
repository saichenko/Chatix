from django.contrib import admin

from ..models.attachments import ProductAttachment, ProductInstanceAttachment


@admin.register(ProductAttachment)
class ProductAttachmentAdmin(admin.ModelAdmin):
    """Represent admin dashboard for ProductAttachment moddel."""

    list_display = (
        "product",
        "created_at",
        "modified_at",
    )
    list_filter = (
        "created_at",
        "modified_at",
    )


@admin.register(ProductInstanceAttachment)
class ProductInstanceAttachmentAdmin(admin.ModelAdmin):
    list_display = (
        "product_instance",
        "created_at",
        "modified_at",
    )
    list_filter = (
        "created_at",
        "modified_at",
    )
