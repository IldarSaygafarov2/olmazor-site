from django.contrib import admin

from .models import Sector


@admin.register(Sector)
class SectorAdmin(admin.ModelAdmin):
    """
    Admin interface for managing sectors.
    """

    list_display = ("name", "supervisor", "created_at", "updated_at")
    search_fields = ("name", "description")
    list_filter = ("supervisor", "created_at", "updated_at")
    ordering = ("-created_at",)
    readonly_fields = ("created_at", "updated_at")
