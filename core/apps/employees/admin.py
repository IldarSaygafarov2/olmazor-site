from django.contrib import admin

from .models import Employee, EmployeeType


@admin.register(EmployeeType)
class EmployeeTypeAdmin(admin.ModelAdmin):
    """
    Admin interface for managing EmployeeType model.
    """

    list_display = ["name"]
    list_display_links = ["name"]
    search_fields = ["name"]
    ordering = ["-created_at"]


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    """
    Admin interface for managing Employee model.
    """

    list_display = [
        "get_full_name",
        "email",
        "position",
        "employee_type",
    ]
    list_editable = ["employee_type"]
    list_display_links = ["get_full_name"]
    search_fields = ["first_name", "last_name", "email", "position"]
    list_filter = ["employee_type"]
