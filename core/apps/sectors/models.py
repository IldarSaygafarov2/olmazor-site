from django.db import models

from core.apps.base_app.models import BaseModel


class Sector(BaseModel):
    name = models.CharField(max_length=250, verbose_name="Название сектора")
    address = models.CharField(
        max_length=250, verbose_name="Адрес сектора", blank=True, null=True
    )
    description = models.TextField(
        verbose_name="Описание сектора", blank=True, null=True
    )
    image = models.ImageField(
        upload_to="sectors/images/",
        verbose_name="Изображение сектора",
        blank=True,
        null=True,
    )
    supervisor = models.ForeignKey(
        "employees.Employee",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="sectors",
    )

    def __str__(self) -> str:
        return self.name

    class Meta(BaseModel.Meta):
        verbose_name = "Сектор"
        verbose_name_plural = "Секторы"
        ordering = ["-created_at"]
