from django.db import models
from django.utils.translation import gettext as _


class BaseModel(models.Model):
    """Base model for apps' models.

    This class adds to models `created_at` and `modified_at` fields.
    """

    created_at = models.DateTimeField(
        verbose_name=_("created at"),
        auto_now_add=True
    )
    modified_at = models.DateTimeField(
        verbose_name=_("modified at"),
        auto_now=True
    )

    class Meta:
        abstract = True


class BaseAttachmentModel(BaseModel):
    """Base model for attachment models.

    This class adds to models `file` field. Inherited from `BaseModel`.
    """

    file = models.FileField(
        verbose_name=_("file"),
        upload_to="attachments/"
    )

    class Meta:
        abstract = True
