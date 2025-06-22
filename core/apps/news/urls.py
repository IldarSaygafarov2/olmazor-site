from django.urls import path

from . import views

app_name = "news"

urlpatterns = [
    path("", views.render_news_page, name="home"),
    path("<str:article_id>/", views.render_news_detail_page, name="detail"),
]
