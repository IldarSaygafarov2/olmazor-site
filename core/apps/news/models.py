from django.db import models
from core.apps.base_app.models import BaseModel


class NewArticle(BaseModel):
    """
    Model representing a news article.
    """

    title = models.CharField(max_length=255, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержание")
    poster = models.ImageField(
        upload_to="news/posters/",
        verbose_name="Постер",
        blank=True,
        null=True,
    )
    published_date = models.DateField(verbose_name="Дата публикации")

    class Meta(BaseModel.Meta):
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ["-published_date"]

    def __str__(self):
        return self.title


class NewArticleImage(BaseModel):
    """
    Model representing an image associated with a news article.
    """

    article = models.ForeignKey(
        NewArticle,
        on_delete=models.CASCADE,
        related_name="images",
        verbose_name="Статья",
    )
    image = models.ImageField(upload_to="news/images/", verbose_name="Изображение")

    class Meta(BaseModel.Meta):
        verbose_name = "Изображение новости"
        verbose_name_plural = "Изображения новостей"

    def __str__(self):
        return f"Image for {self.article.title}"
