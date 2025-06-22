from django.contrib import admin

from .models import NewArticle, NewArticleImage


class NewArticleImageInline(admin.TabularInline):
    """
    Inline admin interface for managing images associated with news articles.
    """

    model = NewArticleImage
    extra = 1


@admin.register(NewArticle)
class NewArticleAdmin(admin.ModelAdmin):
    """
    Admin interface for managing news articles.
    """

    list_display = ("title", "published_date", "created_at", "updated_at")
    search_fields = ("title", "content")
    list_filter = ("published_date",)
    date_hierarchy = "published_date"
    ordering = ("-published_date",)
    inlines = [NewArticleImageInline]
