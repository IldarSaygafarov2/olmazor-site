from django.urls import path

from . import views

app_name = "employees"

urlpatterns = [
    path("", views.render_employees_page, name="home"),
]
