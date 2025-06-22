import uuid
from django.db import models


class BaseModel(models.Model):
    """
    An abstract base model that provides common fields and methods for all models.
    """

    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
        verbose_name="Уникальный идентификатор",
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        abstract = True
        ordering = ["-created_at"]
