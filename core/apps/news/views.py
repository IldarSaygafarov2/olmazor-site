from django.http import HttpRequest
from django.shortcuts import render

from .models import NewArticle


def render_news_page(request: HttpRequest):
    """
    Render the news page.
    """
    objects = NewArticle.objects.all()
    context = {
        "news": objects,
    }
    return render(request, "apps/news/index.html", context)


def render_news_detail_page(request: HttpRequest, article_id: str):
    """
    Render the news detail page for a specific article.
    """
    context = {
        "article_id": article_id,
    }
    return render(request, "apps/news/detail.html", context)
