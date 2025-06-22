from django.urls import path

from . import views

app_name = "main"

urlpatterns = [
    path("", views.render_home_page, name="home"),
]
