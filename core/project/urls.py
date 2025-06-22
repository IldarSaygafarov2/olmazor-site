from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from core.project.settings import base

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.apps.main.urls", namespace="main")),
    path("news/", include("core.apps.news.urls", namespace="news")),
    path("employees/", include("core.apps.employees.urls", namespace="employees")),
]


if base.DEBUG:
    urlpatterns += static(base.STATIC_URL, document_root=base.STATIC_ROOT)
    urlpatterns += static(base.MEDIA_URL, document_root=base.MEDIA_ROOT)
